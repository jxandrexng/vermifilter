import serial
ser = serial.Serial('/dev/ttyACM0', 9600)

while 1:
    line = ser.readline()
    values = line.decode().split(" ")
    ph1, ph2,
    turb1, turb2,
    vol1, vol2,
    temp, soil = [float(s) for s in values]

    print (ph1)
    print (ph2)
    print (turb1)
    print (turb2)
    print (vol1)
    print (vol2)
    print (temp)
    print (soil)

ser.close()
