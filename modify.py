import os
import sys
import subprocess
import datetime as dt
import csv

os.system("date")
# os.system("ils")

hours_removed = dt.timedelta(hours = 7)

def processFileName(arg):

  timeFromName=arg[-54:-35] #time string: 2020-05-30-19-55-00
  print('time from file name: ',timeFromName)
  timeObj= dt.datetime.strptime(timeFromName,'%Y-%m-%d-%H-%M-%S')
  timeSubtracted7h=timeObj-hours_removed
  return ["Original time: " + timeObj.strftime('%Y-%m-%d-%H-%M-%S'), "Subtracted time: " + timeSubtracted7h.strftime('%Y-%m-%d-%H-%M-%S')]

arg=sys.argv[1]
timeFromeFileName=processFileName(arg)
print(timeFromeFileName)






ts = float("1590893701.741696") # time to read from file

# if you encounter a "year is out of range" error the timestamp
# may be in milliseconds, try `ts /= 1000` in that case
timeStr=dt.datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d-%H-%M-%S') # converting unix to readable date
print(timeStr) # print data




print ('Current date/time: {}'.format(dt.datetime.utcfromtimestamp(ts)-hours_removed)) # adding hours to the unix time 

fomatting=dt.datetime.utcfromtimestamp(ts)-hours_removed

print(fomatting.strftime('%Y-%m-%d-%H-%M-%S'))