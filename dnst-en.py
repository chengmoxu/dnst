# Dorm Network Setting Tool for NCCU (English) v1.1
# Build: v1.1.20231117.py.1
# Python Version: 3.12

from os import *
print("Dorm Network Setting Tool for NCCU (English) v1.1")
ip = str(input("Please enter your IP address from NCCU Computer Center:"))
link_name = str(input("Please enter your Internet name:"))
ip_set_command = ('netsh interface ipv4 set address name="' + link_name + '" static '+ ip + ' 255.255.255.0 140.119.194.254')
dns1_set_command = ('netsh interface ipv4 set dns name="' + link_name + '" static 140.119.1.110')
dns2_set_command = ('netsh interface ipv4 add dns name="' + link_name + '" 140.119.252.12')
ip_status = system(ip_set_command)
dns1_status = system(dns1_set_command)
dns2_status = system(dns2_set_command)

if ip_status == 0:
    print("IP setting successful")
else:
    print("IP setting failed, please check whether the network card name or IP address is entered correctly")
if dns1_status == 0:
    print("DNS setting successful")
else:
    print("DNS setting failed, please check whether the network card name or IP address is entered correctly")
if dns2_status == 0:
    print("Add DNS setting successful")
else:
    print("Add DNS setting failed, please check whether the network card name or IP address is entered correctly")
system("Pause")