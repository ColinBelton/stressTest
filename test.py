import os

for x in range(3):

    from random import *
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

     
     
