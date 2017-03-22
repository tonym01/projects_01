#!/usr/bin/env python

from gpiozero import Button, PWMLED
from time import sleep, time
from os import system

#----- Initialisation ------

# define the pins for the shutdown button and pulsing led
btn1 = Button(12) 
led1 = PWMLED(25)
led1_fadein = 3
led1_fadeout = 1.5

hold_time = 3.0

#----- functions ------

def shut_down():
    led1.pulse(led1_fadein, led1_fadeout)
    system("sudo shutdown -h now")
    sleep(40) # should take no more than 40 secs to shutdown

#----- start of main logic------

while True:

    led1.on()
    btn1.wait_for_press()
    led1.blink(0.2, 0.2)
    start_time = time()
    
    while btn1.value == True:
        sleep(0.1)
        duration = time() - start_time
        if duration > hold_time:
            shut_down()

#----- end of main logic -----
