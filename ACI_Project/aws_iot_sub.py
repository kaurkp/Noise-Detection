#!/usr/bin/python

############################################ 
# PROBLEM STATEMENT:
#
# This program will subscribe and show all the messages sent by its companion 
# aws_iot_pub.py using AWS IoT hub
#
############################################

############################################
# STEPS:
#
# 1. Sign in to AWS Amazon > Services > AWS IoT > Settings > copy Endpoint
#    This is your awshost
# 
# 2. Change following things in the below program:
#    a. awshost   (from step 1)
#    b. clientId  (Thing_Name)
#    c. thingName (Thing_Name)
#    d. caPath    (root-CA_certificate_Name)
#    e. certPath  (<Thing_Name>.cert.pem)
#    f. keyPath   (<Thing_Name>.private.key)
# 
# 3. Paste aws_iot_pub.py & aws_iot_sub.py python scripts in folder where all unzipped aws files are kept. 
# 4. Provide Executable permition for both the python scripts.
# 5. Run aws_iot_sub.py script
# 6. Run this aws_iot_pub.py python script
#
############################################

# importing libraries
import paho.mqtt.client as paho
import os
import socket
import ssl
 
def on_connect(client, userdata, flags, rc):                # func for making connection
    print("Connection returned result: " + str(rc) )
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("#" , 1 )                              # Subscribe to all topics
 
def on_message(client, userdata, msg):                      # Func for receiving msgs
    print("topic: "+msg.topic)
    print("payload: "+str(msg.payload))
 
#def on_log(client, userdata, level, msg):
#    print(msg.topic+" "+str(msg.payload))
 
mqttc = paho.Client()                                       # mqttc object
mqttc.on_connect = on_connect                               # assign on_connect func
mqttc.on_message = on_message                               # assign on_message func
#mqttc.on_log = on_log

#### Change following parameters for RPi 1 ####  
awshost = "a1kudj94y1eid7-ats.iot.us-east-1.amazonaws.com"      # Endpoint
awsport = 8883                                              # Port no.   
clientId = "aws_thing1"                                     # Thing_Name
thingName = "aws_thing1"                                    # Thing_Name
caPath = "root-CA_1.crt"                                      # Root_CA_Certificate_Name
certPath = "aws_thing1.cert.pem"                            # <Thing_Name>.cert.pem
keyPath = "aws_thing1.private.key"                          # <Thing_Name>.private.key
 

#### Change following parameters for RPi 2 ####  
awshost = "a1kudj94y1eid7-ats.iot.us-east-1.amazonaws.com"      # Endpoint
awsport = 8883                                              # Port no.   
clientId = "aws_thing2"                                     # Thing_Name
thingName = "aws_thing2"                                    # Thing_Name
caPath = "root-CA_2.crt"                                      # Root_CA_Certificate_Name
certPath = "aws_thing2.cert.pem"                            # <Thing_Name>.cert.pem
keyPath = "aws_thing2.private.key"                          # <Thing_Name>.private.key
 
#### Change following parameters for RPi 3 ####  
awshost = "a1kudj94y1eid7-ats.iot.us-east-1.amazonaws.com"      # Endpoint
awsport = 8883                                              # Port no.   
clientId = "aws_thing3"                                     # Thing_Name
thingName = "aws_thing3"                                    # Thing_Name
caPath = "root-CA_3.crt"                                      # Root_CA_Certificate_Name
certPath = "aws_thing3.cert.pem"                            # <Thing_Name>.cert.pem
keyPath = "aws_thing3.private.key"                          # <Thing_Name>.private.key
  
 
mqttc.tls_set(caPath, certfile=certPath, keyfile=keyPath, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)      # pass parameters
 
mqttc.connect(awshost, awsport, keepalive=60)               # connect to aws server
 
mqttc.loop_forever()                                        # Start receiving in loop
