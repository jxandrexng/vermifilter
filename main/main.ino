#include <NewPing.h> //Ultrasonic Sensor Library
#include <Servo.h>
#include <OneWire.h>

// CONSTANTS
#define TRIGGER1_PIN    12  // Arduino pin tied to trigger pin on the first ultrasonic sensor.
#define ECHO1_PIN       11  // Arduino pin tied to echo pin on the first ultrasonic sensor.
#define TRIGGER2_PIN    10  // Arduino pin tied to trigger pin on the second ultrasonic sensor.
#define ECHO2_PIN        9  // Arduino pin tied to echo pin on the second ultrasonic sensor.
#define TEMP_PIN         8  // Arduino pin tied to temperature sensor.
#define RELAY1           13  // Arduino pin tied to relay1 pin of the influent pump.
#define RELAY2           4  // Arduino pin tied to relay2 pin of the washer1 pump.
#define RELAY3           5  // Arduino pin tied to relay3 pin of the washer2 pump.
#define RELAY4           6  // Arduino pin tied to relay4 pin of the vermibed pump.
#define RELAY5           7  // Arduino pin tied to relay5 pin of the soda ash pump.
#define LEVEL_PIN       22  // Arduino pin tied to level pin of the soda ash container.
#define TURBIDITY1_PIN  A0 // Arduino pin tied to turbidity1 sensor.
#define TURBIDITY2_PIN  A1 // Arduino pin tied to turbidity2 sensor.
#define PH_SENSOR1_PIN  A2 // Arduino pin tied to ph1 sensor.
#define PH_SENSOR2_PIN  A3 // Arduino pin tied to ph2 sensor.
#define MOISTURE_PIN    A4 // Arduino pin tied to soil moisture sensor.
#define TEMPERATURE_PIN A5 // Arduino pin tied to temperature sensor.
#define MAX_DISTANCE   500 // Maximum distance we want to ping for (in centimeters). Maximum sensor distance is rated at 400-500cm.
#define waterLimit      10 // Limit in cm to which the ultrasonic sensor is in proximity to the water.
#define containerHeight 30 // Height of the container in cm.
#define Offset1          0.10  //Deviation compensate for pH Sensor1.
#define Offset2          0.11  //Deviation compensate for pH Sensor2.
#define ArrayLength1     40 // Times of collection for pH values.
#define ArrayLength2     40 // Times of collection for pH values.


// DECLARATION
int sodaLevel; //Store the binary value for soda ash level
boolean initStatus = 0; //Store initialization status
int pHArray1[ArrayLength1];   //Store the average value of the sensor feedback
int pHArrayIndex1 = 0;
int pHArray2[ArrayLength2];   //Store the average value of the sensor feedback
int pHArrayIndex2 = 0;
int distance1, distance2, pos = 0;
float turbidityUnit1 = 0, turbidityUnit2 = 0;
int moistureValue = 0;
char incoming; //Incoming value for serial
unsigned long interval = 1000, previousMillis = 0;
float pHUnit1 = 0, pHUnit2 = 0, temperature = 0, pHvoltage1, pHvoltage2;
boolean relay1_Status = 0, relay2_Status = 0, relay3_Status = 0, relay4_Status = 0, relay5_Status = 0;
OneWire ds(TEMPERATURE_PIN);
Servo myservo1, myservo2;
NewPing sonar1(TRIGGER1_PIN, ECHO1_PIN, MAX_DISTANCE); // NewPing setup of pins and maximum distance. Ultrasonic Sensor NewPing1
NewPing sonar2(TRIGGER2_PIN, ECHO2_PIN, MAX_DISTANCE); // NewPing setup of pins and maximum distance. Ultrasonic Sensor NewPing2

// SETUP
void setup() {
  Serial.begin(9600); //Begin serial transmission at 9600 Baud rate
  initF();
}

// LOOP
void loop() {
  unsigned long currentMillis = millis();
  if ((unsigned long)(currentMillis - previousMillis) >= interval) {
    pH1_Print();
    turbidity1_Print();
    volume1_Print();
    pH2_Print();
    turbidity2_Print();
    volume2_Print();
    temp_Print();
    moisture_Print();
    soda_Print();
    Serial.print("\n"); 
    previousMillis = currentMillis;
  }
  
  if (Serial.available() > 0) {
    incoming = Serial.read(); //Read transmitted input from Raspberry Pi
    if(incoming == '1' && !initStatus){
      relay1_On(); //Pump water to influent container.
      relay2_On(); //Pump cleaning water to pH input sensor.
      relay3_On(); //Pump cleaning water to pH output sensor.
      relay4_Off(); //Standby for vermibed pump.
      relay5_Off(); //Standby for soda ash pump.
      mainF();
      initStatus = 1;
    }
    else if(incoming == '2' && initStatus){
      relay1_Off; 
      relay2_Off;
      relay3_Off;
      relay4_Off;
      relay5_Off;
      initStatus = 0;
    }
  }
}

