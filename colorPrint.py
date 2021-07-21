"""
Color print library: Used to print text to console with colors or text effects. Also hanles different OS's and consoles...
"""


import random
import time, sys
from os import system, name 

print = sys.stdout.write # overwriting print function for better performance!

if 'idlelib.run' in sys.modules: # python IDLE also, does not support ascii codes :(.... so act like its windows
    name = 'nt'

 # ----------< All colors >----------

_Reset = '\u001b[0m' if name != 'nt' else '' # for windows no Ascii command is supported
_Black='\033[30m'
_Red='\033[31m'
_Green='\033[32m'
_Orange='\033[33m'
_Blue='\033[34m'
_Purple='\033[35m'
_Cyan='\033[36m'
_Lightred='\033[91m'
_Lightgreen='\033[92m'
_Yellow='\033[93m'
_Lightblue='\033[94m'
_Pink='\033[95m'
_Lightcyan='\033[96m'

#  ------< Fonts and effects >-------

_Bold='\033[01m'
_Disable='\033[02m'
_Underline='\033[04m'
_Reverse='\033[07m'
_Strikethrough='\033[09m'

# -----------------------------------

# list of colors used to randomize colors
colors = [_Red, _Green, _Yellow, _Blue, _Purple, _Cyan, _Lightblue, _Orange, _Lightred, _Lightgreen, _Pink, _Lightcyan]

def printColor(str, color=_Reset, FX=_Reset,isRandom=False, delay=0, end=True):
    """
        Prints an input str with an optionaly given color, effect and delay!
        end is if one wants go to next line when function is done
    """
    for char in str:

        if name == 'nt': color, FX, isRandom= '', '', False # for windows, if windows: no colors no effects no random just plain white text

        if isRandom:
            color = colors[random.randint(0, len(colors) - 1)] # choose a random color
            
        sys.stdout.write(FX + color + char + _Reset) # print the str with colors and fx
        sys.stdout.flush()

        time.sleep(delay/100) # delay is better to be in milliseconds

    if end: 
        sys.stdout.write('\r\n') # go back to the beginning of the new line
        sys.stdout.flush()

def clear(): 
    """
     Clears the console
    """
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux
    else: 
        _ = system('clear') 