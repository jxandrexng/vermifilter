import os
import time
import random
import serial
import tkMessageBox
import MySQLdb
from Tkinter import *

#connection of serial port to arduino
serial_speed = 2000000
serial_port = '/dev/ttyACM0'

ser = serial.Serial(serial_port, serial_speed, timeout = 0.001)

#font
HELV29 = ("Helvetica", 29, "bold")
HELV18 = ("Helvetica", 18, "bold")
HELV12 = ("Helvetica", 12, "bold")
HELV10 = ("Helvetica", 10, "bold")
HELV9 = ("Helvetica", 9, "bold")
HELV7 = ("Helvetica", 7, "bold")


class Application(Frame):

    def __init__(self, master=None):
            Frame.__init__(self, master, bg="azure")
            #frame format
            self.master = master
            master.title("Automated Vermifiltration System")
            master.resizable(width=False, height=False)
            master.geometry('{}x{}'.format(800, 480))

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
            self.ph_saved_data = StringVar()
            self.Nph_saved_data = StringVar()
            self.turb_saved_data = StringVar()
            self.Nturb_saved_data = StringVar()
            self.timeInterval = IntVar()
            self.ph_value = StringVar()
            
            self.frame()
            self.createWidgets()
            self.pack()
            self.measure()
            self.running = False
            self.timer = [0,0,0,0]    # [minutes ,seconds, centiseconds]
            self.timeString = str(self.timer[0]) + ':' + str(self.timer[1]) + ':' + str(self.timer[2]) + ':' + str(self.timer[3])
            self.update_time()
            self.time()
    
    def frame(self):
        #setting frame
        self.f3 = Frame(self, width = 280, height = 100, relief=SUNKEN, bd=5)
        self.f3.grid(row=2)

        self.f3a = Frame(self.f3, width=170, height=100, bd=5, relief="raise", bg="cyan")
        self.f3a.grid(row=2)

        self.f3b = Frame(self.f3a, width=90, height=70, bd=5, bg="light goldenrod", padx=10, pady=15, relief="raise")
        self.f3b.grid(row=2, column=0)

        self.f3c = Frame(self.f3a, width=90, height=70, bd=5, bg="OliveDrab1", padx=10, pady=15, relief="raise")
        self.f3c.grid(row=2, column=1)

        self.f3d = Frame(self.f3a, width=45, height=10, pady=3, bd=5, bg="SkyBlue1", relief="raise")
        self.f3d.grid(row=3, column=0, columnspan=2)

        self.f4 = Frame(self, width = 30, height = 75, relief=SUNKEN, bd=5)
        self.f4.grid(row=2, column=2)

        self.f4a = Frame(self.f4, width = 30, height = 75, relief="raise", bd=5, pady=3, padx=1, bg="white")
        self.f4a.grid(row=2, column=2, ipadx=1)

        self.f5 = Frame(self, width = 200, height = 75, relief=SUNKEN, bd=5)
        self.f5.grid(row=3, column=0)

        self.f5a = Frame(self.f5, width = 180, height = 75, relief="raise", bd=5, padx=35, bg="cyan")
        self.f5a.grid(row=3, column=0)

        self.f6 = Frame(self, width = 140, height = 75, relief=SUNKEN, bd=5)
        self.f6.grid(row=3, column=2, columnspan=2)

        self.f6a = Frame(self.f6, width = 50, height = 75, relief="raise", bd=5, pady=5, bg="cyan")
        self.f6a.grid(row=3, column=2, columnspan=2)

    def input_saved(self):
         self.ph_saved_data.set(self.ph_input.get())
         self.turb_saved_data.set(self.turb_input.get())
         
    def output_saved(self):
         self.Nph_saved_data.set(self.ph_output.get())
         self.Nturb_saved_data.set(self.turb_output.get())
        
        
                
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

                #===========================Data grid Container========================================
                #Untreated
                self.Untreated_label_name.set("Untreated Water")
                self.Untreated_label.grid(row=2, column=0, columnspan=2)
                
                #Nph input
                self.Nph_input_label_name.set("Ph Input: ")
                self.Nph_input_label.grid(row=3, column=0, columnspan=1, ipadx=5)

                self.Nph_input_data.set("Ph Input: ")
                self.Nph_input.grid(row=3, column=1, ipadx=5)

                #Nturbidity input
                self.Nturb_input_label_name.set("Turbidity Input: ")
                self.Nturb_input_label.grid(row=4, column=0)
                
                self.Nturb_input_data.set("Turbidity Input: ")
                self.Nturb_input.grid(row=4, column=1)

                #breakline
                self.Breakline_label_name.set("--------")
                self.Breakline_label.grid(row=5, column=0, columnspan=2)
                
                #Treated label
                self.Treated_label_name.set("Treated Water")
                self.Treated_label.grid(row=6, column=0, columnspan=2)
                
                #Nph output
                self.Nph_output_label_name.set("Ph Output: ")
                self.Nph_output_label.grid(row=7, column=0)
                
                self.Nph_output_data.set("Ph Output: ")
                self.Nph_output.grid(row=7, column=1)

                #Nturbidity output
                self.Nturb_output_label_name.set("Turbidity Output: ")
                self.Nturb_output_label.grid(row=8, column=0)
                
                self.Nturb_output_data.set("Turbidity Output: ")
                self.Nturb_output.grid(row=8, column=1)

            except IndexError:
                pass

        self.after(250, self.measure)

    def createWidgets(self):
        #=====================================Untreated==========================================================
        #header
        self.header_frame_label = Label(self, textvariable=self.header_frame_label_name, bg="azure", font=HELV29, fg="Steel Blue", bd=10)
        self.header_frame_label_name.set("Vermifilter UI")
        
        self.localtime = Label(self, textvariable=self.localtime_name, font=HELV12, fg="Steel Blue", bd=10, bg="azure")
        self.localtime_name.set(time.asctime(time.localtime(time.time())))
        
        #ph Input
        self.ph_input_label = Label(self.f3b, textvariable=self.ph_input_label_name, font=HELV12, padx=10, pady=10, bg="light goldenrod")
        self.ph_input_label_name.set("ph Input")
        
        self.ph_input = Entry(self.f3b, textvariable=self.ph_input_data, width=10, font=HELV12, bd=5, bg= "powder blue")
        self.ph_input_data.set("pH Input")

        #turbidity input
        self.turb_input_label = Label(self.f3b, textvariable=self.turb_input_label_name, font=HELV12,padx=10, pady=10, bg="light goldenrod")
        self.turb_input_label_name.set("turbidity Input")
        
        self.turb_input = Entry(self.f3b, textvariable=self.turb_input_data, width=10, font=HELV12, bd=5, bg="powder blue")
        self.turb_input_data.set("Turbidity Input")

        #volume input
        self.vol_input_label = Label(self.f3b, textvariable=self.vol_input_label_name, font=HELV12,padx=10, pady=10, bg="light goldenrod")
        self.vol_input_label_name.set("Volume Input")
        
        self.vol_input = Label(self.f3b, textvariable=self.vol_input_data, font=HELV12, bd=5, bg="light goldenrod")
        self.vol_input_data.set("Volume Input")

        #===================================Treated=======================================================================
        #ph output
        self.ph_output_label = Label(self.f3c, textvariable=self.ph_output_label_name, font=HELV12, padx=10, pady=10, bg="OliveDrab1")
        self.ph_output_label_name.set("PH Output")

        self.ph_output = Entry(self.f3c, textvariable=self.ph_output_data, width=10, font=HELV12, bd=5)
        self.ph_output_data.set("pH Output")

        #turbidity Output
        self.turb_output_label = Label(self.f3c, textvariable=self.turb_output_label_name, font=HELV12,padx=10, pady=10, bg="OliveDrab1")
        self.turb_output_label_name.set("turbidity Output")
        
        self.turb_output = Entry(self.f3c, textvariable=self.turb_output_data, width=10, font=HELV12, bd=5)
        self.turb_output_data.set("Turbidity Output")

        #volume Output
        self.vol_output_label = Label(self.f3c, textvariable=self.vol_output_label_name, font=HELV12,padx=10, pady=10, bg="OliveDrab1")
        self.vol_output_label_name.set("Volume Output")
        
        self.vol_output = Label(self.f3c, textvariable=self.vol_output_data, font=HELV12, bd=5, bg="OliveDrab1")
        self.vol_output_data.set("Volume Output")

        #==============================Other Sensors======================
        
        #Soil Moisture
        self.soil_moisture_label = Label(self.f3d, textvariable=self.soil_moisture_label_name, font=HELV12,padx=10, pady=5, bg="coral1")
        self.soil_moisture_label_name.set("Soil Moisture")
        
        self.soil_moisture = Label(self.f3d, textvariable=self.soil_moisture_data, font=HELV12, bd=5, bg="coral1")
        self.soil_moisture_data.set("Soil Moisture")
        #Temperature
        self.temperature_label = Label(self.f3d, textvariable=self.temperature_label_name, font=HELV12,padx=10, pady=5, bg="coral1")
        self.temperature_label_name.set("Temperature")
        
        self.temperature = Label(self.f3d, textvariable=self.temperature_data, font=HELV12, bd=5, bg="coral1")
        self.temperature_data.set("Temperature")

        #=====================================Data container frame==============================================
        #untreated label
        self.Untreated_label = Label(self.f4a, text="Untreated Water", fg="red", font=HELV12, bg="white")
        
        #ph Input
        self.Nph_input_label = Label(self.f4a, text="pH Influent: ", font=HELV9, padx=10, bg="white")

        self.Nph_input = Label(self.f4a, textvariable=self.ph_saved_data, font=HELV9, bg="white")
        #turbidity input
        self.Nturb_input_label = Label(self.f4a, text="Turbidity Influent: ", font=HELV9, padx=10, bg="white")
        
        self.Nturb_input = Label(self.f4a, textvariable=self.turb_saved_data, font=HELV9, bg="white")

        #Breakline
        self.Breakline_label = Label(self.f4a, text="--------------------------------------", font=HELV12, bg="white")
        
        #Treated label
        self.Treated_label = Label(self.f4a, text="Treated Water", fg="green", font=HELV12, bg="white")
        
        #Nph output
        self.Nph_output_label = Label(self.f4a, text="pH Efluent:", font=HELV9, padx=10, bg="white")
   
        self.Nph_output = Label(self.f4a, textvariable=self.Nph_saved_data, font=HELV9, bg="white")

        #turbidity Output
        self.Nturb_output_label = Label(self.f4a, text="Turbidity Efluent: ", font=HELV9, padx=10, bg="white")
        
        self.Nturb_output = Label(self.f4a, textvariable=self.Nturb_saved_data, font=HELV9, bg="white")
        
        #line-height-top
        self.bottom = Label(self.f4a, text=' ' , bg="white")
        self.bottom.grid(row=0, column=0, columnspan=2)
        
        #timer
        self.show = Label(self.f4a, text='00:00:00:00', font=('Helvetica', 15), bg="white")
        self.show.grid(row=1, column=0, columnspan=2)

        #line-height-bottom
        self.bottom = Label(self.f4a, text=' ' , bg="white")
        self.bottom.grid(row=9, column=0, columnspan=2)
        
        #===============================Buttons 3rd Container=======================
        #Button Save in
        self.btn_save_in = Button(self.f5a, text="Save In", command=self.input_saved, bg="light goldenrod", bd=8, font=HELV12, padx=5, pady=5).grid(row=0,column=0)

        #Button Save out
        self.btn_save_out = Button(self.f5a, text="Save Out", command=self.output_saved, bg="OliveDrab1", bd=8, font=HELV12, padx=5, pady=5).grid(row=0,column=1)

        #Button Start
        self.btn_start = Button(self.f5a, text="Start", command=self.start, bd=8, font=HELV12, bg="Green2", padx=5, pady=5).grid(row=0,column=2)

        #Button Stop
        self.btn_stop = Button(self.f5a, text="Stop", bd=8, command=self.stop, font=HELV12, bg="red2", padx=5, pady=5).grid(row=0,column=3)

        #Button Reset
        self.btn_reset = Button(self.f5a, text="Reset", command=self.resetTime, bd=8, bg="DarkGoldenrod1", font=HELV12, padx=5, pady=5).grid(row=0,column=4)

        #Button Shutdown
        self.btn_shutdown = Button(self.f5a, text="Shutdown", command=self.iexit, bd=8, bg="gray70", font=HELV12, padx=5, pady=5).grid(row=0,column=5)

        #=======================Credits 4th container======================
        self.company_name = Label(self.f6a, text= u"\u00A9 JME    ", font=HELV12, bg="cyan")
        self.company_name.grid(row=0, column=0)

        self.company_name = Label(self.f6a, text="         Adviser: Jerwin V. Obmerga               ", font=HELV7, bg="cyan")
        self.company_name.grid(row=1, column=0)
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
              
            if(self.timer[1] == 2): #initialize al readings before saving the input
                self.input_saved()
                
            if(self.timer[1] == 30): #ph input after dillution process
                self.input_saved()  

            if(self.timer[0] == 1 and self.timer[1] == 0 and self.timer[2] == 1):# after 1 hour the effluent will measure the output
                self.input_saved()
                self.output_saved()
                
            if(self.timer[0] == 1 and self.timer[1] == 30 and self.timer[2] == 1):
                self.input_saved()
                self.output_saved()
                
            if(self.timer[0] == 2 and self.timer[1] == 0 and self.timer[2] == 1):
                self.input_saved()
                self.output_saved()

            if(self.timer[0] == 2 and self.timer[1] == 30 and self.timer[2] == 1):
                self.input_saved()
                self.output_saved()

            if(self.timer[0] == 3 and self.timer[1] == 0 and self.timer[2] == 1):
                self.input_saved()
                self.output_saved()

            if(self.timer[0] == 3 and self.timer[1] == 30 and self.timer[2] == 1):
                self.input_saved()
                self.output_saved()

            if(self.timer[0] == 4 and self.timer[1] == 0 and self.timer[2] == 1):
                self.input_saved()
                self.output_saved()

            if(self.timer[0] == 4 and self.timer[1] == 30 and self.timer[2] == 1):
                self.input_saved()
                self.output_saved()

            if(self.timer[0] == 5 and self.timer[1] == 0 and self.timer[2] == 1):
                self.input_saved()
                self.output_saved()
                
            self.timeString = str(self.timer[0]) + ':' + str(self.timer[1]) + ':' + str(self.timer[2]) + ':' + str(self.timer[3])
            self.show.config(text=self.timeString)
        root.after(10, self.update_time)

    def start(self):            #Start the clock
        self.running = True 
        ser.write("1")
        print ('Clock Running...')

    def stop(self):            #Pause the clock
        self.running = False
        ser.write("2")
        print ('Clock Paused')   

    def resetTime(self):        #Reset the clock
        self.running = False
        self.timer = [0,0,0,0]
        print ('Clock is Reset')  
        self.show.config(text='00:00:00:00')
        self.ph_saved_data.set("")
        self.turb_saved_data.set("")
        self.Nph_saved_data.set("")
        self.Nturb_saved_data.set("")


    def time(self):
        self.timeInterval = 0
    
    def pump(self):
        ser.write("1")
        print ('Pump')
        
    def iexit(self):
        self.qexit = tkMessageBox.askyesno(" ", "Are you sure you want to exit?")
        if self.qexit > 0:
            root.destroy()
            os.system("sudo shutdown -h now")
            return


root = Tk()
app = Application(master=root)
root.mainloop()

