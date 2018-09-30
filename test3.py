import os
from time import sleep
from random import *

for x in range(4):
    OGfile = randint(11)
    LinuxVolume = "amixer sget Master | grep 'Right:' | awk -F'[][]' '{ print $2 }'"
    os.system(LinuxVolume)
    FileToPrint = "aplay Recording_{}.wav".format(OGfile)
    os.system(FileToPrint)
    sleep(10)
