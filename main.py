#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time

reader = SimpleMFRC522()
OldText = ''

while True:
   # GPIO.cleanup()
    time.sleep(1)
    try:
        status,TagType = reader.read_no_block()
        print(status)
        if status == None:
            print ("No Card Found")
        elif status != None:
            id,text = reader.read()
            if text != OldText:
                print(text)
                OldText=text

            else:
                print ("Same card")

    finally:
        print('ok')
    time.sleep(5) 