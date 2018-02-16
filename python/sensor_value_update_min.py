import time
import serial
from Tkinter import *

serial_speed = 9600
serial_port = '/dev/ttyACM0'

ser = serial.Serial(serial_port, serial_speed, timeout=1)

class Application(Frame):

    def measure(self):

        data = ser.readline()

        if (data != " "):
            try:
                processed_data = data.split(" ")

                self.ph_input_data.set("pH Input: " + str(processed_data[0]))
                self.ph_input.pack()

                self.turb_input_data.set("Turbidity Input: " + str(processed_data[1]))
                self.turb_input.pack()

                self.vol_input_data.set("Volume Input: " + str(processed_data[2]))
                self.vol_input.pack()
            except IndexError:
                pass

        self.after(1000, self.measure)

    def createWidgets(self):
        self.ph_input = Label(self, textvariable=self.ph_input_data, font=('Verdana', 20, 'bold'))
        #self.ph_input_data.set("pH Input")
        self.ph_input.pack()

        self.turb_input = Label(self, textvariable=self.turb_input_data, font=('Verdana', 20, 'bold'))
        #self.turb_input_data.set("Turbidity Input")
        self.turb_input.pack()

        self.vol_input = Label(self, textvariable=self.vol_input_data, font=('Verdana', 20, 'bold'))
        #self.vol_input_data.set("Volume Input")
        self.turb_input.pack()

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.ph_input_data = StringVar()
        self.turb_input_data = StringVar()
        self.vol_input_data = StringVar()
        self.createWidgets()
        self.pack()
        self.measure()

root = Tk()
app = Application(master=root)
app.mainloop()
