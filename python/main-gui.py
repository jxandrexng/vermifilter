import Tkinter
import tkFont
import serial

root = Tkinter.Tk()

ser = serial.Serial('/dev/ttyACM0', 9600)

helv36 = tkFont.Font(family='Helvetica', size=36, weight='bold')

while 1:
    values = ser.readline()
    hello = values.split(" ")[0]
    ph_value = values.split(" ")[1]
    turbidity_value = values.split(" ")[2]
    #print "Distance in cm:", hello
    #print "pH Value:", ph_value
    #print "Turbidity in NTU:", turbidity_value

Tkinter.Label(root, text='pH Level:', borderwidth=1, font=helv36).grid(row=1,column=1)
Tkinter.Label(root, text='Turbidity:', borderwidth=1, font=helv36).grid(row=2,column=1)
Tkinter.Label(root, text='%s'%(ph_value), borderwidth=1, font=helv36).grid(row=1,column=2)
Tkinter.Label(root, text='%s'%(turbidity_value), borderwidth=1, font=helv36).grid(row=2,column=2)

Tkinter.Label(root, text='pH Level:', borderwidth=1, font=helv36).grid(row=3,column=1)
Tkinter.Label(root, text='Turbidity:', borderwidth=1, font=helv36).grid(row=4,column=1)
Tkinter.Label(root, text='%s'%(ph_value), borderwidth=1, font=helv36).grid(row=3,column=2)
Tkinter.Label(root, text='%s'%(turbidity_value), borderwidth=1, font=helv36).grid(row=4,column=2)

ser.close()

root.mainloop()
