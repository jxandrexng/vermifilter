from tkinter import *
from tkinter import font
from tkinter import ttk
import serial
import time
import threading
import tkinter

#s = serial.Serial('/dev/ttyACM1', 9600)

class gui(object):
    def __init__(self):
        self.root = Tk()

        self.helv36 = font.Font(family = "Helvetica", size = 36, weight = "bold")
        self.helv24 = font.Font(family = "Helvetica", size = 18, weight = "bold")
        self.helv18 = font.Font(family = "Helvetica", size = 12, weight = "normal")
        self.helv12 = font.Font(family = "Helvetica", size = 12, weight = "normal")

        self.root.title("Automated Vermifiltration System")
        self.root.resizable(width=False, height=False)
        self.root.geometry('{}x{}'.format(720, 480))

        self.top_frame = Frame(self.root)
        

        self.left_frame = Frame(self.root, bd=10)
        

        self.right_frame = Frame(self.root, bd=10)
        

        self.bot_frame = Frame(self.root, bd=10)
        

        #Title
        self.header_title = Label(self.top_frame, text="Vermifilter UI", font=self.helv36)

        #Labels-Values for Untreated water
        self.untreated_label = Label(self.left_frame, text="Untreated Water", font=self.helv24)

        self.untreated_ph = Label(self.left_frame, text="pH Level:", font=self.helv18)
        self.untreated_ph_value = Label(self.left_frame, font=self.helv18, width=4)

        self.untreated_turb = Label(self.left_frame, text="Turbidity Level:", font=self.helv18)
        self.untreated_turb_value = Label(self.left_frame, font=self.helv18, width=4)

        self.untreated_volume = Label(self.left_frame, text="Volume:", font=self.helv18)
        self.untreated_volume_value = Label(self.left_frame, font=self.helv18, width=4)

        self.untreated_soil = Label(self.left_frame, text="Soil Moisture:", font=self.helv18)
        self.untreated_soil_value = Label(self.left_frame, font=self.helv18, width=4)

        self.untreated_temperature = Label(self.left_frame, text="Temperature:", font=self.helv18)
        self.untreated_temperature_value = Label(self.left_frame, font=self.helv18, width=4)

        #Labels-Values for treated water
        self.treated_label = Label(self.right_frame, text="Treated Water", font=self.helv24)

        self.treated_ph = Label(self.right_frame, text="pH Level:", font=self.helv18)
        self.treated_ph_value = Label(self.right_frame, font=self.helv18, width=4)

        self.treated_turb = Label(self.right_frame, text="Turbidity Level:", font=self.helv18)
        self.treated_turb_value = Label(self.right_frame, font=self.helv18, width=4)

        self.treated_volume = Label(self.right_frame, text="Volume:", font=self.helv18)
        self.treated_volume_value = Label(self.right_frame, font=self.helv18, width=4)

        self.treated_soil = Label(self.right_frame, text="Soil Moisture:", font=self.helv18)
        self.treated_soil_value = Label(self.right_frame, font=self.helv18, width=4)

        self.treated_temperature = Label(self.right_frame, text="Temperature:", font=self.helv18)
        self.treated_temperature_value = Label(self.right_frame, font=self.helv18, width=4)


        #Labels-Values for Input Container
        self.input_container_label = Label(self.left_frame, text="Input Container", font=self.helv24)

        self.input_ph = Label(self.left_frame, text="pH Level:", font=self.helv18)
        self.input_ph_value = Entry(self.left_frame, font=self.helv18, width=4)

        self.input_turb = Label(self.left_frame, text="Turbidity Level:", font=self.helv18)
        self.input_turb_value = Entry(self.left_frame, font=self.helv18, width=4)

        self.input_volume = Label(self.left_frame, text="Volume:", font=self.helv18)
        self.input_volume_value = Entry(self.left_frame, font=self.helv18, width=4)


        #Labels-Values for Output Container
        self.output_container_label = Label(self.right_frame, text="Output Container", font=self.helv24)

        self.output_ph = Label(self.right_frame, text="pH Level:", font=self.helv18)
        self.output_ph_value = Entry(self.right_frame, font=self.helv18, width=4)

        self.output_turb = Label(self.right_frame, text="Turbidity Level:", font=self.helv18)
        self.output_turb_value = Entry(self.right_frame, font=self.helv18, width=4)

        self.output_volume = Label(self.right_frame, text="Volume:", font=self.helv18)
        self.output_volume_value = Entry(self.right_frame, font=self.helv18, width=4)


        #Other Label-Values (Temperature and Soil Moisture)
        self.temperature = Label(self.bot_frame, text="Temperature:", font=self.helv12)
        self.temperature_value = Entry(self.bot_frame, font=self.helv12, width=4)

        self.soil_moisture = Label(self.bot_frame, text="Soil Moisture:", font=self.helv12)
        self.soil_moisture_value = Entry(self.bot_frame, font=self.helv12, width=4)

    def run(self):
        self.top_frame.pack(side=TOP, ipady=10)
        self.left_frame.pack(side=LEFT, ipady=120)
        self.right_frame.pack(side=RIGHT, ipady=120)
        self.bot_frame.pack(side=BOTTOM, ipady=50)
        self.root.mainloop()


if __name__ == "__main__":
    gui().run()
