######################################################################
# author: Josiah Norman
# date: 2/4/2021
# desc: Making use of one massive function that I built. This program should output a calculation similar to the given one on the PDF.
#####################################################################
#BEGIN

from random import randint, choice

DEBUG = False

# Setting "formating" equal to a print statement I will use throughout the program 
formating = ("=" * 60)

print("Simulation Set Up: ")
print(formating)

# This section of the program will take a user's input as an integer value and return it to the equivalent value.
QBank = int(input("What is the size of the question bank? "))
StudiedBank = int(input("How many of theose questions have you studied? "))
TestQS = int(input("How many questions does the test have? "))
PassingGD = int(input("How many questions must you answer correctly to pass the test? "))

print(formating)

NSim = int(input("How many simulations do you want to run? "))

print(formating)
print(formating)

# This is the function that will essentially do everything as far as calculations go.
# I pass the declared variables into my function.
def sucessEvaluation (QBank, StudiedBank, TestQS, PassingGD, NSim):
    SimCounter = 0
    totalCorrect = 0
    passedScore = []
    
    # This part makes certain that the SimCounter repeats the correct amount of times.
    while (SimCounter < NSim):
        correctIntersection = 0
        QBlist = []
        CopyQBlist = []
        SBlist = []
        TQlist = []
        GradeTracker = []
        simScore = []

        # This will append numbers 1-100 to both QBlist and CopyQBlist.
        for i in range(QBank):
            QBlist.append(i+1)
            CopyQBlist.append(i+1)
            
        # This part makes certain that SBlist is filled with the appropriate number of elements.
        # It also removes that element from QBlist so that it won't continue to check for that element.
        while (len(SBlist) <= (StudiedBank-1)):
            selection = choice(QBlist)
            QBlist.remove(selection)
            SBlist.append(selection)

        # This part is essentially identical to the previous one with the addition that CopyQBlist is being used.
        while (len(TQlist) < TestQS):
            selection = choice(CopyQBlist)
            CopyQBlist.remove(selection)
            TQlist.append(selection)

        # This section checks each index within the lists and relates them to eachother. if the values do match-
        # Than the following code executes if, if the values do not match then the program will continue in the loop.
        for i in range(len(SBlist)):
            n = SBlist[i]
            for j in range(len(TQlist)):
                m = TQlist[j]
                if (n == m):
                    simScore.append(n)
                    correctIntersection = (correctIntersection + 1)
                    GradeTracker.append(correctIntersection)
                    if (len(GradeTracker) >= PassingGD):
                        Passed = 1
                    else:
                        Passed = 0
        passedScore.append(len(GradeTracker))

        # This last section makes use of the True and False as instructions. If Debug is set to False none of this will run.
        if DEBUG == True:
            print("Simulation No. {}".format(SimCounter + 1))
            print("Questions you were asked: {}".format(TQlist))
            print("Question you studied: {}".format(SBlist))
            print("Question you passed: {}".format(simScore))
            print("Which means you scored {}/{}".format(len(GradeTracker),TestQS))
            print("-" * 60)
        totalCorrect += Passed
        SimCounter = (SimCounter + 1)
    if DEBUG == True:
        print("Simulation scores were: {}".format(passedScore))
    return (totalCorrect/SimCounter)

# Final print that uses the returned value of our function to print.
print("You passed the exam {}% of the time".format(sucessEvaluation (QBank, StudiedBank, TestQS, PassingGD, NSim) * 100))            

# END
