# Collection of functions for interfacing with smart devices

# pyHS100 library for TP-Link devices
import pyHS100
from threading import Thread


bedside_light = pyHS100.SmartPlug('10.0.0.61')
sound_system = pyHS100.SmartPlug('10.0.0.62')


        state = bedside_light.is_off
