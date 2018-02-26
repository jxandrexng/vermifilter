import time
import serial
from Tkinter import *

serial_speed = 9600
serial_port = '/dev/ttyACM0'

ser = serial.Serial(serial_port, serial_speed, timeout=1)

HELV36 = ("Helvetica", 36, "bold")
HELV24 = ("Helvetica", 18, "bold")
HELV18 = ("Helvetica", 12, "normal")
HELV12 = ("Helvetica", 12, "normal")

class Application(Frame):

    def measure(self):

        data = ser.readline()

        if (data != " "):
            try:
                processed_data = data.split(" ")

           ##     self.ph_input_data.set("pH Input: " + str(processed_data[0]))
##                self.ph_input.pack()
##
##                self.turb_input_data.set("Turbidity Input: " + str(processed_data[1]))
##                self.turb_input.pack()
##
##                self.vol_input_data.set("Volume Input: " + str(processed_data[2]))
##                self.vol_input.pack()

                self.ph_input_value.set(str(processed_data[0]))
                self.ph_input.grid(row=0, column=0, sticky=E)

                self.turb_input_value.set(str(processed_data[1]))
                self.turb_treated.grid(row=2, column=0, sticky=E)
                
                self.vol_input_value.set(str(processed_data[2]))
                self.vol_output_value.grid(row=2, column=1)

                self.ph_output_value.set(str(processed_data[3]))
                self.ph_output_value.grid(row=0, column=1)
                
                self.turb_output_value.set(str(processed_data[4]))
                self.turb_output_value.grid(row=1, column=1)

                self.vol_output_value.set(str(processed_data[5]))
                self.vol_input_value.grid(row=2, column=1)

                self.temperature_value.set(str(processed_data[6]))
                self.temperature_value.grid(row=0, column=1, sticky=E)

                self.soil_moisture_value.set(str(processed_data[7]))
                self.soil_moisture_value.grid(row=1, column=1, sticky=E)


            except IndexError:
                pass

        self.after(1000, self.measure)

    def createWidgets(self):
