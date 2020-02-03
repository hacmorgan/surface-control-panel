# Collection of functions for interfacing with smart devices

# pyHS100 library for TP-Link devices
import pyHS100
from threading import Thread

# Initialise smart device objects
bedside_light = pyHS100.SmartPlug('10.0.0.61')
sound_system = pyHS100.SmartPlug('10.0.0.62')

# Dictionary storing states - True = on
smart_device_states = {
    bedside_light : False,
    sound_system : False
}

# Body head and tail
body_head = (b'<body bgcolor=white>' +
             b'<p>Basic control of network connected devices</p>')
body_tail = b'</body>'

# HTML link syntax repeatable parts
link_0 = b'<a href="'
link_1 = b'"><img src="'
link_2 = b'" style="width:200px;height:120px;border:0;"></a>'



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

    # Assign on and off images for light
    if smart_device_states['bedside_light'] == True:
        light_on_image = b'active_on.png'
        light_off_image = b'inactive_off.png'
    else:
        light_on_image = b'inactive_on.png'
        light_off_image = b'active_off.png'

    # Assign on and off images for sound system 
    if smart_device_states['sound_system'] == True:
        sound_system_on_image = b'active_on.png'
        sound_system_off_image = b'inactive_off.png'
    else:
        sound_system_on_image = b'inactive_on.png'
        sound_system_off_image = b'active_off.png'

    # Build up the response
    response = body_head

    response += b'<h2> Bedside Light<p>'
    response += link_0 + b'SDC_light_on' + link_1 + light_on_image + link_2
    response += link_0 + b'SDC_light_off' + link_1 + light_off_image + link_2
    response += b'</p><h2> Sound System<p>'
    response += link_0 + b'SDC_sound_system_on' + link_1 + sound_system_on_image + link_2
    response += link_0 + b'SDC_sound_system_off' + link_1 + sound_system_off_image + link_2
    response += b'</p>'

    response += body_tail

    return response


    
        
# This function returns True if the device will now be switched on
def smartDeviceControl(message):
    if message == 'light_on':
        bedside_light.turn_on()
    elif message == 'light_off':
        bedside_light.turn_off()
    elif message == 'sound_system_on':
        sound_system.turn_on()
    elif message == 'sound_system_off':
        sound_system.turn_off()
    
