import serial

ser = serial.Serial('/dev/ttyACM1', 9600)

while 1 :
    print ser.readline()
ser.close()