##        self.ph_input = Label(self, textvariable=self.ph_input_value, font=('Verdana', 20, 'bold'))
##        self.ph_input_value.set("pH Input")
##        self.ph_input.pack()
##
##        self.turb_input = Label(self, textvariable=self.turb_input_value, font=('Verdana', 20, 'bold'))
##        self.turb_input_value.set("Turbidity Input")
##        self.turb_input.pack()
##
##        self.vol_input = Label(self, textvariable=self.vol_input_value, font=('Verdana', 20, 'bold'))
##        self.vol_input_value.set("Volume Input")
##        self.vol_input.pack()
##
##        self.ph_output = Label(self, textvariable=self.ph_output_value, font=('Verdana', 20, 'bold'))
##        self.ph_output_value.set("pH Output")
##        self.ph_output.pack()
##
##        self.turb_output = Label(self, textvariable=self.turb_output_value, font=('Verdana', 20, 'bold'))
##        self.turb_output_value.set("Turbidity Output")
##        self.turb_output.pack()
##
##        self.vol_output = Label(self, textvariable=self.vol_output_value, font=('Verdana', 20, 'bold'))
##        self.vol_output_value.set("Volume Output")
##        self.vol_output.pack()
##
##        self.temperature = Label(self, textvariable=self.temperature_value, font=('Verdana', 20, 'bold'))
##        self.temperature_value.set("Temperature")
##        self.temperature.pack()
##
##        self.soil_moisture = Label(self, textvariable=self.soil_moisture_value, font=('Verdana', 20, 'bold'))
##        self.soil_moisture_value.set("Soil Moisture")
##        self.soil_moisture.pack()

        center_frame = Frame(self, width=720, height=480)
        center_frame.pack(fill="both", expand=True)
        center_frame.place(anchor="c", relx=.5, rely=.5)

        header_frame = Label(center_frame, text="VERMIFILTER UI", font=HELV36)
        header_frame.grid(row=0, column=0, columnspan=5)

        untreated_water_frame = LabelFrame(center_frame, text="Untreated Water", font=HELV24, pady=20, padx=20)
        untreated_water_frame.grid(row=1, column=0, columnspan=2)

        treated_water_frame = LabelFrame(center_frame, text="Treated Water    ", font=HELV24, pady=20, padx=20)
        treated_water_frame.grid(row=1, column=3, columnspan=2)

        temp_soil_frame = LabelFrame(center_frame, pady=20, padx=20)
        temp_soil_frame.grid(row=1, column=5, columnspan=2)

        input_container_frame = LabelFrame(center_frame, text="Input Container", font=HELV24, pady=20, padx=20)
        input_container_frame.grid(row=2, column=0, columnspan=2)

        output_container_frame = LabelFrame(center_frame, text="Output Container", font=HELV24, pady=20, padx=20)
        output_container_frame.grid(row=2, column=3, columnspan=2)

        time_flow_shut_frame = LabelFrame(center_frame, pady=20, padx=20)
        time_flow_shut_frame.grid(row=2, column=5, columnspan=2)
        
        #Untreated Water Frame
        self.ph_untreated = Label(untreated_water_frame, text="pH Level:", font=HELV18)
        self.ph_untreated_value = Label(untreated_water_frame, textvariable=self.ph_input_value, font=HELV18) 
        self.turb_untreated = Label(untreated_water_frame, text="Turbidity Level:", font=HELV18)
        self.turb_untreated_value = Label(untreated_water_frame, textvariable=self.turb_input_value, font=HELV18)
        self.vol_untreated = Label(untreated_water_frame, text="Volume:", font=HELV18)
        self.vol_untreated_value = Label(untreated_water_frame, textvariable=self.vol_input_value, font=HELV18)

        self.ph_untreated.grid(row=1, column=0, sticky=E)
        self.ph_untreated_value.grid(row=1, column=1)
        self.turb_untreated.grid(row=2, column=0, sticky=E)
        self.turb_untreated_value.grid(row=2, column=1)
        self.vol_untreated.grid(row=3, column=0, sticky=E)
        self.vol_untreated_value.grid(row=3, column=1)


        #Treated Frame
        self.ph_treated = Label(treated_water_frame, text="pH Level:", font=HELV18)
        self.ph_treated_value = Label(treated_water_frame, textvariable=self.ph_output_value, font=HELV18)
        self.turb_treated = Label(treated_water_frame, text="Turbidity Level:", font=HELV18)
        self.turb_treated_value = Label(treated_water_frame, textvariable=self.turb_output_value, font=HELV18)
        self.vol_treated = Label(treated_water_frame, text="Volume:", font=HELV18)
        self.vol_treated_value = Label(treated_water_frame, textvariable=self.vol_output_value, font=HELV18)
        
        self.ph_treated.grid(row=1, column=0, sticky=E)
        self.ph_treated_value.grid(row=1, column=1)
        self.turb_treated.grid(row=2, column=0, sticky=E)
        self.turb_treated_value.grid(row=2, column=1)
        self.vol_treated.grid(row=3, column=0, sticky=E)
        self.vol_treated_value.grid(row=3, column=1)


        #Input Container Frame
        self.ph_input = Label(input_container_frame, text="pH Level:", font=HELV18)
        self.ph_input_value = Entry(input_container_frame, text="value", width=6, font=HELV18)
        self.turb_input = Label(input_container_frame, text="Turbidity Level:", font=HELV18)
        self.turb_input_value = Entry(input_container_frame, text="value", width=6, font=HELV18)
        self.vol_input = Label(input_container_frame, text="Volume:", font=HELV18)
        self.vol_input_value = Entry(input_container_frame, text="value", width=6, font=HELV18)

        self.ph_input.grid(row=0, column=0, sticky=E)
        self.ph_input_value.grid(row=0, column=1)
        self.turb_input.grid(row=1, column=0, sticky=E)
        self.turb_input_value.grid(row=1, column=1)
        self.vol_input.grid(row=2, column=0, sticky=E)
        self.vol_input_value.grid(row=2, column=1)


        #Output Container Frame
        self.ph_output = Label(output_container_frame, text="pH Level:", font=HELV18)
        self.ph_output_value = Entry(output_container_frame, text="value", width=6, font=HELV18)
        self.turb_output = Label(output_container_frame, text="Turbidity Level:", font=HELV18)
        self.turb_output_value = Entry(output_container_frame, text="value", width=6, font=HELV18)
        self.vol_output = Label(output_container_frame, text="Volume:", font=HELV18)
        self.vol_output_value = Entry(output_container_frame, text="value", width=6, font=HELV18)

        self.ph_output.grid(row=0, column=0, sticky=E)
        self.ph_output_value.grid(row=0, column=1)
        self.turb_output.grid(row=1, column=0, sticky=E)
        self.turb_output_value.grid(row=1, column=1)
        self.vol_output.grid(row=2, column=0, sticky=E)
        self.vol_output_value.grid(row=2, column=1)
        

        #Temperature and Soil Moisture Frame
        self.temperature = Label(temp_soil_frame, text="Temperature:", font=HELV18)
        self.temperature_value = Label(temp_soil_frame, width=6, textvariable=temperature_value, font=HELV18) 
        self.soil_moisture = Label(temp_soil_frame, text="Soil Moisture:", font=HELV18)
        self.soil_moisture_value = Label(temp_soil_frame, width=6, textvariable=soil_moisture_value, font=HELV18) 

        self.temperature.grid(row=0, column=0)
        self.temperature_value.grid(row=0, column=1, sticky=E)
        self.soil_moisture.grid(row=1, column=0)
        self.soil_moisture_value.grid(row=1, column=1, sticky=E)


        #Timer, Flow rate, Shutdown system
        self.timer = Label(time_flow_shut_frame, text="00:00:00", font=HELV18)
        self.flowrate = Label(time_flow_shut_frame, text="Flow Rate", font=HELV18)
        self.shutdown = Button(time_flow_shut_frame, text="Shutdown", font=HELV18)

        self.timer.grid(row=0, column=0, columnspan=2)
        self.flowrate.grid(row=1, column=0, columnspan=2)
        self.shutdown.grid(row=2, column=0, columnspan=2)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        
        self.ph_input_value = StringVar()
        self.turb_input_value = StringVar()
        self.vol_input_value = StringVar()
        self.ph_output_value = StringVar()
        self.turb_output_value = StringVar()
        self.vol_output_value = StringVar()
        self.temperature_value = StringVar()
        self.soil_moisture_value = StringVar()
        self.createWidgets()
        self.pack()
        self.grid()
        self.measure()

root = Tk()
app = Application(master=root)

root.title("VERMIFILTER UI")
root.resizable(width=False, height=False)
root.geometry('{}x{}'.format(720, 480))

app.mainloop()
