#include <EEPROM.h>
#include <NewPing.h> //Ultrasonic Sensor Library
#include <AnalogPHMeter.h>
#include <Servo.h> 

// CONSTANTS
#define TRIGGER1_PIN  12  // Arduino pin tied to trigger pin on the first ultrasonic sensor.
#define ECHO1_PIN     11  // Arduino pin tied to echo pin on the first ultrasonic sensor.
#define TRIGGER2_PIN  10  // Arduino pin tied to trigger pin on the second ultrasonic sensor.
#define ECHO2_PIN     9  // Arduino pin tied to echo pin on the second ultrasonic sensor.
#define RELAY1       3  // Arduino pin tied to relay1 pin of the first pump.
#define RELAY2       4  // Arduino pin tied to relay2 pin of the second pump.
#define RELAY3       5  // Arduino pin tied to relay3 pin of the first pump.
#define RELAY4       6  // Arduino pin tied to relay4 pin of the second pump.
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
int distance1, distance2, pos = 0;
Servo myservo1, myservo2, myservo3, myservo4;
NewPing sonar1(TRIGGER1_PIN, ECHO1_PIN, MAX_DISTANCE); // NewPing setup of pins and maximum distance. Ultrasonic Sensor NewPing
NewPing sonar2(TRIGGER2_PIN, ECHO2_PIN, MAX_DISTANCE);

// SETUP
void setup() {
  struct PHCalibrationValue pHCalibrationValue;
  Serial.begin(9600); // Open serial monitor at 9600 baud to see ping results
  EEPROM.get(pHCalibrationValueAddress, pHCalibrationValue);
  pHSensor1.initialize(pHCalibrationValue);
  pHSensor2.initialize(pHCalibrationValue);
  pinMode(RELAY1, OUTPUT);
  pinMode(RELAY2, OUTPUT);
  pinMode(RELAY3, OUTPUT);
  pinMode(RELAY4, OUTPUT);
  pinMode(22, OUTPUT);
  digitalWrite(22, HIGH); 
  pinMode(24, OUTPUT);
  digitalWrite(24, HIGH);  
  myservo1.attach(44);
//  myservo2.attach(45);
//  myservo3.attach(46);
//  myservo4.attach(47);
}

// LOOP
void loop() {
  pH1_Read();
  pH1_Print();
  turbidity1_Read();
  turbidity1_Print();
  distance1_Read();
  distance1_Print();
  Serial.print(" | ");
  pH2_Read();
  pH2_Print();
  turbidity2_Read();
  turbidity2_Print();
  distance2_Read();
  distance2_Print();
  Serial.print("\n");
  relay1_On();
  relay2_On();
  servo1_Expand();
  servo1_Retract();
}

int distance1_Read(){
   distance1 = sonar1.ping_cm();
   return distance1;
}

void distance1_Print() {
  Serial.print(distance1); // Send ping, get distance in cm and print result (0 = outside set distance range)
  Serial.print(" ");
}

int distance2_Read(){
   distance2 = sonar2.ping_cm();
   return distance2;
}

void distance2_Print() {
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
    Serial.print(" ");
}

void turbidity2_Read() {
  int sensorValue = analogRead(TURBIDITY2_PIN);
  float voltage = sensorValue * (5.0 / 1024.0);
  turbidityUnit2 = sensorValue;
}

void turbidity2_Print(){
    Serial.print(turbidityUnit2);
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

void servo1_Expand(){
    for(pos=0;pos<=90;pos+=1){
    myservo1.write(pos);
    delay(15);
    }
    delay(5000);
}

void servo1_Retract(){
    for(pos=90;pos>=1;pos-=1){
    myservo1.write(pos);
    delay(15);
    }
    delay(5000);
}

void servo2_Expand(){
    for(pos=0;pos<=90;pos+=1){
    myservo2.write(pos);
    delay(5);
    }
    delay(5000);
}

void servo2_Retract(){
    for(pos=90;pos>=1;pos-=1){
    myservo2.write(pos);
    delay(5);
    }
    delay(5000);
}

void servo3_Expand(){
    for(pos=0;pos<=90;pos+=1){
    myservo3.write(pos);
    delay(5);
    }
    delay(5000);
}

void servo3_Retract(){
    for(pos=90;pos>=1;pos-=1){
    myservo3.write(pos);
    delay(5);
    }
    delay(5000);
}

void servo4_Expand(){
    for(pos=0;pos<=90;pos+=1){
    myservo4.write(pos);
    delay(5);
    }
    delay(5000);
}

void servo4_Retract(){
    for(pos=90;pos>=1;pos-=1){
    myservo4.write(pos);
    delay(5);
    }
    delay(5000);
}

/*void main(){
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

