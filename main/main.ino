#include <EEPROM.h>
#include <NewPing.h> //Ultrasonic Sensor Library
#include <AnalogPHMeter.h>
#include <Servo.h> 

// CONSTANTS
#define TRIGGER_PIN  12  // Arduino pin tied to trigger pin on the ultrasonic sensor.
#define ECHO_PIN     11  // Arduino pin tied to echo pin on the ultrasonic sensor.
#define RELAY1       3  // Arduino pin tied to relay1 pin of the pump.
#define TURBIDITY_PIN A0 // Arduino pin tied to turbidity sensor.
#define PH_SENSOR1_PIN A1 // Arduino pin tied to ph sensor.
#define MAX_DISTANCE 500 // Maximum distance we want to ping for (in centimeters). Maximum sensor distance is rated at 400-500cm.


// DECLARATION
AnalogPHMeter pHSensor(PH_SENSOR1_PIN);
unsigned int pHCalibrationValueAddress = 0;
int turbidityUnit1 = 0;
int distance;
int pos;
Servo myservo;
NewPing sonar(TRIGGER_PIN, ECHO_PIN, MAX_DISTANCE); // NewPing setup of pins and maximum distance. Ultrasonic Sensor NewPing

// SETUP
void setup() {
  struct PHCalibrationValue pHCalibrationValue;
  Serial.begin(9600); // Open serial monitor at 9600 baud to see ping results
  EEPROM.get(pHCalibrationValueAddress, pHCalibrationValue);
  pHSensor.initialize(pHCalibrationValue);
  pinMode(RELAY1, OUTPUT);
  myservo.attach(9);
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

void distance1_Print() {
  delay(1000);                   // Wait 50ms between pings (about 20 pings/sec). 29ms should be the shortest delay between pings.
  distance = sonar.ping_cm();
  Serial.print(distance); // Send ping, get distance in cm and print result (0 = outside set distance range)
  Serial.print(" ");
}

void pH1_Read() {
  pHSensor.calibrationClear();
  EEPROM.put(pHCalibrationValueAddress, pHSensor.getCalibrationValue());
}

void pH1_Print(){
  Serial.print(pHSensor.singleReading().getpH());
  Serial.print(" ");
}

void turbidity1_Read() {
  int sensorValue = analogRead(TURBIDITY_PIN);
  float voltage = sensorValue * (5.0 / 1024.0);
  turbidityUnit1 = sensorValue;
}

void turbidity1_Print(){
    Serial.print(turbidityUnit1);
}

void relay1_On() {
  digitalWrite(RELAY1, HIGH);
}

void relay1_Off() {
  digitalWrite(RELAY1, LOW);
}

void Servo1_Expand(){
    for(pos=0;pos<90;pos+=1){
    myservo.write(pos);
    delay(5);
    }
    delay(5000);
}

void Servo1_Retract(){
    for(pos=90;pos>=1;pos-=1){
    myservo.write(pos);
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

