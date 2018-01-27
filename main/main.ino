#include <EEPROM.h>
#include <NewPing.h> //Ultrasonic Sensor Library
#include <AnalogPHMeter.h>
#include <Servo.h> 

// CONSTANTS
#define TRIGGER_PIN  12  // Arduino pin tied to trigger pin on the ultrasonic sensor.
#define ECHO_PIN     11  // Arduino pin tied to echo pin on the ultrasonic sensor.
#define RELAY1       3  // Arduino pin tied to relay1 pin of the first pump.
#define RELAY2       4  // Arduino pin tied to relay2 pin of the second pump.
#define TURBIDITY1_PIN A0 // Arduino pin tied to turbidity1 sensor.
#define TURBIDITY2_PIN A1 // Arduino pin tied to turbidity2 sensor.
#define PH_SENSOR1_PIN A2 // Arduino pin tied to ph1 sensor.
#define PH_SENSOR2_PIN A3 // Arduino pin tied to ph2 sensor.
#define MAX_DISTANCE 500 // Maximum distance we want to ping for (in centimeters). Maximum sensor distance is rated at 400-500cm.


// DECLARATION
AnalogPHMeter pHSensor1(PH_SENSOR1_PIN);
AnalogPHMeter pHSensor2(PH_SENSOR2_PIN);
unsigned int pHCalibrationValueAddress = 0;
int turbidityUnit1 = 0, turbidityUnit2 = 0;
int distance1, distance2, pos;
Servo myservo1, myservo2, myservo3, myservo4;
NewPing sonar(TRIGGER_PIN, ECHO_PIN, MAX_DISTANCE); // NewPing setup of pins and maximum distance. Ultrasonic Sensor NewPing

// SETUP
void setup() {
  struct PHCalibrationValue pHCalibrationValue;
  Serial.begin(9600); // Open serial monitor at 9600 baud to see ping results
  EEPROM.get(pHCalibrationValueAddress, pHCalibrationValue);
  pHSensor1.initialize(pHCalibrationValue);
  pHSensor2.initialize(pHCalibrationValue);
  pinMode(RELAY1, OUTPUT);
  myservo1.attach(9);
  myservo2.attach(8);
  myservo3.attach(7);
  myservo4.attach(6);
}

// LOOP
void loop() {
  distance1_Print();
  pH1_Read();
  pH1_Print();
  turbidity1_Read();
  turbidity1_Print();
  Serial.print("\n");
  relay1_On();
}

int distance1_Read(){
   distance1 = 5;
   //distance = sonar.ping_cm();
   return distance1;
}

void distance1_Print() {
  delay(1000);                   // Wait 50ms between pings (about 20 pings/sec). 29ms should be the shortest delay between pings.
  Serial.print(distance1); // Send ping, get distance in cm and print result (0 = outside set distance range)
  Serial.print(" ");
}

int distance2_Read(){
   distance2 = 5;
   //distance = sonar.ping_cm();
   return distance2;
}

void distance2_Print() {
  delay(1000);                   // Wait 50ms between pings (about 20 pings/sec). 29ms should be the shortest delay between pings.
  Serial.print(distance2); // Send ping, get distance in cm and print result (0 = outside set distance range)
  Serial.print(" ");
}

void pH1_Read() {
  pHSensor1.calibrationClear();
  EEPROM.put(pHCalibrationValueAddress, pHSensor1.getCalibrationValue());
}

void pH1_Print(){
  Serial.print(pHSensor1.singleReading().getpH());
  Serial.print(" ");
}

void pH2_Read() {
  pHSensor2.calibrationClear();
  EEPROM.put(pHCalibrationValueAddress, pHSensor2.getCalibrationValue());
}

void pH2_Print(){
  Serial.print(pHSensor2.singleReading().getpH());
  Serial.print(" ");
}

void turbidity1_Read() {
  int sensorValue = analogRead(TURBIDITY1_PIN);
  float voltage = sensorValue * (5.0 / 1024.0);
  turbidityUnit1 = sensorValue;
}

void turbidity1_Print(){
    Serial.print(turbidityUnit1);
}

void turbidity2_Read() {
  int sensorValue = analogRead(TURBIDITY2_PIN);
  float voltage = sensorValue * (5.0 / 1024.0);
  turbidityUnit2 = sensorValue;
}

void turbidity2_Print(){
    Serial.print(turbidityUnit2);
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

/*void Servo1_Expand(){
    for(pos=0;pos<90;pos+=1){
    myservo1.write(pos);
    delay(5);
    }
    delay(5000);
}

void Servo1_Retract(){
    for(pos=90;pos>=1;pos-=1){
    myservo1.write(pos);
    delay(5);
    }
    delay(5000);
}

void Servo2_Expand(){
    for(pos=0;pos<90;pos+=1){
    myservo2.write(pos);
    delay(5);
    }
    delay(5000);
}

void Servo2_Retract(){
    for(pos=90;pos>=1;pos-=1){
    myservo2.write(pos);
    delay(5);
    }
    delay(5000);
}

void Servo3_Expand(){
    for(pos=0;pos<90;pos+=1){
    myservo3.write(pos);
    delay(5);
    }
    delay(5000);
}

void Servo3_Retract(){
    for(pos=90;pos>=1;pos-=1){
    myservo3.write(pos);
    delay(5);
    }
    delay(5000);
}

void Servo4_Expand(){
    for(pos=0;pos<90;pos+=1){
    myservo4.write(pos);
    delay(5);
    }
    delay(5000);
}

void Servo4_Retract(){
    for(pos=90;pos>=1;pos-=1){
    myservo4.write(pos);
    delay(5);
    }
    delay(5000);
}

void main(){
  if(distance < 10){
    Relay1_On();
    Servo1_Expand();
  }
  else
  {
    Relay1_Off();
    Servo1_Retract();
  }
}*/

