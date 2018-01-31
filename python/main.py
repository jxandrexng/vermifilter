import serial

ser = serial.Serial('/dev/ttyACM0', 9600)

while 1:
    values = ser.readline().decode()
    hello = values.split(" ")[0]
    ph_value = values.split(" ")[1]
    turbidity_value = values.split(" ")[2]
    print ("Distance in cm:", hello)
    print ("pH Value:", ph_value)
    print ("Turbidity in NTU:", turbidity_value)
ser.close()
