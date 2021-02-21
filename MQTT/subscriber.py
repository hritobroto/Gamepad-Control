import paho.mqtt.client as paho
import time
import sys
import datetime
import time
broker="localhost"
topic="control" 
        
def on_message(client, userdata, message):
  print("Received data is :")  
  print(str(message.payload.decode("utf-8")) ) 
  print("")
    
client= paho.Client("user")
client.on_message=on_message
   
print("connecting to broker host",broker)
client.connect(broker)
client.subscribe(topic)

while 1:
    client.loop_forever() 
