"""
The magic8ball class: This class will create an ascii object of magic 8 ball and handle the movements and behaviours alongside with the random responses
The quantumrandom library was chosen to create true random numbers for a more intresting result...!
This class requires the responsesDect file to operate properly; the file must contain all of the responses without anything extra... The responses could be changed. This is 
to simply make this whole program more modular and customizable...
"""

import quantumrandom
import os
from os import system, name
import re
from colorPrint import *

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

def clearConsole():
  
        # for windows
        if name == 'nt':
            _ = system('cls')
    
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')

class magic8Ball:
    def __init__(self, r=0, x=0, y=0):
        # self.radius = r # for future refrence, I may make a new one with a sizable ball!
        self.responsDect = open(os.path.join(__location__,'responsesDect'), 'r').read().split('\n') # get all of the responses
        # self.x = x
        # self.y = y
        self.frames = open(os.path.join(__location__,'ballFrames'), 'r').read().split('+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+')  # get all of the frames
    
    

    def resetBall(self):
        clearConsole()
        print('\n\n')
        printColor(self.frames[0], colors[random.randint(0, len(colors) - 1)])


    def generateResponse(self):

        response =  self.responsDect[quantumrandom.get_data()[0] % len(self.responsDect)] # generate a truly random response 
        newFrame = list(self.frames[1])

        if len(response) < 15: # if the response length is smaller than first line then center it
            response = response.center(14, ' ')

        response = list(response)  # convert into list to allow for in-place assignment

        for i in range(len(newFrame)):

                if newFrame[i] == 'W': # regex pattern is 'W'
                    if len(response) > 0:
                        newFrame[i] = response.pop(0)
                    else: # replace rest of the W's with white space
                        newFrame[i] = ' '


        clearConsole()
        strOut = ''
        printColor(strOut.join(newFrame), colors[random.randint(0, len(colors) - 1)]) # join newFrame to gether as one string and print in color

