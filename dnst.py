# NCCU宿舍網路設定工具 v2.0
# Dorm Network Setting Tool for NCCU v2.0
# Build: v2.0.20240701.py.1
# Python Version: 3.12.2

import os

print ("NCCU宿舍網路設定工具 v2.0")
link_name = str (input ("請輸入您的連線名稱:"))
ip = str (input ("請輸入您欲設定的IP位置:"))
default_gateway = str (input ("請輸入系統顯示的預設閘道IP位置:"))
ip_set_command = ('netsh interface ipv4 set address name="' + link_name + '" static '+ ip + ' 255.255.255.0 ' + default_gateway)
dns1_set_command = ('netsh interface ipv4 set dns name="' + link_name + '" static 140.119.1.110')
dns2_set_command = ('netsh interface ipv4 add dns name="' + link_name + '" 140.119.252.12')
ip_status = os.system (ip_set_command)
dns1_status = os.system (dns1_set_command)
dns2_status = os.system (dns2_set_command)

if ip_status == 0:
    print ("IP設定成功")
else:
    print ("IP設定失敗，請檢查網卡名稱或IP位置是否輸入正確")
if dns1_status == 0:
    print ("慣用DNS伺服器設定成功")
else:
    print ("慣用DNS伺服器設定失敗，請檢查網卡名稱或IP位置是否輸入正確")
if dns2_status == 0:
    print ("其他DNS伺服器設定成功")
else:
    print ("其他DNS伺服器設定失敗，請檢查網卡名稱或IP位置是否輸入正確")
os.system ("Pause")