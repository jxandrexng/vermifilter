#include <NewPing.h> //Ultrasonic Sensor Library
#include <OneWire.h> //Temperature Sensor Library

// CONSTANTS
#define TRIGGER1_PIN    12  // Arduino pin tied to trigger pin on the first ultrasonic sensor.
#define ECHO1_PIN       11  // Arduino pin tied to echo pin on the first ultrasonic sensor.
#define TRIGGER2_PIN    10  // Arduino pin tied to trigger pin on the second ultrasonic sensor.
#define ECHO2_PIN        9  // Arduino pin tied to echo pin on the second ultrasonic sensor.
#define RELAY1           3  // Arduino pin tied to relay1 pin of the influent pump.
#define RELAY2           4  // Arduino pin tied to relay2 pin of the mixing pump1.
#define RELAY3           5  // Arduino pin tied to relay3 pin of the soda ash pump.
#define RELAY4           6  // Arduino pin tied to relay4 pin of the mixing pump2.
#define RELAY5           7  // Arduino pin tied to relay5 pin of solenoid valve.
#define TURBIDITY1_PIN  50 // Arduino pin tied to turbidity1 sensor.
#define TURBIDITY2_PIN  52 // Arduino pin tied to turbidity2 sensor.
#define PH_SENSOR1_PIN  A8 // Arduino pin tied to ph1 sensor.
#define PH_SENSOR2_PIN  A10 // Arduino pin tied to ph2 sensor.
#define MOISTURE_PIN    A4 // Arduino pin tied to soil moisture sensor.
#define TEMPERATURE_PIN A5 // Arduino pin tied to temperature sensor.
#define MAX_DISTANCE    30 // Maximum distance we want to ping for (in centimeters). Maximum sensor distance is rated at 400-500cm.
#define Offset1          0.10  //Deviation compensate for pH Sensor1.
#define Offset2          0.26  //Deviation compensate for pH Sensor2.
#define ArrayLength1     40 // Times of collection for pH values.
#define ArrayLength2     40 // Times of collection for pH values.


// DECLARATION
boolean initStatus = 0; //Store initialization status
boolean relay5_State = 0; //Store relay5 status
boolean relay3_State = 0;
boolean isFull = 0; //Store container status
boolean ef_isFull = 0;
char incoming; //Incoming value for serial
float pHUnit1, pHUnit2, temperature, pHvoltage1, pHvoltage2, voltage1, voltage2;
float max_distance1 = 24.0, max_distance2 = 25.0;
int pHArray1[ArrayLength1];   //Store the average value of the sensor feedback
int pHArrayIndex1 = 0;
int pHArray2[ArrayLength2];   //Store the average value of the sensor feedback
int pHArrayIndex2 = 0;
int distance1, distance2, moistureValue, sensorValue1, sensorValue2;
unsigned long interval_On = 25000, interval_Off = 100, previousMillis1 = 0, previousMillis2 = 0, previousMillis3 = 0, previousMillis4 = 0, previousMillis5 = 0;
OneWire ds(TEMPERATURE_PIN);
NewPing sonar1(TRIGGER1_PIN, ECHO1_PIN, MAX_DISTANCE); // NewPing setup of pins and maximum distance. Ultrasonic Sensor NewPing1
NewPing sonar2(TRIGGER2_PIN, ECHO2_PIN, MAX_DISTANCE); // NewPing setup of pins and maximum distance. Ultrasonic Sensor NewPing2

// SETUP
void setup() {
  Serial.begin(2000000); //Begin serial transmission at 2000000 Baud rate
  pinMode(RELAY1, OUTPUT); //Set relay1 as output.
  pinMode(RELAY2, OUTPUT); //Set relay2 as output.
  pinMode(RELAY3, OUTPUT); //Set relay3 as output.
  pinMode(RELAY4, OUTPUT); //Set relay4 as output.
  pinMode(RELAY5, OUTPUT); //Set relay5 as output.
  pinMode(TURBIDITY1_PIN, INPUT); //Set turbidity1 as input.
  pinMode(TURBIDITY2_PIN, INPUT); //Set turbidity2 as input.
}

