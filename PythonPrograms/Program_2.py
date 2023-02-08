
################################################################################
# Name: Josiah Norman
# Date: 10/5/2020
# Description: This Program will replicate the results of the intial program
################################################################################
def callName():
    name = input("Please enter your name ")
    return name

def callScore1():
    scoreA = int(input("What was your first score? "))
    return scoreA

def callScore2():
    scoreB = int(input("What was your second score? "))
    return scoreB

def callAverage():
    Average = (scoreA + scoreB) / 2
    return Average
    
def output(name, Average):
    print ("Hi, {}.  Your Average score is {} " .format (name, Average))
    

name = callName()

scoreA = callScore1()
scoreB = callScore2()

Average = callAverage()
output(name, Average)
