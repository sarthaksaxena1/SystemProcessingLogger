#!/usr/bin/python
# -*- coding: utf-8 -*-
import subprocess
import time
import os
logn = 1
def CP():
   with open('olog.txt') as f:
      with open('log.txt', 'a+') as f1:
        for line in f:
         f1.write(line)
def start():	
 subprocess.call('tasklist >olog.txt', shell=True)
 CP()
 f2=open('log.txt','a+')
 f2.write("The File Is Logged "+str(logn)+" Time \n")
 time.sleep(3)
while True :
 logn=logn+1
 start()
