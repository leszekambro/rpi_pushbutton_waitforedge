#!/usr/bin/python
import RPi.GPIO as GPIO 
import time

kanal = 23
GPIO.setmode(GPIO.BCM)  
GPIO.setup(kanal, GPIO.IN, pull_up_down=GPIO.PUD_UP)  

print("***")
print("Pkt testowy 1")
print("***")

channel = GPIO.wait_for_edge(kanal, GPIO.FALLING, timeout=5000)

if channel is None:
    print("Timeout, koniec programu")
    GPIO.cleanup()
else:
    print("Zbocze wykryte na kanale", kanal)
    print("Koniec programu za 2 sec")
    time.sleep(2)
    GPIO.cleanup()