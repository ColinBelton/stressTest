import os
#from time import sleep
import time
#from random import *
import random

for x in range(4):
    OGfile = what_time.wav
#    LinuxVolume = "amixer sget Master | grep 'Right:' | awk -F'[][]' '{ print $2 }'"
#    os.system(LinuxVolume)
    FileToPrint = "aplay Recording_{}.wav".format(OGfile)
    os.system(FileToPrint)
    time.sleep(10)
#    sleep(10)
