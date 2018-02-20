import time
import serial
from Tkinter import Tk, Frame, LabelFrame, Label, Button, Entry, StringVar, N, E, S, W

##serial_speed = 9600
##serial_port = '/dev/ttyACM0'

#ser = serial.Serial(serial_port, serial_speed, timeout=1)

HELV36 = ("Helvetica", 36, "bold")
HELV24 = ("Helvetica", 18, "bold")
HELV18 = ("Helvetica", 12, "normal")
HELV12 = ("Helvetica", 12, "normal")

class VermifilterUI(object):

    
    
    def measure(self):

        data = ser.readline()

        if (data != " "):
            try:
                processed_data = data.split(" ")

                self.ph_input_value.set(str(processed_data[0]))
                
                self.turb_input_value.set(str(processed_data[1]))
                
                self.vol_input_value.set(str(processed_data[2]))
                
                self.ph_output_value.set(str(processed_data[3]))
                
                self.turb_output_value.set(str(processed_data[4]))
                
                self.vol_output_value.set(str(processed_data[5]))
                
                self.temperature_value.set(str(processed_data[6]))
                
                self.soil_moisture_value.set(str(processed_data[7]))
                

            except IndexError:
                pass

        self.after(1000, self.measure)

    def update_timeText(self):
        if (state):
            global timer
            # Every time this function is called, 
            # we will increment 1 centisecond (1/100 of a second)
            self.timer[2] += 1
            
            # Every 100 centisecond is equal to 1 second
            if (self.timer[2] >= 100):
                self.timer[2] = 0
                self.timer[1] += 1
            # Every 60 seconds is equal to 1 min
            if (self.timer[1] >= 60):
                self.timer[0] += 1
                self.timer[1] = 0
            # We create our time string here
            self.timeString = pattern.format(self.timer[0], self.timer[1], self.timer[2])
            # Update the timeText Label box with the current time
            self.timeText.configure(text=self.timeString)
            # Call the update_timeText() function after 1 centisecond
        root.after(10, self.update_timeText)

    
    def start(self):
        global state
        state = True

    def pause(self):
        global state
        state = False

    def reset(self):
        global timer
        self.timer = [0, 0, 0]
        timeText.configure(text='00:00:00')
        
    def exist(self):
        root.destroy()    

    def shutdown(self):
        os.system("sudo shutdown -h now")

    def __init__(self, master):
##        self.ph_input_value = StringVar()
##        self.turb_input_value = StringVar()
##        self.vol_input_value = StringVar()
##        self.ph_output_value = StringVar()
##        self.turb_output_value = StringVar()
##        self.vol_output_value = StringVar()
##        self.temperature_value = StringVar()
##        self.soil_moisture_value = StringVar()
##
##        self.measure()
        
        self.master = master
        master.title("VERMIFILTER UI")
        master.resizable(width=False, height=False)
        master.geometry('{}x{}'.format(720, 480))

        center_frame = Frame(master, width=720, height=480)
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

        self.timer = [0, 0, 0]
        self.pattern = '{0:02d}:{1:02d}:{2:02d}'
        
        #Untreated Water Frame
        self.ph_untreated = Label(untreated_water_frame, text="pH Level:", font=HELV18)
        self.ph_untreated_value = Label(untreated_water_frame, font=HELV18) #textvariable=self.ph_input_value, 
        self.turb_untreated = Label(untreated_water_frame, text="Turbidity Level:", font=HELV18)
        self.turb_untreated_value = Label(untreated_water_frame, font=HELV18) #textvariable=self.turb_input_value,
        self.vol_untreated = Label(untreated_water_frame, text="Volume:", font=HELV18)
        self.vol_untreated_value = Label(untreated_water_frame, font=HELV18) #textvariable=self.vol_input_value

        self.ph_untreated.grid(row=1, column=0, sticky=E)
        self.ph_untreated_value.grid(row=1, column=1)
        self.turb_untreated.grid(row=2, column=0, sticky=E)
        self.turb_untreated_value.grid(row=2, column=1)
        self.vol_untreated.grid(row=3, column=0, sticky=E)
        self.vol_untreated_value.grid(row=3, column=1)


        #Treated Frame
        self.ph_treated = Label(treated_water_frame, text="pH Level:", font=HELV18)
        self.ph_treated_value = Label(treated_water_frame, font=HELV18) #textvariable=self.ph_output_value
        self.turb_treated = Label(treated_water_frame, text="Turbidity Level:", font=HELV18)
        self.turb_treated_value = Label(treated_water_frame, font=HELV18) #textvariable=self.turb_output_value
        self.vol_treated = Label(treated_water_frame, text="Volume:", font=HELV18)
        self.vol_treated_value = Label(treated_water_frame, font=HELV18) #textvariable=self.vol_output_value
        
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
        self.temperature_value = Label(temp_soil_frame, width=6, font=HELV18) #textvariable=temperature_value,
        self.soil_moisture = Label(temp_soil_frame, text="Soil Moisture:", font=HELV18)
        self.soil_moisture_value = Label(temp_soil_frame, width=6, font=HELV18) #textvariable=soil_moisture_value,

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

        self.update_timeText()
        self.start()

state = False

root = Tk()
my_gui = VermifilterUI(root)
root.mainloop()