// LOOP
void loop() {
  main_printF();
  if (Serial.available() > 0) {
    incoming = Serial.read(); //Read transmitted input from Raspberry Pi
    if (incoming == '1') {
      initStatus = true;
      digitalWrite(RELAY1, HIGH); //Pump water to influent container.
      while (initStatus) {
        main_printF();
        if (distance1 > 11 && distance1 <= 30 && !isFull) {
          digitalWrite(RELAY1, HIGH); //Pump water to influent container until it is full.
          digitalWrite(RELAY4, HIGH); //Turn on mixing pump
          digitalWrite(RELAY2, HIGH);
          if (pHUnit1 < 6.00) {
            unsigned long currentMillis5 = millis();
            if (!relay3_State && currentMillis5 - previousMillis5 >= 5000) {
              previousMillis5 = millis();
              relay3_State = true;
              digitalWrite(RELAY3, relay3_State);
            }
            else if (relay3_State && currentMillis5 - previousMillis5 >= 100) {
              previousMillis5 = millis();
              relay3_State = false;
              digitalWrite(RELAY3, relay3_State);
            }
          }
        }
        else if (distance1 != 0 && !ef_isFull) { //Check if influent container is full.
          isFull = true;
          digitalWrite(RELAY4, HIGH); //Turn on mixing pump
          digitalWrite(RELAY2, HIGH);
          digitalWrite(RELAY1, LOW); //Turn off influent pump
          if (pHUnit1 < 6.00) {
            unsigned long currentMillis5 = millis();
            if (!relay3_State && currentMillis5 - previousMillis5 >= 5000) {
              previousMillis5 = millis();
              relay3_State = true;
              digitalWrite(RELAY3, relay3_State);
            }
            else if (relay3_State && currentMillis5 - previousMillis5 >= 100) {
              previousMillis5 = millis();
              relay3_State = false;
              digitalWrite(RELAY3, relay3_State);
            }
          }
          else if (pHUnit1 > 6.00) {
            digitalWrite(RELAY3, LOW);
          }
          unsigned long currentMillis2 = millis();
          if (!relay5_State && currentMillis2 - previousMillis2 >= interval_Off && pHUnit1 >= 6.00) { //Every 1000ms
            previousMillis2 = millis(); //0 is replaced with 1000 and so on
            relay5_State = true;
            digitalWrite(RELAY5, relay5_State); //Pump turns off
          }
          else if (relay5_State && currentMillis2 - previousMillis2 >= interval_On && pHUnit1 >= 6.00) {
            previousMillis2 = millis();
            relay5_State = false;
            digitalWrite(RELAY5, relay5_State); //Pump turns on
            distance1_Read(); //Check distance
            distance2_Read();
            if (distance1 != 0 && distance1 == 25 && distance2 != 0 && distance2 > 4 && !ef_isFull) {
              isFull = false;
              digitalWrite(RELAY1, HIGH);
              digitalWrite(RELAY5, LOW);
            } else if (distance1 != 0 && distance2 != 0 && distance2 < 4 && !ef_isFull) {
              initStatus = false;
              ef_isFull = true;
              digitalWrite(RELAY1, LOW);
              digitalWrite(RELAY2, LOW);
              digitalWrite(RELAY3, LOW);
              digitalWrite(RELAY4, LOW);
              digitalWrite(RELAY5, LOW);
            }
          }
        }
        incoming = Serial.read();
        if (incoming == '2') {
          initStatus = false;
          isFull = false;
          digitalWrite(RELAY1, LOW);
          digitalWrite(RELAY2, LOW);
          digitalWrite(RELAY3, LOW);
          digitalWrite(RELAY4, LOW);
          digitalWrite(RELAY5, LOW);
        }
      }
    }
  }
}

void main_printF() {
  unsigned long currentMillis1 = millis();
  if (currentMillis1 - previousMillis1 >= 250) {
    previousMillis1 = millis();
    pH1_Print();
    turbidity1_Print();
    volume1_Print();
    pH2_Print();
    turbidity2_Print();
    volume2_Print();
    moisture_Print();
    temp_Print();
    Serial.print("\n");
  }
}

int distance1_Read() {
  distance1 = sonar1.ping_cm();
  return distance1;
}

void distance1_Print() {
  distance1_Read();
  Serial.print("Distance1: ");
  Serial.print(distance1); // Send ping, get distance in cm and print result (0 = outside set distance range)
  Serial.print(" ");
}

int distance2_Read() {
  distance2 = sonar2.ping_cm();
  return distance2;
}

void distance2_Print() {
  distance2_Read();
  Serial.print("Distance2: ");
  Serial.print(distance2); // Send ping, get distance in cm and print result (0 = outside set distance range)
  Serial.print(" ");
}

float pH1_Read() {
  pHArray1[pHArrayIndex1++] = analogRead(PH_SENSOR1_PIN);
  if (pHArrayIndex1 == ArrayLength1)pHArrayIndex1 = 0;
  pHvoltage1 = averagearray(pHArray1, ArrayLength1) * 5.0 / 1024;
  pHUnit1 = 3.5 * pHvoltage1 + Offset1;
  return pHUnit1;
}

void pH1_Print() {
  pH1_Read();
  Serial.print(pHUnit1);
  Serial.print("pH ");
}

float pH2_Read() {
  pHArray2[pHArrayIndex2++] = analogRead(PH_SENSOR2_PIN);
  if (pHArrayIndex2 == ArrayLength2)pHArrayIndex2 = 0;
  pHvoltage2 = averagearray1(pHArray2, ArrayLength2) * 5.0 / 1024;
  pHUnit2 = 3.5 * pHvoltage2 + Offset2;
  return pHUnit2;
}

