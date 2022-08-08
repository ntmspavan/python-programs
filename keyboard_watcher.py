#pip install keyboard
from keyboard import press, is_pressed
import time

#change 'refresh_seconds' for how often right arrow is is_pressed

refresh_seconds = 2

# change 'duration_minutes'  for how long you would like program to run
duration_minutes = 1

count = 0
while(count *refresh_seconds/60<duration_minutes):
  time.sleep(refresh_seconds)
  press('right arrow')
  count += 1
