import time
import random
import serial
import MySQLdb
from Tkinter import *

#connection of serial port to arduino
serial_speed = 9600
serial_port = '/dev/ttyACM1'

ser = serial.Serial(serial_port, serial_speed, timeout=1)

#font
HELV29 = ("Helvetica", 29, "bold")
HELV18 = ("Helvetica", 18, "bold")
HELV12 = ("Helvetica", 12, "bold")
HELV10 = ("Helvetica", 10, "bold")


class Application(Frame):

    
    def __init__(self, master=None):
            Frame.__init__(self, master)
            #frame format
            self.master = master
            master.title("Automated Vermifiltration System")
            master.resizable(width=False, height=False)
            master.geometry('{}x{}'.format(790, 480))

            self.header_frame_label_name = StringVar()
            self.localtime_name = StringVar()
            self.ph_input_label_name = StringVar()
            self.ph_input_data = StringVar()
            self.turb_input_label_name = StringVar()
            self.turb_input_data = StringVar()
            self.vol_input_label_name = StringVar()
            self.vol_input_data = StringVar()
            self.ph_output_label_name = StringVar()
            self.ph_output_data = StringVar()
            self.turb_output_label_name = StringVar()
            self.turb_output_data = StringVar()
            self.vol_output_label_name = StringVar()
            self.vol_output_data = StringVar()
            self.soil_moisture_label_name = StringVar()
            self.soil_moisture_data = StringVar()
            self.temperature_label_name = StringVar()
            self.temperature_data = StringVar()
            self.Nph_input_label_name = StringVar()
            self.Nph_input_data = StringVar()
            self.Nturb_input_label_name = StringVar()
            self.Nturb_input_data = StringVar()
            self.Nph_output_label_name = StringVar()
            self.Nph_output_data = StringVar()
            self.Nturb_output_label_name = StringVar()
            self.Nturb_output_data = StringVar()
            self.Untreated_label_name = StringVar()
            self.Treated_label_name = StringVar()
            self.Breakline_label_name = StringVar()
            self.btn_dispense_speed = StringVar()
            self.timeText = StringVar()
            
            self.frame()
            self.createWidgets()
            self.pack()
            self.measure()
            self.running = False
            self.timer = [0,0,0,0]    # [minutes ,seconds, centiseconds]
            self.timeString = str(self.timer[0]) + ':' + str(self.timer[1]) + ':' + str(self.timer[2]) + ':' + str(self.timer[3])
            self.update_time()
    
    def frame(self):
        #setting frame
        self.f3 = Frame(self, width = 520, height = 100, relief=SUNKEN, bd=10)
        self.f3.grid(row=2)

        self.f3a = Frame(self.f3, width=590, height=100, bd=10, relief="raise", padx=20, pady=20)
        self.f3a.grid(row=2)

        self.f4 = Frame(self, width = 190, height = 235, relief=SUNKEN, bd=10)
        self.f4.grid(row=2, column=2)

        self.f4a = Frame(self, width = 100, height = 235, relief="raise", bd=5, pady=10)
        self.f4a.grid(row=2, column=2, ipadx=1)

        self.f5 = Frame(self, width = 590, height = 75, relief=SUNKEN, bd=10)
        self.f5.grid(row=3, column=0)

        self.f5a = Frame(self, width = 580, height = 75, relief="raise", bd=5, padx=50)
        self.f5a.grid(row=3, column=0)

        self.f6 = Frame(self, width = 190, height = 75, relief=SUNKEN, bd=10)
        self.f6.grid(row=3, column=2)

        self.f6a = Frame(self, width = 180, height = 75, relief="raise", bd=5, padx=35)
        self.f6a.grid(row=3, column=2)
        
            
    #get the values from the arduino and split and store to the text variable
    def measure(self):

        data = ser.readline()

        if (data != " "):
            try:
                processed_data = data.split(" ")

                #header
                self.header_frame_label_name.set("Automated Vermifiltration System")
                self.header_frame_label.grid(row=0, column=0, columnspan=5)

                #Local Time
                self.localtime_name = time.asctime(time.localtime(time.time()))
                self.localtime.grid(row=1, column=0, columnspan=5)
                
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

                #ph output
                self.ph_output_label_name.set("Ph Output: ")
                self.ph_output_label.grid(row=2, column=4)
                
                self.ph_output_data.set(str(processed_data[3]))
                self.ph_output.grid(row=2, column=5)

                #turbidity output
                self.turb_output_label_name.set("Turbidity Output: ")
                self.turb_output_label.grid(row=3, column=4)
                
                self.turb_output_data.set(str(processed_data[4]))
                self.turb_output.grid(row=3, column=5)

                #volume output
                self.vol_output_label_name.set("Volume Output: ")
                self.vol_output_label.grid(row=4, column=4)
                
                self.vol_output_data.set(str(processed_data[5]))
                self.vol_output.grid(row=4, column=5)

                #soil moisture
                self.soil_moisture_label_name.set("Soil Moisture: ")
                self.soil_moisture_label.grid(row=6, column=0)
                
                self.soil_moisture_data.set(str(processed_data[6]))
                self.soil_moisture.grid(row=6, column=1)

                #temperature
                self.temperature_label_name.set("Temperature: ")
                self.temperature_label.grid(row=6, column=4)
                
                self.temperature_data.set(str(processed_data[7]))
                self.temperature.grid(row=6, column=5)

                #===========================2nd Frame Container========================================
                #Untreated
                self.Untreated_label_name.set("Untreated Water")
                self.Untreated_label.grid(row=1, column=0, columnspan=2)
                
                #Nph input
                self.Nph_input_label_name.set("Ph Input: ")
                self.Nph_input_label.grid(row=2, column=0)

                self.Nph_input_data.set("Ph Input: ")
                self.Nph_input.grid(row=2, column=1)

                #Nturbidity input
                self.Nturb_input_label_name.set("Turbidity Input: ")
                self.Nturb_input_label.grid(row=3, column=0)
                
                self.Nturb_input_data.set("Turbidity Input: ")
                self.Nturb_input.grid(row=3, column=1)

                #breakline
                self.Breakline_label_name.set("-------------")
                self.Breakline_label.grid(row=4, column=0, columnspan=2)
                
                #Treated label
                self.Treated_label_name.set("Treated Water")
                self.Treated_label.grid(row=5, column=0, columnspan=2)
                
                #Nph output
                self.Nph_output_label_name.set("Ph Output: ")
                self.Nph_output_label.grid(row=6, column=0)
                
                self.Nph_output_data.set("Ph Output: ")
                self.Nph_output.grid(row=6, column=1)

                #Nturbidity output
                self.Nturb_output_label_name.set("Turbidity Output: ")
                self.Nturb_output_label.grid(row=7, column=0)
                
                self.Nturb_output_data.set("Turbidity Output: ")
                self.Nturb_output.grid(row=7, column=1)

            except IndexError:
                pass

        self.after(1000, self.measure)

    def createWidgets(self):
        #=====================================Untreated==========================================================
        #header
        self.header_frame_label = Label(self, textvariable=self.header_frame_label_name, font=HELV29, fg="Steel Blue", bd=10)
        self.header_frame_label_name.set("Vermifilter UI")
        
        self.localtime = Label(self, textvariable=self.localtime_name, font=HELV12, fg="Steel Blue", bd=10)
        self.localtime_name.set(time.asctime(time.localtime(time.time())))
        
        #ph Input
        self.ph_input_label = Label(self.f3a, textvariable=self.ph_input_label_name, font=HELV12, padx=10, pady=10)
        self.ph_input_label_name.set("ph Input")
        
        self.ph_input = Entry(self.f3a, textvariable=self.ph_input_data, width=10, font=HELV12, bd=5, bg= "powder blue")
        self.ph_input_data.set("pH Input")

        #turbidity input
        self.turb_input_label = Label(self.f3a, textvariable=self.turb_input_label_name, font=HELV12,padx=10, pady=10)
        self.turb_input_label_name.set("turbidity Input")
        
        self.turb_input = Entry(self.f3a, textvariable=self.turb_input_data, width=10, font=HELV12, bd=5, bg="powder blue")
        self.turb_input_data.set("Turbidity Input")

        #volume input
        self.vol_input_label = Label(self.f3a, textvariable=self.vol_input_label_name, font=HELV12,padx=10, pady=10)
        self.vol_input_label_name.set("Volume Input")
        
        self.vol_input = Label(self.f3a, textvariable=self.vol_input_data, font=HELV12, bd=5)
        self.vol_input_data.set("Volume Input")

        #===================================Treated=======================================================================
        #ph output
        self.ph_output_label = Label(self.f3a, textvariable=self.ph_output_label_name, font=HELV12, padx=10, pady=10)
        self.ph_output_label_name.set("PH Output")

        self.ph_output = Entry(self.f3a, textvariable=self.ph_output_data, width=10, font=HELV12, bd=5)
        self.ph_output_data.set("pH Output")

        #turbidity Output
        self.turb_output_label = Label(self.f3a, textvariable=self.turb_output_label_name, font=HELV12,padx=10, pady=10)
        self.turb_output_label_name.set("turbidity Output")
        
        self.turb_output = Entry(self.f3a, textvariable=self.turb_output_data, width=10, font=HELV12, bd=5)
        self.turb_output_data.set("Turbidity Output")

        #volume Output
        self.vol_output_label = Label(self.f3a, textvariable=self.vol_output_label_name, font=HELV12,padx=10, pady=10)
        self.vol_output_label_name.set("Volume Output")
        
        self.vol_output = Label(self.f3a, textvariable=self.vol_output_data, font=HELV12, bd=5)
        self.vol_output_data.set("Volume Output")

        #==============================Other Sensors======================
        
        #Soil Moisture
        self.soil_moisture_label = Label(self.f3a, textvariable=self.soil_moisture_label_name, font=HELV12,padx=10, pady=10)
        self.soil_moisture_label_name.set("Soil Moisture")
        
        self.soil_moisture = Label(self.f3a, textvariable=self.soil_moisture_data, font=HELV12, bd=5)
        self.soil_moisture_data.set("Soil Moisture")

        #Temperature
        self.temperature_label = Label(self.f3a, textvariable=self.temperature_label_name, font=HELV12,padx=10, pady=10)
        self.temperature_label_name.set("Temperature")
        
        self.temperature = Label(self.f3a, textvariable=self.temperature_data, font=HELV12, bd=5)
        self.temperature_data.set("Temperature")

        #=====================================Data container frame==============================================
        #untreated label
        self.Untreated_label = Label(self.f4a, text="Untreated Water", font=HELV12)
        
        #ph Input
        self.Nph_input_label = Label(self.f4a, text="PH Input: ", font=HELV10, padx=10)

        self.Nph_input = Label(self.f4a, text="231", font=HELV10)

        #turbidity input
        self.Nturb_input_label = Label(self.f4a, text="Turbidity Input: ", font=HELV10, padx=10)
        
        self.Nturb_input = Label(self.f4a, text="132", font=HELV10)

        #Brekline
        self.Breakline_label = Label(self.f4a, text="-----------------------------", font=HELV12)
        
        #Treated label
        self.Treated_label = Label(self.f4a, text="Treated Water", font=HELV12)
        
        #Nph output
        self.Nph_output_label = Label(self.f4a, text="PH Output", font=HELV10, padx=10)
   
        self.Nph_output = Label(self.f4a, text="123", font=HELV10)

        #turbidity Output
        self.Nturb_output_label = Label(self.f4a, text="Turbidity Output: ", font=HELV10, padx=10)
        
        self.Nturb_output = Label(self.f4a, text="212", font=HELV10)

        #timer
        self.show = Label(self.f4a, text='00:00:00:00', font=('Helvetica', 15))
        self.show.grid(row=0, column=0, columnspan=2)

        

        #Soda Ash Level
        self.soda_ash = Label(self.f4a, text="Ash Level:", font=HELV12)
        self.soda_ash.grid(row=9, column=0)

        self.soda_ash_data = Label(self.f4a, text="Low", font=HELV12)
        self.soda_ash_data.grid(row=9,column=1)

        #===============================Buttons 3rd Container=======================
        #Button Pump
        self.btn_pump = Button(self.f5a, text="Pump", command=self.pump, bd=8, font=HELV12, padx=5, pady=5).grid(row=0,column=0)

        #Button ADD Soda
        self.btn_add_soda = Button(self.f5a, text="Add Soda", command=self.add_soda, bd=8, font=HELV12, padx=5, pady=5).grid(row=0,column=1)

        #Button Dispense
        self.btn_dispense = Button(self.f5a, text="Dispense", command=self.start, bd=8, font=HELV12, padx=5, pady=5).grid(row=0,column=2)

        #Button Stop
        self.btn_stop = Button(self.f5a, text="Stop", bd=8, command=self.pause, font=HELV12, padx=5, pady=5).grid(row=0,column=3)

        #Button Shutdown
        self.btn_shutdown = Button(self.f5a, text="Shutdown", bd=8, font=HELV12, padx=5, pady=5).grid(row=0,column=4)

        #=======================Button 4th container======================
        #Button -
        self.btn_minus = Button(self.f6a, text="-", command=self.decrease_delay, bd=3, font=HELV12, padx=8, pady=6).grid(row=0, column=0)

        #Button +
        self.btn_plus = Button(self.f6a, text="+", command=self.increase_delay, bd=3, font=HELV12, padx=5, pady=6).grid(row=0, column=1)

        #Speed
        self.btn_dispense_speed = Label(self.f6a, text="123", font=HELV12).grid(row=0, column=2)


    #================================ Timer =============================
    def update_time(self):

        if (self.running == True):      #Clock is running

            self.timer[3] += 1

            if (self.timer[3] >= 100):  #100 centiseconds --> 1 second
                self.timer[3] = 0
                self.timer[2] += 1      #add 1 second

            if (self.timer[2] >= 60):   #60 seconds --> 1 minute
                self.timer[1] += 1
                self.timer[2] = 0

            if (self.timer[1] >= 60):
                self.timer[0] += 1
                self.timer[1] = 0

            self.timeString = str(self.timer[0]) + ':' + str(self.timer[1]) + ':' + str(self.timer[2]) + ':' + str(self.timer[3])
            self.show.config(text=self.timeString)
        root.after(10, self.update_time)


    def start(self):            #Start the clock
        self.running = True
        ser.write("3")
        print 'Clock Running...'

    def pause(self):            #Pause the clock
        self.running = False
        ser.write("4")
        print 'Clock Paused'    

    def resetTime(self):        #Reset the clock
        self.running = False
        self.timer = [0,0,0,0]
        print 'Clock is Reset'  
        self.show.config(text='00:00:00:00')

    def quit(self):             #Quit the program
        root.destroy()

    #=============================Functions=============================
    def pump(self):
        ser.write("1")
        print 'Pump'

    def add_soda(self):
        ser.write("2")
        print 'Add Soda'

    def decrease_delay(self):
        ser.write("5")
        print 'Delay Decreased'
        
    def increase_delay(self):
        ser.write("6")
        print 'Delay Increased'

root = Tk()
app = Application(master=root)
root.mainloop()

