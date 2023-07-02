# NCCU宿舍網路設定工具 v1.1
# Dorm Network Setting Tool for NCCU v1.1
# Build: v1.1.20230702.py.1
# Python Version: 3.11

from os import *
print("NCCU宿舍網路設定工具 v1.1")
ip = str(input("請輸入您欲設定的ip位置:"))
link_name = str(input("請輸入您的連線名稱:"))
ip_set_command = ('netsh interface ipv4 set address name="' + link_name + '" static '+ ip + ' 255.255.255.0 140.119.194.254')
dns1_set_command = ('netsh interface ipv4 set dns name="' + link_name + '" static 140.119.1.110')
dns2_set_command = ('netsh interface ipv4 add dns name="' + link_name + '" 140.119.252.12')
ip_status = system(ip_set_command)
dns1_status = system(dns1_set_command)
dns2_status = system(dns2_set_command)

if ip_status == 0:
    print("IP設定成功")
else:
    print("IP設定失敗，請檢查網卡名稱或IP位置是否輸入正確")
if dns1_status == 0:
    print("慣用DNS伺服器設定成功")
else:
    print("慣用DNS伺服器設定失敗，請檢查網卡名稱或IP位置是否輸入正確")
if dns2_status == 0:
    print("其他DNS伺服器設定成功")
else:
    print("其他DNS伺服器設定失敗，請檢查網卡名稱或IP位置是否輸入正確")
system("Pause")