void initF() {
  pinMode(RELAY1, OUTPUT); //Set relay1 as output.
  pinMode(RELAY2, OUTPUT); //Set relay2 as output.
  pinMode(RELAY3, OUTPUT); //Set relay3 as output.
  pinMode(RELAY4, OUTPUT); //Set relay4 as output.
  pinMode(RELAY5, OUTPUT); //Set relay5 as output.
  pinMode(LEVEL_PIN, INPUT); //Set level pin as input.
  myservo1.attach(44); //Attach servo1 to pin 44.
  myservo2.attach(46); //Attach servo2 to pin 46.
  initStatus = 0;
}

//void main_printF() {
//  unsigned long currentMillis = millis();
//  if ((unsigned long)(currentMillis - previousMillis) >= interval) {
//    pH1_Print();
//    turbidity1_Print();
//    volume1_Print();
//    pH2_Print();
//    turbidity2_Print();
//    volume2_Print();
//    temp_Print();
//    moisture_Print();
//    soda_Print();
//    Serial.print("\n"); 
//    previousMillis = currentMillis;
//  }
//}

void mainF() {
    pump_Effluent();
    pump_Vermibed();
    pump_Soda();
    pump_Influent();
    pump_Vermibed();
    pump_Vermibed();
}

void stop_Relays() {
  relay1_Off; 
  relay2_Off;
  relay3_Off;
  relay4_Off;
  relay5_Off;
}

//void init_Relays() {
//  relay1_On(); //Pump water to influent container.
//  relay2_On(); //Pump cleaning water to pH input sensor.
//  relay3_On(); //Pump cleaning water to pH output sensor.
//  relay4_Off(); //Standby for vermibed pump.
//  relay5_Off(); //Standby for soda ash pump.
//  initStatus = 1;
//}

int distance1_Read() {
  distance1 = sonar1.ping_cm();
  return distance1;
}

void distance1_Print() {
  Serial.print("Distance1: ");
  Serial.print(distance1); // Send ping, get distance in cm and print result (0 = outside set distance range)
  Serial.print(" ");
}

int distance2_Read() {
  distance2 = sonar2.ping_cm();
  return distance2;
}

void distance2_Print() {
  Serial.print("Distance2: ");
  Serial.print(distance2); // Send ping, get distance in cm and print result (0 = outside set distance range)
  Serial.print(" ");
}

float pH1_Read() {
    pHArray1[pHArrayIndex1++]=analogRead(PH_SENSOR1_PIN);
      if(pHArrayIndex1==ArrayLength1)pHArrayIndex1=0;
      pHvoltage1 = averagearray(pHArray1, ArrayLength1)*5.0/1024;
      pHUnit1 = 3.5*pHvoltage1+Offset1;
      return pHUnit1;
}

void pH1_Print() {
  pH1_Read();
  Serial.print(pHUnit1);
  Serial.print(" ");
}

float pH2_Read() {
    pHArray2[pHArrayIndex2++]=analogRead(PH_SENSOR2_PIN);
      if(pHArrayIndex2==ArrayLength2)pHArrayIndex2=0;
      pHvoltage2 = averagearray(pHArray2, ArrayLength2)*5.0/1024;
      pHUnit2 = 3.5*pHvoltage2+Offset2;
      return pHUnit2;
}

void pH2_Print() {
  pH2_Read();
  Serial.print(pHUnit2);
  Serial.print(" ");
}

float turbidity1_Read() {
  float sensorValue = analogRead(TURBIDITY1_PIN);
  float voltage = sensorValue * (5.0 / 1024.0);
  turbidityUnit1 = (-1120.4*voltage*voltage) + 5742.3*voltage -4352.9;
  return turbidityUnit1;
}

void turbidity1_Print() {
  turbidity1_Read();
  Serial.print(turbidityUnit1);
  Serial.print(" ");
}

float turbidity2_Read() {
  float sensorValue = analogRead(TURBIDITY2_PIN);
  float voltage = sensorValue * (5.0 / 1024.0);
  turbidityUnit2 = (-1120.4*voltage*voltage) + 5742.3*voltage -4352.9;
  return turbidityUnit2;
}

