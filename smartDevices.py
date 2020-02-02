# Collection of functions for interfacing with smart devices

# pyHS100 library for TP-Link devices
import pyHS100
from threading import Thread

# Initialise smart device objects
bedside_light = pyHS100.SmartPlug('10.0.0.61')
sound_system = pyHS100.SmartPlug('10.0.0.62')

# Dictionary storing states
smart_device_states = {
    bedside_light : False,
    sound_system : False
}

# Body head and tail
body_head = (b'<body bgcolor=white>' +
             b'<p>Basic control of network connected devices</p>')
body_tail = b'</body>'



'''
function to return a dictionary with the states of the smart devices
'''
def getDeviceStates():
    smart_device_states['bedside_light'] = bedside_light.is_on
    smart_device_states['sound_system'] = sound_system.is_on
    return smart_device_states


    
'''
change light state
'''
def switchLightState():
    pass



'''
Generate the body of the index page
'''
def genIndexBody():
    # Make sure device states are accurate
    getDeviceStates()

    # Select light image as appropriate
    if smart_device_states['bedside_light'] == True:
        light_image = 'light_on.png'
    else:
        light_image = 'light_off.png'

    # Select sound system image as appropriate
    if smart_device_states['sound_system'] == True:
        sound_system_image = 'ss_on.png'
    else:
        sound_system_image = 'ss_off.png'

    
        
