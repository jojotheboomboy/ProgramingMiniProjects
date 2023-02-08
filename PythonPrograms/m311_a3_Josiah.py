####################################################################################################################################
# Names: Josiah Norman, Christian Smith 
# Date: 4/14/2022
# Big(O): cubic O(n^3)
# Equation: Y = 0.1667x^3 + 0.5x^2 + 0.3333x - 2E-09
# Course: MATH311-002, Spring22, Assignment 3
# Work Delegation: This implementation was written by Josiah and a similar one was written by Christian in Rust. (See other file)
# Definition of an Operation: An operation is when an accumulator is modified directly or when the current maximum sum is updated to a new value.
####################################################################################################################################

from random import randint

def sub_array_generator(array):                                     #function will generate arrays, via slicing, which will be passed into the max Calculator
    length = len(array)
    (max, ops) = maxCalculator(array, 0)                            # max is defined to be an accumulator
    for j in range (1, len(array)):
        for i in range(length):
            (max, new_ops) = maxCalculator(array[i:i+j], max)
            ops += (new_ops)
        length-=1
    return (max, ops)

def maxCalculator(array, max):
    curr = 0                                                        # curr is defined to be an accumulator
    for i in range(len(array)):
        curr += array[i]                                            # Directly modifying the accumulator curr
    if (curr > max):
        return (curr, 1+len(array))                                 # This will cause max accumulator to be updated
    else:
        return (max, len(array))

def printer(size, ops): 
    print("{}                               {}".format(size, int(ops)))

format = 'size\t\t\t\tAvg # of Ops'                                 # padding format
print(format)
size = 5                                                            # initial array size
sample_size  = 2500                                                 # amount of arrays that will be generated 
iterations = 11                                                     # amount of times array will increment 
incrementation = 5                                                  # amount the array will increment by

for i in range(iterations):                                         # Main 
    ops = 0                                                         # Operation counter
    total = 0           
    for j in range(sample_size):
        array = [None] * size                                       # Generates array of given size
        for k in range(size):
            array[k] = randint(-10,99)                              # Random generation for a given index
        (curr_sum, curr_ops) = sub_array_generator(array)
        total += curr_sum
        ops += curr_ops
    printer(size, ops/sample_size)
    size += incrementation
