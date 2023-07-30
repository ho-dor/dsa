from os import *
from sys import *
from collections import *
from math import *

def findSecondLargest(sequenceOfNumbers):
    # Write your code here.
    if len(sequenceOfNumbers) < 2:
        return -1
    current = []
    if sequenceOfNumbers[0] < sequenceOfNumbers[1]:
        current = [sequenceOfNumbers[1], sequenceOfNumbers[0]]
    else:
        current = [sequenceOfNumbers[0], sequenceOfNumbers[1]]
    
    for i in range(2, len(sequenceOfNumbers)):
        if sequenceOfNumbers[i] > current[0]:
            temp = current[0]
            current[0] = sequenceOfNumbers[i]
            current[1] = temp

        elif sequenceOfNumbers[i] > current[1] and sequenceOfNumbers[i] != current[0]:
            current[1] = sequenceOfNumbers[i]
    
    return current[1] if current[1] != current[0] else -1
