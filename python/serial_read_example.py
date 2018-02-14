#!/usr/bin/env python
import serial
import turtle
import sys
import time
import threading
import Tkinter
from Tkinter import *
import ttk

f = open('/Users/tempfile.txt', 'w')
s = serial.Serial(port='/dev/tty.usbserial-AH01A6MB', baudrate=9600)
told=1
n=1
num=1
class gui(object):
    def _init_(self):
        self.root = Tk()
        self.root.title("Python Serial Monitor Test Window")
        self.root.geometry("600x500+500+200")
        self.mylabel =Tkinter.Label(self.root,text= "Serial Monitor")
        self.quitButton = Tkinter.Button(self.root,text="Exit",command=self.exodou)
        self.nl= Label (self.root,text="egine")
        self.nl.config(font=("arial",80),fg="green")
        self.pb = ttk.Progressbar(self.root,)
        self.datelabel = Tkinter.Label(self.root,text= "__________")
        self.updateGui()
        self.readsensor()
        self.read()
    
    def exodou(self): # routina koumpiou exit
        n=0
        
        f.close()
        sys.exit(15)
        
        
    def updateGui(self): # routina koumpiou start serial monitor
        self.root.update()
        self.root.after(1000, self.updateGui)
        
    def readsensor(self):
        
        self.root.update()
        self.nl.after(100, self.readsensor)
    
    def run(self):
        self.mylabel.pack() 
        self.nl.pack()
        self.pb.pack()
        self.datelabel.pack()
        self.quitButton.pack()
        self.nl.after(1000, self.updateGui)
        self.root.mainloop()
        
    def read(self):
        global told
        num=1
        n=1
        aa="aa"
        aa = s.readline()
        
        
        if aa[0:4]== "Data":
            num=aa[6:11]
            num=float(num) 
            format (num, '.1f')
            #print("%.1f" % num),
            if told>num:
                self.nl.config(fg="blue")
                
                #print ("Temp Down")
            if told<num:
                self.nl.config(fg="red")
                #print ("Temp Up")
                #told=num
            if told==num:
                self.nl.config(fg="green")
                #print ("")
        #else:
            #print("Connection Lost")
            told=num
        self.nl.config(text=num)
        snum = str(num)
        ddate = time.asctime( time.localtime(time.time()) )
        
        self.datelabel.config(text = ddate)
        f.writelines(' ' + snum + ' ' + ddate + chr(10))
        f.flush() 
        self.root.after(1000, self.read)
    
    
if _name_ == "__main__":
    
    gui().run()
