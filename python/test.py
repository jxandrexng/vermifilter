import serial
ser = serial.Serial('/dev/ttyACM1', 9600)

while 1:
    ser.read(10)
    ser.write('c')
