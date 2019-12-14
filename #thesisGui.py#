# Imports
import tkinter
from tkinter import messagebox
import numpy as np
import SharedArray as sa
import os




# Callback functions
def checkInputs():
    os.system('bash /home/hamish/Documents/thesis/final/checkInputs')
    global status
    status[0] = 1
def calibStartCallBack():
    global status
    if status[4] == 1:
        messagebox.showinfo("Error", "Please stop live calculation before commencing calibration")
    else:
        status[3] = 1
def calibStopCallBack():
    global status
    status[3] = 0
def liveStartCallBack():
    global status
    if status[3] == 1:
        messagebox.showinfo("Error", "Please stop calibration before commencing live calculation")
    else:
        status[4] = 1
def liveStopCallBack():
    global status
    status[4] = 0
def setAngle(angle):
    global status
    status[1] = angle
def setHSV(angle):
    global status
    status[6] = angle
def haltExecution():
    global status
    global window
    status[5] = 1
    window.destroy()


def createGui():
    # Attach to shared memory blocks
    global status
    status = sa.attach('status')
    # laser_data = sa.attach('laser_data')
    # rgb_image = sa.attach('rgb_control')

    # Make a window
    global window
    window = tkinter.Tk()

    # Add buttons
    test_inputs = tkinter.Button(window, text = "Run input checking script", command = checkInputs, padx = 20, pady = 10, bg = 'magenta')
    calib_start = tkinter.Button(window, text = "Start Calibration", command = calibStartCallBack, padx = 40, pady = 20, bg = 'green')
    calib_stop = tkinter.Button(window, text = "Stop Calibration", command = calibStopCallBack, padx = 40, pady = 20, bg = 'red')
    live_start = tkinter.Button(window, text = "Start Live Algorithm", command = liveStartCallBack, padx = 40, pady = 20, bg = 'green')
    live_stop = tkinter.Button(window, text = "Stop Live Algorithm", command = liveStopCallBack, padx = 40, pady = 20, bg = 'red')
    start_angle_slider = tkinter.Scale(window, from_=-20, to=20, orient=tkinter.HORIZONTAL, length=600, width = 30, bg = 'cyan')
    set_angle = tkinter.Button(window, text = "Set start angle from slider", command = lambda : setAngle(start_angle_slider.get()), padx = 20, pady = 10, bg = 'cyan')
    hsv_cutoff_slider = tkinter.Scale(window, from_=15, to=50, orient=tkinter.HORIZONTAL, length=600, width = 30, bg = 'blue')
    hsv_cutoff_slider.set(28)
    set_hsv = tkinter.Button(window, text = "Set HSV cutoff angle from slider", command = lambda : setHSV(hsv_cutoff_slider.get()), padx = 20, pady = 10, bg = 'blue')
    
    halt_execution = tkinter.Button(window, text = "QUIT", command = haltExecution, padx = 60, pady = 30, bg = 'orange')
    start_angle_slider.set(0)
    
    # Set positions
    test_inputs.grid(row = 0, column = 0, columnspan = 2)
    calib_start.grid(row = 1, column = 0)
    calib_stop.grid(row = 1, column = 1)
    live_start.grid(row = 2, column = 0)
    live_stop.grid(row = 2, column = 1)
    start_angle_slider.grid(row = 3, column = 0, columnspan = 2)
    set_angle.grid(row = 4, column = 0, columnspan = 2)
    hsv_cutoff_slider.grid(row = 5, column = 0, columnspan = 2)
    set_hsv.grid(row = 6, column = 0, columnspan = 2)
    halt_execution.grid(row = 7, column = 0, columnspan = 2)

    # Make everything expand
    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=1)
    window.grid_rowconfigure(0, weight=1)
    window.grid_rowconfigure(1, weight=2)
    window.grid_rowconfigure(2, weight=2)
    window.grid_rowconfigure(3, weight=1)
    window.grid_rowconfigure(4, weight=2)
    window.grid_rowconfigure(5, weight=1)
    window.grid_rowconfigure(6, weight=2)
    window.grid_rowconfigure(7, weight=3)    

    window.mainloop()

createGui()