void turbidity2_Print() {
  turbidity2_Read();
  Serial.print(turbidityUnit2);
  Serial.print(" ");
}

int moisture_Read() {
  moistureValue = analogRead(MOISTURE_PIN);
  moistureValue = map(moistureValue, 531, 263, 0, 100);
  return moistureValue;
}

void moisture_Print() {
  moisture_Read();
  Serial.print(moistureValue);
  Serial.print(" ");
}

void volume1_Print() {
  distance1_Read();
  float waterVolume1 = ((30.0 - distance1) * (30.0 * 40.0) / (30.0 * 30.0 * 40.0)) * 100.0;
  Serial.print(waterVolume1);
  Serial.print(" ");
}

void volume2_Print() {
  distance2_Read();
  float waterVolume2 = ((30.0 - distance2) * (30.0 * 40.0) / (30.0 * 30.0 * 40.0)) * 100.0;
  Serial.print(waterVolume2);
  Serial.print(" ");
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
  Serial.print(" ");
}

void relay1_On() {
  digitalWrite(RELAY1, HIGH);
}

void relay1_Off() {
  digitalWrite(RELAY1, LOW);
}

void relay2_On() {
  digitalWrite(RELAY2, HIGH);
}

void relay2_Off() {
  digitalWrite(RELAY2, LOW);
}

void relay3_On() {
  digitalWrite(RELAY3, HIGH);
}

void relay3_Off() {
  digitalWrite(RELAY3, LOW);
}

void relay4_On() {
  digitalWrite(RELAY4, HIGH);
}

void relay4_Off() {
  digitalWrite(RELAY4, LOW);
}

void relay5_On() {
  digitalWrite(RELAY5, HIGH);
}

void relay5_Off() {
  digitalWrite(RELAY5, LOW);
}

void servo1_Expand() {
  myservo1.write(90);
}

void servo1_Retract() {
  myservo1.write(0);
}

void servo2_Expand() {
  myservo2.write(90);
}

void servo2_Retract() {
  myservo2.write(0);
}

void soda_Print() {
  sodaLevel = digitalRead(LEVEL_PIN);
  if(sodaLevel == 1) {
  Serial.print("OKAY");
  } else {
    Serial.print("LOW");
  }
  
}

void pump_Soda() {
  sodaLevel = digitalRead(LEVEL_PIN);
  if (sodaLevel = HIGH) {
    relay5_On();
  } else {
    relay5_Off();
  }
}

void pump_Influent() {
  distance1_Read();
  if (distance1 <= waterLimit) { //If influent water level is nearly full, execute the following functions:
    relay1_Off(); //Turn off influent pump.
    relay2_Off(); //Turn off washer pump.
    servo1_Expand(); //Rotate pH sensor towards untreated water.
  }
  else if (distance1 >= waterLimit && distance1 <= containerHeight) { //If influent water is almost empty, execute the following:
    servo1_Retract(); //Rotate pH sensor towards cleaning water.
    relay2_On(); //Turn on washer pump.
    relay1_On(); //Turn on influent pump.
  }
}

void pump_Vermibed() {
  distance1_Read();
  //Do logic that pumps water to vermibed while influent container is not empty without disrupting other functions.
  unsigned long currentMillis = millis();
  if(distance1 == containerHeight){
    if(currentMillis - previousMillis >= interval && !relay4_Status){
      relay4_On(); //Turn on vermibed pump.
      previousMillis = currentMillis;
      relay4_Status = 1;    
    }
    else if(currentMillis - previousMillis >= interval && relay4_Status){
      relay4_Off();
      previousMillis = currentMillis;
      relay4_Status = 0;
    }
  }
  //Add timer interval that reads soil moisture.
  if (distance1 == containerHeight) {
    relay4_Off();
  }
}

void pump_Effluent() {
  distance2_Read();
  if (distance2 <= waterLimit) { //If effluent water level is nearly full, execute the following:
    relay3_Off(); //Turn off washer pump.
    servo2_Expand(); //Rotate pH sensor towards treated water.
  }
  else if (distance2 >= waterLimit && distance2 <= containerHeight) { //If water level is almost empty, execute the following.
    relay3_On(); //Turn on washer pump.
    servo2_Retract(); //Rotate pH sensor towards cleaning water.
  }
}

void dilute() {
  pH1_Read();
  if (pHUnit1 < 6.00) {
    relay5_On();
  } else {
    relay5_Off();
  }
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
