from pyfirmata import Arduino, util
from tkinter import font
from tkinter import *
from tkinter import ttk
import time, threading
import serial

root = Tk()

##board = Arduino('/dev/ttyACM0')
##it = util.Iterator(board)
##it.start()
##
##ph_a2 = board.get_pin('a:2:o')
##ph_a3 = board.get_pin('a:3:o')
##turb_a0 = board.get_pin('a:0:o')
##turb_a1 = board.get_pin('a:1:o')
##vol_d1 = board.get_pin('d:11:o')
##vol_d2 = board.get_pin('d:9:o')
##temp_a5 = board.get_pin('a:5:o')
##moist_a4 = board.get_pin('a:4:o')
##
##in_ph = StringVar(ph_a2.read())
##out_ph = StringVar(ph_a3.read())
##in_turb = StringVar(turb_a0.read())
##out_turb = StringVar(turb_a1.read())
##in_vol = StringVar(vol_d1.read())
##out_vol = StringVar(vol_d2.read())
##temperature = StringVar(temp_a5.read())
##soil_moisture = StringVar(moist_a4.read())
##
##print(ph_a2)

##ser = serial.Serial('/dev/ttyACM1', baudrate=9600, timeout=10,
##                    parity=serial.PARITY_NONE,
##                    stopbits=serial.STOPBITS_ONE,
##                    bytesize=serial.EIGHTBITS
##                    )

#def check_serial_event():
    

def update_clock():
    now = time.strftime("%H:%M:%S")
    timer.configure(text=now)
    root.after(1000, update_clock)

def autosave_30():
    save = Label(text="Save")
    #Wait 30 seconds
    #If 30 seconds, save the currennt value in the entry to the database

##Serial Monitor Output
def update_values():
##    global ser
##    ser = serial.Serial('/dev/ttyACM0', 9600)
##
##    line = ser.readline().strip()
##    values = line.decode('ascii').split(" ")
##    ph1, ph2,
##    turb1, turb2,
##    vol1, vol2,
##    temp, soil = [float(s) for s in values]
##        
##    ser.close()
    arduino = serial.Serial('/dev/ttyACM1', 9600)
 
    while 1:
        values = arduino.readline().decode()
        ph1 = values.split(" ")[0]
        ph2 = values.split(" ")[1]
        turb1 = values.split(" ")[2]
        turb2 = values.split(" ")[3]
        vol1 = values.split(" ")[4]
        vol2 = values.split(" ")[5]
        temp = values.split(" ")[6]
        soil_moist = values.split(" ")[7]
    arduino.close()

    
#Fonts
helv36 = font.Font(family = "Helvetica", size = 36, weight = "bold")
helv24 = font.Font(family = "Helvetica", size = 18, weight = "bold")
helv18 = font.Font(family = "Helvetica", size = 12, weight = "normal")
helv12 = font.Font(family = "Helvetica", size = 12, weight = "normal")

root.resizable(width=False, height=False)
root.geometry('{}x{}'.format(720, 480))

top_frame = Frame(root)
top_frame.pack(side=TOP, ipady=10)

left_frame = Frame(root, bd=10)
left_frame.pack(side=LEFT, ipady=120)

right_frame = Frame(root, bd=10)
right_frame.pack(side=RIGHT, ipady=120)

bot_frame = Frame(root, bd=10)
bot_frame.pack(side=BOTTOM, ipady=50)

#Title
header_title = Label(top_frame, text="Vermifilter UI", font=helv36)

#Labels-Values for Untreated water
untreated_label = Label(left_frame, text="Untreated Water", font=helv24)

untreated_ph = Label(left_frame, text="pH Level:", font=helv18)
untreated_ph_value = Label(left_frame, font=helv18, width=4)

untreated_turb = Label(left_frame, text="Turbidity Level:", font=helv18)
untreated_turb_value = Label(left_frame, font=helv18, width=4)

untreated_volume = Label(left_frame, text="Volume:", font=helv18)
untreated_volume_value = Label(left_frame, font=helv18, width=4)

untreated_soil = Label(left_frame, text="Soil Moisture:", font=helv18)
untreated_soil_value = Label(left_frame, font=helv18, width=4)

untreated_temperature = Label(left_frame, text="Temperature:", font=helv18)
untreated_temperature_value = Label(left_frame, font=helv18, width=4)

#Labels-Values for treated water
treated_label = Label(right_frame, text="Treated Water", font=helv24)

treated_ph = Label(right_frame, text="pH Level:", font=helv18)
treated_ph_value = Label(right_frame, font=helv18, width=4)

