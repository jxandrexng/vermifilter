#!/usr/bin/env python
import Tkinter as tk
import tkFont

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
##        self.quitButton = tk.Button(self, text='Quit',
##                                    command=self.quit)
##        self.quitButton.grid()
        
        self.helv36 = tkFont.Font(family = "Helvetica", size = 36, weight = "bold")
        self.helv24 = tkFont.Font(family = "Helvetica", size = 18, weight = "bold")
        self.helv18 = tkFont.Font(family = "Helvetica", size = 12, weight = "normal")
        self.helv12 = tkFont.Font(family = "Helvetica", size = 12, weight = "normal")
        
        self.top_frame = tk.Frame(self)
        self.left_frame = tk.Frame(self, bd=10)
        self.right_frame = tk.Frame(self, bd=10)
        self.bot_frame = tk.Frame(self, bd=10)

        #Title
        self.header_title = tk.Label(self.top_frame, text="Vermifilter UI", font=self.helv36)

        #Labels-Values for Untreated water
        self.untreated_label = tk.Label(self.left_frame, text="Untreated Water", font=self.helv24)

        self.untreated_ph = tk.Label(self.left_frame, text="pH Level:", font=self.helv18)
        self.untreated_ph_value = tk.Label(self.left_frame, font=self.helv18, width=4)

        self.untreated_turb = tk.Label(self.left_frame, text="Turbidity Level:", font=self.helv18)
        self.untreated_turb_value = tk.Label(self.left_frame, font=self.helv18, width=4)

        self.untreated_volume = tk.Label(self.left_frame, text="Volume:", font=self.helv18)
        self.untreated_volume_value = tk.Label(self.left_frame, font=self.helv18, width=4)

        self.untreated_soil = tk.Label(self.left_frame, text="Soil Moisture:", font=self.helv18)
        self.untreated_soil_value = tk.Label(self.left_frame, font=self.helv18, width=4)

        self.untreated_temperature = tk.Label(self.left_frame, text="Temperature:", font=self.helv18)
        self.untreated_temperature_value = tk.Label(self.left_frame, font=self.helv18, width=4)

        #Labels-Values for treated water
        self.treated_label = tk.Label(self.right_frame, text="Treated Water", font=self.helv24)

        self.treated_ph = tk.Label(self.right_frame, text="pH Level:", font=self.helv18)
        self.treated_ph_value = tk.Label(self.right_frame, font=self.helv18, width=4)

        self.treated_turb = tk.Label(self.right_frame, text="Turbidity Level:", font=self.helv18)
        self.treated_turb_value = tk.Label(self.right_frame, font=self.helv18, width=4)

        self.treated_volume = tk.Label(self.right_frame, text="Volume:", font=self.helv18)
        self.treated_volume_value = tk.Label(self.right_frame, font=self.helv18, width=4)

        self.treated_soil = tk.Label(self.right_frame, text="Soil Moisture:", font=self.helv18)
        self.treated_soil_value = tk.Label(self.right_frame, font=self.helv18, width=4)

        self.treated_temperature = tk.Label(self.right_frame, text="Temperature:", font=self.helv18)
        self.treated_temperature_value = tk.Label(self.right_frame, font=self.helv18, width=4)


        #Labels-Values for Input Container
        self.input_container_label = tk.Label(self.left_frame, text="Input Container", font=self.helv24)

        self.input_ph = tk.Label(self.left_frame, text="pH Level:", font=self.helv18)
        self.input_ph_value = tk.Entry(self.left_frame, font=self.helv18, width=4)

        self.input_turb = tk.Label(self.left_frame, text="Turbidity Level:", font=self.helv18)
        self.input_turb_value = tk.Entry(self.left_frame, font=self.helv18, width=4)

        self.input_volume = tk.Label(self.left_frame, text="Volume:", font=self.helv18)
        self.input_volume_value = tk.Entry(self.left_frame, font=self.helv18, width=4)


        #Labels-Values for Output Container
        self.output_container_label = tk.Label(self.right_frame, text="Output Container", font=self.helv24)

        self.output_ph = tk.Label(self.right_frame, text="pH Level:", font=self.helv18)
        self.output_ph_value = tk.Entry(self.right_frame, font=self.helv18, width=4)

        self.output_turb = tk.Label(self.right_frame, text="Turbidity Level:", font=self.helv18)
        self.output_turb_value = tk.Entry(self.right_frame, font=self.helv18, width=4)

        self.output_volume = tk.Label(self.right_frame, text="Volume:", font=self.helv18)
        self.output_volume_value = tk.Entry(self.right_frame, font=self.helv18, width=4)


        #Other Label-Values (Temperature and Soil Moisture)
        self.temperature = tk.Label(self.bot_frame, text="Temperature:", font=self.helv12)
        self.temperature_value = tk.Entry(self.bot_frame, font=self.helv12, width=4)

        self.soil_moisture = tk.Label(self.bot_frame, text="Soil Moisture:", font=self.helv12)
        self.soil_moisture_value = tk.Entry(self.bot_frame, font=self.helv12, width=4)

        #Layout Grid
        self.header_title.grid(row=0, pady=1)

        self.untreated_label.grid(row=1, column=1, columnspan=2, pady=10)
        self.treated_label.grid(row=1, column=3, columnspan=2, pady=10)

        self.untreated_ph.grid(row=2, column=1, sticky=tk.E, padx=10)
        self.untreated_ph_value.grid(row=2, column=2, sticky=tk.W)
        self.untreated_turb.grid(row=3, column=1, sticky=tk.E, padx=10)
        self.untreated_turb_value.grid(row=3, column=2, sticky=tk.W)
        self.untreated_volume.grid(row=4, column=1, sticky=tk.E, padx=10)
        self.untreated_volume_value.grid(row=4, column=2, sticky=tk.W)

        self.treated_ph.grid(row=2, column=3, sticky=tk.E, padx=10)
        self.treated_ph_value.grid(row=2, column=4, sticky=tk.W)
        self.treated_turb.grid(row=3, column=3, sticky=tk.E, padx=10)
        self.treated_turb_value.grid(row=3, column=4, sticky=tk.W)
        self.treated_volume.grid(row=4, column=3, sticky=tk.E, padx=10)
        self.treated_volume_value.grid(row=4, column=4, sticky=tk.W)

        self.input_container_label.grid(row=5, column=1, columnspan=2, pady=10)
        self.output_container_label.grid(row=5, column=3, columnspan=2, pady=10)

        self.input_ph.grid(row=6, column=1, sticky=tk.E, padx=10)
        self.input_ph_value.grid(row=6, column=2, sticky=tk.W)
        self.input_turb.grid(row=7, column=1, sticky=tk.E, padx=10)
        self.input_turb_value.grid(row=7, column=2, sticky=tk.W)
        self.input_volume.grid(row=8, column=1, sticky=tk.E, padx=10)
        self.input_volume_value.grid(row=8, column=2, sticky=tk.W)

        self.output_ph.grid(row=6, column=3, sticky=tk.E, padx=10)
        self.output_ph_value.grid(row=6, column=4, sticky=tk.W)
        self.output_turb.grid(row=7, column=3, sticky=tk.E, padx=10)
        self.output_turb_value.grid(row=7, column=4, sticky=tk.W)
        self.output_volume.grid(row=8, column=3, sticky=tk.E, padx=10)
        self.output_volume_value.grid(row=8, column=4, sticky=tk.W)

        self.temperature.grid(row=9, column=1, sticky=tk.E)
        self.temperature_value.grid(row=9, column=2, sticky=tk.W)

        self.soil_moisture.grid(row=10, column=1, sticky=tk.E)
        self.soil_moisture_value.grid(row=10, column=2, sticky=tk.W)


app = Application()
app.master.title('Automated Vermifiltration System')
app.master.resizable(width=False, height=False)
app.master.geometry('{}x{}'.format(720, 480))
app.mainloop()
