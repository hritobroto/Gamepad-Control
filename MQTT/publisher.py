import paho.mqtt.client as paho 
import os
import json
import time
from datetime import datetime
import inputs

broker="localhost" 
topic="control";
port=1883 
ACCESS_TOKEN='M7OFDCmemyKoi461BJ4j' 


def on_publish(client,userdata,result): 
    print("published data is : ")
    pass

client1= paho.Client("control") 
client1.on_publish = on_publish 
client1.username_pw_set(ACCESS_TOKEN) 
client1.connect(broker,port,keepalive=60) 
x=0;

while True:
    if(len(inputs.devices.gamepads) == 0): 
        print("Please connect controller!")
    else:
        try:
            events = inputs.get_gamepad()  
            for event in events:
                x=0
                if(event.code == 'BTN_SOUTH' and event.state == 1):
                    payload="A"
                if(event.code == 'BTN_NORTH' and event.state == 1):
                    payload="Y"
                if(event.code == 'BTN_WEST' and event.state == 1):
                    payload="X"
                if(event.code == 'BTN_EAST' and event.state == 1):
                    payload="B"

                
                if(event.code == 'ABS_RY' and event.state > 0):
                    payload="UP"
                if(event.code == 'ABS_RY' and event.state < 0):
                    payload="DOWN"
                if(event.code == 'ABS_RX' and event.state > 0):
                    payload="RIGHT"
                if(event.code == 'ABS_RX' and event.state < 0):
                    payload="LEFT"

                if(event.code == 'BTN_START' and event.state == 1):
                    payload="SELECT"
                if(event.code == 'BTN_SELECT' and event.state == 1):
                    payload="START"

                ret= client1.publish(topic,payload) 
                print(payload);
        except:
            if(x==0):
                    print("Please connect controller!")
                    x+=1
    #time.sleep(0.25)
