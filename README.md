# Gamepad-Control
Contains python codes to map a controller 

To run the code go to Command Prompt(cmd) in Windows and run the following:
###### pip install inputs

* Basic- All button mapping 
* Version 1.0- Direction and speed control
________________________________________________________________________

## Connecting to the Raspberry Pi
Updating Raspberry Pi:
###### apt-get update && apt-get upgrade -y

* For bluetooth controllers: 
  sudo bluetoothctl
  ###### power on
  ###### agent on
  ###### default-agent

  The bluetoothctl will keep the bluetooth device talking to Linux.
  ###### scan on
  This gives a list of the avaiable devices
  ###### pair XX:XX:XX:XX:XX:XX
  This is the format for pairing the device with the device ID.

* For USB Controllers:
  <br /> Just plug in the USB cable
_________________________________________________________________________

### Communication
Turn off/unplug the device and use
###### ls /dev/input
Then reconnect/plug the device back in and run the command again.
This gives the new device that is being added. For eg, Device1
Now to test out out the incoming data from the device:
###### cat /dev/input/Device1
if this gives an output it means the device is connected and it is communicating with the Raspberry Pi.
__________________________________________________________________________

### Test communication with EVDEV
First, lets install EVDEV
###### sudo apt-get install python-dev
###### sudo apt-get install python-pip
###### sudo pip install evdev
__________________________________________________________________________

### Mapping controller:
* EVDEV
<br /> Parts: ecode type, event code, event value.
* Inputs
<br /> Parts: event type, event code, event state.
___________________________________________________________________________


##### NB: 
* The error when the controller is removed abruptly is not yet corrected.
* Bold fields are executable terminal commands.






