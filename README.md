# Gamepad-Control

* Basic- All button mapping 
* Version 1.0- Direction and speed control
* Version 2.0- Exception handling
________________________________________________________________________

### Connecting to the Raspberry Pi
Updating Raspberry Pi:
``` diff
apt-get update && apt-get upgrade -y
```

* For bluetooth controllers: 
  ``` diff
  sudo bluetoothctl
  power on
  agent on
  default-agent
  ```
  The bluetoothctl will keep the bluetooth device talking to Linux.
  ``` diff
  scan on
  ```
  This gives a list of the avaiable devices
  ``` diff
  pair XX:XX:XX:XX:XX:XX
  ```
  This is the format for pairing the device with the device ID.

* For USB Controllers:
  <br /> Just plug in the USB cable
_________________________________________________________________________

### Communication
Turn off/unplug the device and use
``` diff
ls /dev/input
```
Then reconnect/plug the device back in and run the command again.
This gives the new device that is being added. For eg, Device1
<br /> Now to test out out the incoming data from the device:
``` diff
cat /dev/input/Device1
```
if this gives an output it means the device is connected and it is communicating with the Raspberry Pi.
__________________________________________________________________________

### Test communication with EVDEV
First, lets install EVDEV
``` diff
sudo apt-get install python-dev
sudo apt-get install python-pip
sudo pip install evdev
```
__________________________________________________________________________

### Test communication with INPUTS
First, lets install input
``` diff
pip install inputs
```
or
``` diff
git clone https://github.com/zeth/inputs.git
cd inputs
python setup.py install
```
or 
just download inputs.py
__________________________________________________________________________

### Mapping controller:
* EVDEV
<br /> Parts: ecode type, event code, event value.
* Inputs
<br /> Parts: event type, event code, event state.
___________________________________________________________________________

### Installing Mosquitto
``` diff
sudo apt install -y mosquitto mosquitto-clients
mosquitto -v
```
### Installing Flask
``` diff
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python-pip python-flask
pi@raspberrypi ~ $ sudo pip install flask
```
### Installing Paho-MQTT
``` diff
sudo pip install paho-mqtt
```
___________________________________________________________________________




##### NB: 
* Highlighted fields are executable terminal commands.
* Flask as backup if controller fails