treated_turb = Label(right_frame, text="Turbidity Level:", font=helv18)
treated_turb_value = Label(right_frame, font=helv18, width=4)

treated_volume = Label(right_frame, text="Volume:", font=helv18)
treated_volume_value = Label(right_frame, font=helv18, width=4)

treated_soil = Label(right_frame, text="Soil Moisture:", font=helv18)
treated_soil_value = Label(right_frame, font=helv18, width=4)

treated_temperature = Label(right_frame, text="Temperature:", font=helv18)
treated_temperature_value = Label(right_frame, font=helv18, width=4)


#Labels-Values for Input Container
input_container_label = Label(left_frame, text="Input Container", font=helv24)

input_ph = Label(left_frame, text="pH Level:", font=helv18)
input_ph_value = Entry(left_frame, font=helv18, width=4)

input_turb = Label(left_frame, text="Turbidity Level:", font=helv18)
input_turb_value = Entry(left_frame, font=helv18, width=4)

input_volume = Label(left_frame, text="Volume:", font=helv18)
input_volume_value = Entry(left_frame, font=helv18, width=4)


#Labels-Values for Output Container
output_container_label = Label(right_frame, text="Output Container", font=helv24)

output_ph = Label(right_frame, text="pH Level:", font=helv18)
output_ph_value = Entry(right_frame, font=helv18, width=4)

output_turb = Label(right_frame, text="Turbidity Level:", font=helv18)
output_turb_value = Entry(right_frame, font=helv18, width=4)

output_volume = Label(right_frame, text="Volume:", font=helv18)
output_volume_value = Entry(right_frame, font=helv18, width=4)


#Other Label-Values (Temperature and Soil Moisture)
temperature = Label(bot_frame, text="Temperature:", font=helv12)
temperature_value = Entry(bot_frame, font=helv12, width=4)

soil_moisture = Label(bot_frame, text="Soil Moisture:", font=helv12)
soil_moisture_value = Entry(bot_frame, font=helv12, width=4)

#Button (text = 'Pump Again').grid (row = 11, column = 2)


#Timer
timer = Label(bot_frame, text="", font=helv12)


#Layout
header_title.grid(row=0, pady=1)

untreated_label.grid(row=1, column=1, columnspan=2, pady=10)
treated_label.grid(row=1, column=3, columnspan=2, pady=10)

untreated_ph.grid(row=2, column=1, sticky=E, padx=10)
untreated_ph_value.grid(row=2, column=2, sticky=W)
untreated_turb.grid(row=3, column=1, sticky=E, padx=10)
untreated_turb_value.grid(row=3, column=2, sticky=W)
untreated_volume.grid(row=4, column=1, sticky=E, padx=10)
untreated_volume_value.grid(row=4, column=2, sticky=W)

treated_ph.grid(row=2, column=3, sticky=E, padx=10)
treated_ph_value.grid(row=2, column=4, sticky=W)
treated_turb.grid(row=3, column=3, sticky=E, padx=10)
treated_turb_value.grid(row=3, column=4, sticky=W)
treated_volume.grid(row=4, column=3, sticky=E, padx=10)
treated_volume_value.grid(row=4, column=4, sticky=W)

input_container_label.grid(row=5, column=1, columnspan=2, pady=10)
output_container_label.grid(row=5, column=3, columnspan=2, pady=10)

input_ph.grid(row=6, column=1, sticky=E, padx=10)
input_ph_value.grid(row=6, column=2, sticky=W)
input_turb.grid(row=7, column=1, sticky=E, padx=10)
input_turb_value.grid(row=7, column=2, sticky=W)
input_volume.grid(row=8, column=1, sticky=E, padx=10)
input_volume_value.grid(row=8, column=2, sticky=W)

output_ph.grid(row=6, column=3, sticky=E, padx=10)
output_ph_value.grid(row=6, column=4, sticky=W)
output_turb.grid(row=7, column=3, sticky=E, padx=10)
output_turb_value.grid(row=7, column=4, sticky=W)
output_volume.grid(row=8, column=3, sticky=E, padx=10)
output_volume_value.grid(row=8, column=4, sticky=W)

temperature.grid(row=9, column=1, sticky=E)
temperature_value.grid(row=9, column=2, sticky=W)

soil_moisture.grid(row=10, column=1, sticky=E)
soil_moisture_value.grid(row=10, column=2, sticky=W)


timer.grid(row=13)


#root.after(1000, update_values)                         
root.mainloop()
