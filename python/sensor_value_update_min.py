import time
import serial
from Tkinter import *

#connection of serial port to arduino
serial_speed = 9600
serial_port = '/dev/ttyACM0'

ser = serial.Serial(serial_port, serial_speed, timeout=1)

#font
HELV36 = ("Helvetica", 36, "bold")
HELV18 = ("Helvetica", 18, "bold")
HELV12 = ("Helvetica", 12, "bold")

class Application(Frame):
    def __init__(self, master=None):
            Frame.__init__(self, master)
            #frame format
            self.master = master
            master.title("Automated Vermifiltration System")
            master.resizable(width=False, height=False)
            master.geometry('{}x{}'.format(790, 480))

            self.header_frame_label_name = StringVar()
            self.ph_input_label_name = StringVar()
            self.ph_input_data = StringVar()
            self.turb_input_label_name = StringVar()
            self.turb_input_data = StringVar()
            self.vol_input_label_name = StringVar()
            self.vol_input_data = StringVar()
            self.vol_output_data = StringVar()
            self.createWidgets()
            self.pack()
            self.measure()
            
    #get the values from the arduino and split and store to the text variable
    def measure(self):

        data = ser.readline()

        if (data != " "):
            try:
                processed_data = data.split(" ")

                #header
                self.header_frame_label_name.set("Vermifilter UI")
                self.header_frame_label.grid(row=0, column=0, columnspan=5)
                
                #ph input
                self.ph_input_label_name.set("Ph Input: ")
                self.ph_input_label.grid(row=2, column=0)

                self.ph_input_data.set(str(processed_data[0]))
                self.ph_input.grid(row=2, column=1)

                #turbidity input
                self.turb_input_label_name.set("Turbidity Input: ")
                self.turb_input_label.grid(row=3, column=0)
                
                self.turb_input_data.set(str(processed_data[1]))
                self.turb_input.grid(row=3, column=1)

                #volume input
                self.vol_input_label_name.set("Volume Input: ")
                self.vol_input_label.grid(row=4, column=0)
                
                self.vol_input_data.set(str(processed_data[2]))
                self.vol_input.grid(row=4, column=1)

                self.vol_output_data.set("Volume Output: " + str(processed_data[3]))
                self.vol_output.grid(row=1, column=3)
            except IndexError:
                pass

        self.after(1000, self.measure)

    def createWidgets(self):
        #header
        self.header_frame_label = Label(self, textvariable=self.header_frame_label_name, font=HELV36)
        self.header_frame_label_name.set("Vermifilter UI")
        
        #ph Input
        self.ph_input_label = Label(self, textvariable=self.ph_input_label_name, font=HELV12)
        self.ph_input_label_name.set("ph Input")
        
        self.ph_input = Entry(self, textvariable=self.ph_input_data, width=4, font=HELV12)
        self.ph_input_data.set("pH Input")

        #turbidity input
        self.turb_input_label = Label(self, textvariable=self.turb_input_label_name, font=HELV12)
        self.turb_input_label_name.set("turbidity Input")
        
        self.turb_input = Entry(self, textvariable=self.turb_input_data, width=4, font=HELV12)
        self.turb_input_data.set("Turbidity Input")

        #volume input
        self.vol_input_label = Label(self, textvariable=self.vol_input_label_name, font=HELV12)
        self.vol_input_label_name.set("Volume Input")
        
        self.vol_input = Label(self, textvariable=self.vol_input_data, font=HELV12)
        self.vol_input_data.set("Volume Input")


        self.vol_output = Label(self, textvariable=self.vol_output_data, width=4, font=HELV12)
        self.vol_output_data.set("Volume Output")


    


root = Tk()
app = Application(master=root)
app.mainloop()
