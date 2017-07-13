import os
import requests
import json
import subprocess

#list of statuses
#to add a status
    #add appropiate response to status in blinkt_display_status
    #add on webpage.py the approproate image and defining color of status
STATUSES = ['available', 'busy', 'disturbable', 'finding', 'party', 'alert', 'offline']

#list of Pi's and their respective IPs on the network
MASTER_IP = "192.168.55.116"

#files to store information
status_file = '/home/pi/Desktop/blinkt_status/data/blinkt_status' 
name_file = '/home/pi/Desktop/blinkt_status/data/blinkt_name'
ip_file = '/home/pi/Desktop/blinkt_status/data/blinkt_ips'
PROFILE_FILE = '/home/pi/Desktop/blinkt_status/data/blinkt_profiles'
#ip_file is redundant at the moment

#this is to set and get the Pi's own IP - redundant at the moment
def get_self_ip():
    #essentially "hostname -I" in terminal
    my_ip = subprocess.check_output(["hostname", "-I"])
    #subprocess returns variable in bytes --> let's convert it into a string
    string = my_ip.decode("utf-8")
    #now we have the ip without the utf-6 encoding! 
    print ("This pi's ip:" + string)
    #(you can use "print (type(variable))" to check a variable's type)
    return string
    
#where is this function used?...    
def set_ip(new_ip):
    file = open(ip_file, 'w')
    file.write(new_ip)

#get and set name
def get_name():
    if os.path.exists(name_file):
            file = open(name_file, 'r')
            name = file.readline()
            print (name)
            return name
    else:
        return "no-name"
    
def set_name(new_name):
    print ("Setting new name!")
    file = open(name_file, 'w')
    file.write(new_name)
    file.close()
    url = "http://" + MASTER_IP + ":5000/register"
    info = get_status() + ',' + new_name
    r = requests.post(url, json=info, timeout=2)
    r
    print ("sent new name!")
    return "Hey"


#get and set status
def change_status(new_status):
    #change the content of the file 'Blinkt_Status'
    status = open(status_file,'w')
    status.write(new_status)
    status.close()
    url = "http://" + MASTER_IP + ":5000/register"
    info = new_status + ','  + get_name()
    print("Grrrr!!")
    requests.post(url, json=info, timeout=5)
    print("Nope?")
    
    print ("sent new status!")
    
def get_status():
    file = open(status_file,'r')
    status = file.readline()
    if status is "":
       status = "available"
    return status

get_self_ip()
