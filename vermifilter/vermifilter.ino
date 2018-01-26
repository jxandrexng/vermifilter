#include <EEPROM.h>
#include <NewPing.h> //Ultrasonic Sensor Library
#include <AnalogPHMeter.h>

// CONSTANTS
#define TRIGGER_PIN  12  // Arduino pin tied to trigger pin on the ultrasonic sensor.
#define ECHO_PIN     11  // Arduino pin tied to echo pin on the ultrasonic sensor.
#define RELAY1       22  // Arduino pin tied to relay1 pin of the pump.
#define MAX_DISTANCE 500 // Maximum distance we want to ping for (in centimeters). Maximum sensor distance is rated at 400-500cm.

// INITIALIZE
AnalogPHMeter pHSensor(A7);
unsigned int pHCalibrationValueAddress = 0;
int turbidityUnit1 = 0;
NewPing sonar(TRIGGER_PIN, ECHO_PIN, MAX_DISTANCE); // NewPing setup of pins and maximum distance. Ultrasonic Sensor NewPing

// SETUP
void setup() {
  struct PHCalibrationValue pHCalibrationValue;
  Serial.begin(9600); // Open serial monitor at 9600 baud to see ping results
  EEPROM.get(pHCalibrationValueAddress, pHCalibrationValue);
  pHSensor.initialize(pHCalibrationValue);
  //  pinMode(RELAY1, OUTPUT);
}

// LOOP
void loop() {
  distance1_Print();
  pH1_Read();
  pH1_Print();
  turbidity1_Read();
  turbidity1_Print();
  Serial.print("\n");
}

// ULTRASONIC SENSOR 1 PRINTING
void distance1_Print() {
  delay(1000);                   // Wait 50ms between pings (about 20 pings/sec). 29ms should be the shortest delay between pings.
  Serial.print(sonar.ping_cm()); // Send ping, get distance in cm and print result (0 = outside set distance range)
  Serial.print(" ");
}

// PH SENSOR 1 READING
void pH1_Read() {
  pHSensor.calibrationClear();
  EEPROM.put(pHCalibrationValueAddress, pHSensor.getCalibrationValue());
}

// PH SENSOR 1 PRINTING
void pH1_Print(){
  Serial.print(pHSensor.singleReading().getpH());
  Serial.print(" ");
}

// TURBIDITY SENSOR 1 READING
void turbidity1_Read() {
  int sensorValue = analogRead(A0);
  float voltage = sensorValue * (5.0 / 1024.0);
  turbidityUnit1 = sensorValue;
}

// TURBIDITY SENSOR 1 PRINTING
void turbidity1_Print(){
    Serial.print(turbidityUnit1);
}

// RELAY ON
void relay1_On() {
  digitalWrite(RELAY1, HIGH);
}

// RELAY OFF
void relay1_Off() {
  digitalWrite(RELAY1, LOW);
}
