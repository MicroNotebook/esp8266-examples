from network import WLAN 
from mqtt import MQTTClient 
import machine 
import time 
 
def sub_cb(topic, msg): 
   print(msg) 
 
client = MQTTClient("device_id", "10.0.0.80", port=1883) 
client.set_callback(sub_cb) 
client.connect()
#client.subscribe(topic="youraccount/feeds/lights") 
while True: 
    #print("Sending ON") 
    client.publish(topic="youraccount/feeds/lights", msg="poop")
    time.sleep(5) 
    #print("Sending OFF") 
    #client.publish(topic="youraccount/feeds/lights", msg="OFF")
    
    #time.sleep(1)