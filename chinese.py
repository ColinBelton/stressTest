import time
import os

for x in range(11):
   FileToPlay = "aplay what_time.wav"
   os.system(FileToPlay)
   time.sleep(10)
