import RPi.GPIO as GPIO
from time import sleep
from random import randint

gpio = [17,18,27,22,26,6,16,20,21]

def setGPIO():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(gpio,GPIO.OUT)

def allon():
    GPIO.output(gpio, GPIO.HIGH)
    sleep(3)
    GPIO.output(gpio, GPIO.LOW)

def setNum():
    num = []
    for i in range (0, 8):
        num.append(randint(0,1))
    return num

def display():
    for i in range(len(sum)):
        if (sum[i] == 1):
            GPIO.output(gpio[i], GPIO.HIGH)
        else:
            GPIO.output(gpio[i], GPIO.LOW)

def fullAdder(Cin, A, B):
    S = Cin ^ (A ^ B)
    Cout = (A & B) | (Cin & (A ^ B))
    return S, Cout

def calculate(num1, num2):
    Cout = 0
    sum = []
    n = len(num1) - 1
    while (n >= 0):
        A = num1[n]
        B = num2[n]
        Cin = Cout
        S, Cout = fullAdder(Cin, A, B)
        sum.insert(0, S)
        n -= 1
    sum.insert(0, Cout)
    return sum

#MAIN Program
setGPIO()       # setup GPIO
allon()         # indicate our circut works

num1 = setNum()         #Randomly create an 8-bit value
print("     ", num1)    #print value

num2 = setNum()
print("+    ", num2)    #Randomly create an 8-bit value and print.

sum = calculate(num1, num2)     # find the sum of the two values
print("=    ", sum)

display()                       #Make the LEDs display the number

input("Press ENTER to terminate")   #terminate when ready
GPIO.cleanup()
