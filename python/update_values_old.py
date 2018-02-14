    arduino = serial.Serial('/dev/ttyACM1', 9600)
    arduino.readline().decode()
    
    while (1==1):
        values = []
        
        in_ph = values.append(arduino)
        in_turb = values.append(arduino)
        in_vol = values.append(arduino)
        out_ph = values.append(arduino)
        out_turb = values.append(arduino)
        out_vol = values.append(arduino)

        temp = values.append(arduino)
        soil_moisture = values.append(arduino)

        in_ph.decode('ascii')
        in_turb.decode('ascii')
        in_vol.decode('ascii')
        out_ph.decode('ascii')
        out_turb.decode('ascii')
        out_vol.decode('ascii')

        str(in_ph)
        str(in_turb)
        str(in_vol)
        str(out_ph)
        str(out_turb)
        str(out_vol)
        
    arduino.close()