void pH2_Print() {
  pH2_Read();
  Serial.print(pHUnit2);
  Serial.print("pH ");
}

void turbidity1_Print() {
  sensorValue1 = digitalRead(TURBIDITY1_PIN);
  //  Serial.print(sensorValue1);
  //  Serial.print(" ");
  if (sensorValue1 == LOW) {
    Serial.print("TURBID ");
  } else {
    Serial.print("CLEAR ");
  }
}

void turbidity2_Print() {
  sensorValue2 = digitalRead(TURBIDITY2_PIN);
  //  Serial.print(sensorV/alue2);
  //  Serial.print(" ");/
  if (sensorValue2 == LOW) {
    Serial.print("TURBID ");
  } else {
    Serial.print("CLEAR ");
  }
}

int moisture_Read() {
  moistureValue = analogRead(MOISTURE_PIN);
  moistureValue = map(moistureValue, 531, 263, 0, 100);
  return moistureValue;
}

void moisture_Print() {
  moisture_Read();
  if (moistureValue < 0) {
    Serial.print("0% ");
  } else {
    Serial.print(moistureValue);
    Serial.print("% ");
  }
}

void volume1_Print() {
  distance1_Read();
  double waterLevel1 = ((max_distance1 - distance1) / (max_distance1 - 11.00)) * 100.0;
  if (waterLevel1 < 0) {
    Serial.print("0.00% ");
  } else {
    Serial.print(waterLevel1);
    Serial.print("% ");
  }
}

void volume2_Print() {
  distance2_Read();
  double waterLevel2 = ((max_distance2 - distance2) / max_distance2) * 100.0;
  if (waterLevel2 < 0) {
    Serial.print("0.00% ");
  } else {
    Serial.print(waterLevel2);
    Serial.print("% ");
  }
}

float temp_Read() {
  //returns the temperature from one DS18S20 in DEG Celsius

  byte data[12];
  byte addr[8];

  if ( !ds.search(addr)) {
    //no more sensors on chain, reset search
    ds.reset_search();
    return -1000;
  }

  if ( OneWire::crc8( addr, 7) != addr[7]) {
    //Serial.print("CRC is not valid!");
    return -1000;
  }

  if ( addr[0] != 0x10 && addr[0] != 0x28) {
    //Serial.print("Device is not recognized");
    return -1000;
  }

  ds.reset();
  ds.select(addr);
  ds.write(0x44, 1); // start conversion, with parasite power on at the end

  byte present = ds.reset();
  ds.select(addr);
  ds.write(0xBE); // Read Scratchpad


  for (int i = 0; i < 9; i++) { // we need 9 bytes
    data[i] = ds.read();
  }

  ds.reset_search();

  byte MSB = data[1];
  byte LSB = data[0];

  float tempRead = ((MSB << 8) | LSB); //using two's compliment
  temperature = tempRead / 16;

  return temperature;

}

void temp_Print() {
  temp_Read();
  Serial.print(temperature);
  Serial.print("°C ");
}

//For pH Sensor
float averagearray(int* arr, int number) {
  int i;
  int max, min;
  double avg;
  long amount = 0;
  if (number <= 0) {
    return 0;
  }
  if (number < 5) { //less than 5, calculated directly statistics
    for (i = 0; i < number; i++) {
      amount += arr[i];
    }
    avg = amount / number;
    return avg;
  } else {
    if (arr[0] < arr[1]) {
      min = arr[0]; max = arr[1];
    }
    else {
      min = arr[1]; max = arr[0];
    }
    for (i = 2; i < number; i++) {
      if (arr[i] < min) {
        amount += min;      //arr<min
        min = arr[i];
      } else {
        if (arr[i] > max) {
          amount += max;  //arr>max
          max = arr[i];
        } else {
          amount += arr[i]; //min<=arr<=max
        }
      }//if
    }//for
    avg = (double)amount / (number - 2);
  }//if
  return avg;
}

float averagearray1(int* arr, int number) {
  int i;
  int max, min;
  double avg;
  long amount = 0;
  if (number <= 0) {
    return 0;
  }
  if (number < 5) { //less than 5, calculated directly statistics
    for (i = 0; i < number; i++) {
      amount += arr[i];
    }
    avg = amount / number;
    return avg;
  } else {
    if (arr[0] < arr[1]) {
      min = arr[0]; max = arr[1];
    }
    else {
      min = arr[1]; max = arr[0];
    }
    for (i = 2; i < number; i++) {
      if (arr[i] < min) {
        amount += min;      //arr<min
        min = arr[i];
      } else {
        if (arr[i] > max) {
          amount += max;  //arr>max
          max = arr[i];
        } else {
          amount += arr[i]; //min<=arr<=max
        }
      }//if
    }//for
    avg = (double)amount / (number - 2);
  }//if
  return avg;
}
