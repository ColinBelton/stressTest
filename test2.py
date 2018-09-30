import os
from time import sleep
from random import *
for x in range(4):
    OGfile=randint(1, 4)
    if OGfile == 1:
        print OGfile
        os.system("aplay Recording_1.wav")
    if OGfile == 2:
        print OGfile
        os.system("aplay Recording_2.wav")
    if OGfile == 3:
        print OGfile
        os.system("aplay Recording_3.wav")
    if OGfile == 4:
        print OGfile
        os.system("aplay Recording_4.wav")
    sleep(10)
