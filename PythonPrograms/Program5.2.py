
minimum = -1
minimum = int(input("Minimum number of the list"))

while (minimum < 0):
    minimum = int(input("ERROR: Minimum number of the list must be a postive number"))

maximum = 1
maximum = int(input("Maximum number of the list"))

while (maximum < minimum):
    maximum = int(input("ERROR: Maximum must be greater than the minimum"))

