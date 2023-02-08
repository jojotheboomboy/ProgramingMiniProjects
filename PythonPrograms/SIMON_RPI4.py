###############################################
# Name: Josiah Norman 
# Date: 2/28/2021
###############################################

import RPi.GPIO as GPIO
from time import sleep
from random import randint
import pygame

DEBUG = True

pygame.init()

score = 0
switches = [18, 19, 20, 21]
leds = [17,16,13,12]
sounds = [
    pygame.mixer.Sound("sounds/one.wav"),
    pygame.mixer.Sound("sounds/two.wav"),
    pygame.mixer.Sound("sounds/three.wav"),
    pygame.mixer.Sound("sounds/four.wav")
    ]

GPIO.setmode(GPIO.BCM)
GPIO.setup(switches, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(leds, GPIO.OUT)

def all_on():
    for i in leds:
        GPIO.output(leds, True)
        
def all_off():
    for i in leds:
        GPIO.output(leds, False)
        
def lose():
    for i in range(0,4):
        all_on()
        sleep(0.5)
        all_off()
        sleep(0.5)
    print("You made it to a sequence of {}".format(len(seq)-3))

### The main sequence
seq = []

seq.append(randint(0,3))
seq.append(randint(0,3))

print("Welcome to Simon!")
print("Try to play the sequence back by pressing the switches")
print("Press the switches or Ctrl+c to exit...")


try:
    while True:      #main loop
        seq.append(randint(0,3))
        
        if DEBUG == True:
            if (len(seq) > 3):
                print("seq={}".format(seq))
                
        for s in seq:
            if (len(seq) < 5):
                GPIO.output(leds[s], True)
                sounds[s].play()
                sleep(1)
                GPIO.output(leds[s], False)
                sleep(0.5)
            elif (len(seq) >= 5) and (len(seq) < 7):
                GPIO.output(leds[s], True)
                sounds[s].play()
                sleep(0.9)
                GPIO.output(leds[s], False)
                sleep(0.4)
            elif (len(seq) >= 7) and (len(seq) < 10):
                GPIO.output(leds[s], True)
                sounds[s].play()
                sleep(0.8)
                GPIO.output(leds[s], False)
                sleep(0.3)
            elif (len(seq) >= 10) and (len(seq) < 13):
                GPIO.output(leds[s], True)
                sounds[s].play()
                sleep(0.7)
                GPIO.output(leds[s], False)
                sleep(0.25)
            elif (len(seq) >= 13) and (len(seq) < 15):
                GPIO.output(leds[s], True)
                sounds[s].play()
                sleep(0.6)
                GPIO.output(leds[s], False)
                sleep(0.15)
            elif (len(seq) > 15):
                GPIO.output(leds[s], False)
                sounds[s].play()
                sleep(0.6)
                GPIO.output(leds[s], False)
                sleep(0.15)
                

        switch_count = 0
        while switch_count < len(seq):
            pressed = False
            while not pressed:
                for i in range(len(switches)):
                    while GPIO.input(switches[i]) == True:
                        val = i
                        pressed = True
                        
                        
            GPIO.output(leds[val], True)
            sounds[val].play()
            sleep(0.25)
            GPIO.output(leds[val], False)
            sleep(0.25)
            
            if val != seq[switch_count]:
                lose()
                GPIO.cleanup()
                exit(0)
                
            switch_count += 1
    
except KeyboardInterrupt:
    GPIO.cleanup()
    print("Goodbye!")