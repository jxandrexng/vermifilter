# Graphical User Interface for the Bluetooth sensor

# Imports
import time
import serial
from Tkinter import *

# Serial port parameters
serial_speed = 9600
serial_port = '/dev/ttyACM1'

# Test with USB-Serial connection
# serial_port = '/dev/tty.usbmodem1421'

ser = serial.Serial(serial_port, serial_speed, timeout=1)

# Main Tkinter application
class Application(Frame):

	# Measure data from the sensor
	def measure(self):

		# Request data and read the answer
		data = ser.readline()

		# If the answer is not empty, process & display data
		while 1:
			processed_data = data.split(" ")

			self.ph_input_data.set("pH Input: " + str(processed_data[0]))
			self.ph_input.pack()

			self.turb_input_data.set("Turbidity Input: " + str(processed_data[1]))
			self.turb_input.pack()

			self.vol_input_data.set("Volume Input: " + str(processed_data[2]))
			self.vol_input.pack()

			self.ph_output_data.set("pH Output: " + str(processed_data[3]))
			self.ph_output.pack()

			self.turb_output_data.set("Turbidity Output: " + str(processed_data[4]))
			self.turb_output.pack()

			self.vol_output_data.set("Volume Output: " + str(processed_data[5]))
			self.vol_output.pack()

			self.temperature_data.set("Temperature: " + str(processed_data[6]))
			self.temperature.pack()

			self.soil_moisture_data.set("Soil Moisture: " + str(processed_data[7]))
			self.soil_moisture.pack()

		# Wait 1 second between each measurement
		self.after(1000,self.measure)

	# Create display elements
	def createWidgets(self):

		self.ph_input = Label(self, textvariable=self.ph_input_data, font=('Verdana', 20, 'bold'))
		self.ph_input_data.set("pH Input")
		self.ph_input.pack()

		self.turb_input = Label(self, textvariable=self.turb_input_data, font=('Verdana', 20, 'bold'))
		self.turb_input_data.set("Turbidity Input")
		self.turb_input.pack()

		self.vol_input = Label(self, textvariable=self.vol_input_data, font=('Verdana', 20, 'bold'))
		self.vol_input_data.set("Volume Input")
		self.vol_input.pack()

		self.ph_output = Label(self, textvariable=self.ph_output_data, font=('Verdana', 20, 'bold'))
		self.ph_output_data.set("pH Output")
		self.ph_output.pack()

		self.turb_output = Label(self, textvariable=self.turb_output_data, font=('Verdana', 20, 'bold'))
		self.turb_output_data.set("Turbidity Output")
		self.turb_output.pack()

		self.vol_output = Label(self, textvariable=self.vol_output_data, font=('Verdana', 20, 'bold'))
		self.vol_output_data.set("Volume Output")
		self.vol_output.pack()

		self.temperature = Label(self, textvariable=self.vol_output_data, font=('Verdana', 20, 'bold'))
		self.temperature_data.set("Temperature")
		self.temperature.pack()

		self.soil_moisture = Label(self, textvariable=self.vol_output_data, font=('Verdana', 20, 'bold'))
		self.soil_moisture_data.set("Soil Moisture")
		self.soil_moisture.pack()

	# Init the variables & start measurements
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.ph_input_data = StringVar()
		self.turb_input_data = StringVar()
		self.vol_input_data = StringVar()
		self.ph_output_data = StringVar()
		self.turb_output_data = StringVar()
		self.vol_output_data = StringVar()
		self.temperature_data = StringVar()
		self.soil_moisture_data = StringVar()
		self.createWidgets()
		self.pack()
		self.measure()

# Create and run the GUI
root = Tk()
app = Application(master=root)
app.mainloop()
