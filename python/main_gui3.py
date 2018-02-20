from tkinter import *
from tkinter import font
from tkinter import ttk
import serial
import time
import Tkinter as tk

class Vermifilter(object):

    def measure(self):
        data = ser.readline()

        if (data != " "):
            try:
                processed_data = data.split(" ")

                self.input_ph_data.set(str(processed_data[0]))
                self.input_ph_value.grid(row=6, column=2, sticky=W)

                self.input_turb_data.set(str(processed_data[1]))
                self.input_turb_value.grid(row=7, column=2, sticky=W)
                
                self.input_volume_data.set(str(processed_data[2]))
                self.input_volume_value.grid(row=8, column=2, sticky=W)

                
                self.output_ph_data.set(str(processed_data[3]))
                self.output_ph_value.grid(row=6, column=4, sticky=W)
                
                self.output_turb_data.set(str(processed_data[4]))
                self.output_turb_value.grid(row=7, column=4, sticky=W)
                
                self.output_volume_data.set(str(processed_data[5]))
                self.output_volume_value.grid(row=8, column=4, sticky=W)
                
                self.temperature_data.set(str(processed_data[6]))
                self.temperature_value.grid(row=9, column=2, sticky=W)
                
                self.soil_moisture_data.set(str(processed_data[7]))
                self.soil_moisture_value.grid(row=10, column=2, sticky=W)

            except IndexError:
                pass

    
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
        self.output_ph_value = Entry(self.right_frame, textvariable=input_ph_data, font=self.helv18, width=4)

        self.output_turb = Label(self.right_frame, text="Turbidity Level:", font=self.helv18)
        self.output_turb_value = Entry(self.right_frame, textvariable=input_turb_data, font=self.helv18, width=4)

        self.output_volume = Label(self.right_frame, text="Volume:", font=self.helv18)
        self.output_volume_value = Entry(self.right_frame, font=self.helv18, width=4)


        #Other Label-Values (Temperature and Soil Moisture)
        self.temperature = Label(self.bot_frame, text="Temperature:", font=self.helv12)
        self.temperature_value = Entry(self.bot_frame, font=self.helv12, width=4)

        self.soil_moisture = Label(self.bot_frame, text="Soil Moisture:", font=self.helv12)
        self.soil_moisture_value = Entry(self.bot_frame, font=self.helv12, width=4)

        self.header_title.grid(row=0, pady=1)

        self.untreated_label.grid(row=1, column=1, columnspan=2, pady=10)
        self.treated_label.grid(row=1, column=3, columnspan=2, pady=10)

        self.untreated_ph.grid(row=2, column=1, sticky=E, padx=10)
        self.untreated_ph_value.grid(row=2, column=2, sticky=W)
        self.untreated_turb.grid(row=3, column=1, sticky=E, padx=10)
        self.untreated_turb_value.grid(row=3, column=2, sticky=W)
        self.untreated_volume.grid(row=4, column=1, sticky=E, padx=10)
        self.untreated_volume_value.grid(row=4, column=2, sticky=W)

        self.treated_ph.grid(row=2, column=3, sticky=E, padx=10)
        self.treated_ph_value.grid(row=2, column=4, sticky=W)
        self.treated_turb.grid(row=3, column=3, sticky=E, padx=10)
        self.treated_turb_value.grid(row=3, column=4, sticky=W)
        self.treated_volume.grid(row=4, column=3, sticky=E, padx=10)
        self.treated_volume_value.grid(row=4, column=4, sticky=W)

        self.input_container_label.grid(row=5, column=1, columnspan=2, pady=10)
        self.output_container_label.grid(row=5, column=3, columnspan=2, pady=10)

        self.input_ph.grid(row=6, column=1, sticky=E, padx=10)
        self.input_ph_value.grid(row=6, column=2, sticky=W)
        self.input_turb.grid(row=7, column=1, sticky=E, padx=10)
        self.input_turb_value.grid(row=7, column=2, sticky=W)
        self.input_volume.grid(row=8, column=1, sticky=E, padx=10)
        self.input_volume_value.grid(row=8, column=2, sticky=W)

        self.output_ph.grid(row=6, column=3, sticky=E, padx=10)
        self.output_ph_value.grid(row=6, column=4, sticky=W)
        self.output_turb.grid(row=7, column=3, sticky=E, padx=10)
        self.output_turb_value.grid(row=7, column=4, sticky=W)
        self.output_volume.grid(row=8, column=3, sticky=E, padx=10)
        self.output_volume_value.grid(row=8, column=4, sticky=W)

        self.temperature.grid(row=9, column=1, sticky=E)
        self.temperature_value.grid(row=9, column=2, sticky=W)

        self.soil_moisture.grid(row=10, column=1, sticky=E)
        self.soil_moisture_value.grid(row=10, column=2, sticky=W)

        

    def run(self):
        self.top_frame.pack(side=TOP, ipady=10)
        self.left_frame.pack(side=LEFT, ipady=120)
        self.right_frame.pack(side=RIGHT, ipady=120)
        self.bot_frame.pack(side=BOTTOM, ipady=50)
        self.measure()
        self.root.mainloop()
        


if __name__ == "__main__":
    Vermifilter().run()
