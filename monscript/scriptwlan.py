
# Import module 
from scapy.all import *
  
# Make an variable interface and assign  
# this name of wlan connection name "my-Wlan" 
interface = "my_Wlan"
  
# This will be sender's MAC address  
# This is there random MAC address generated 
sender = RandMAC() 
  
# Assign access point name 
access_point_name = "Test"
  
# Here we will define 802.11 frame 
dot11 = Dot11(type=0, subtype=8,  
              addr1="ff:ff:ff:ff:ff:ff", 
              addr2=sender, addr3=sender) 
beacon = Dot11Beacon() 
  
# Assign ssid in frame 
e_SSID = Dot11Elt(ID="SSID", info=access_point_name, 
                  len=len(access_point_name)) 
  
# stack all the layers and add a RadioTap  
frame = RadioTap()/dot11/beacon/e_SSID 
  
# Send the frame in layer 2 every 100 milliseconds  
# using the iface interface 
sendp(frame, inter=0.1, iface=interface, loop=1) 

