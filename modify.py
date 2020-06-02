import os
import sys
import subprocess
import datetime as dt
import csv
import shutil
import time
from pytz import timezone

os.system("date")

hours_removed = dt.timedelta(hours = 7)

def processFileName(arg):

  timeFromName=arg[-54:-35] #time string: 2020-05-30-19-55-00
  # print('time from file name: ',timeFromName)
  timeObj= dt.datetime.strptime(timeFromName,'%Y-%m-%d-%H-%M-%S')
  timeSubtracted7h=timeObj-hours_removed
  # print(["Original time: " + timeObj.strftime('%Y-%m-%d-%H-%M-%S'), "Subtracted time: " + timeSubtracted7h.strftime('%Y-%m-%d-%H-%M-%S')])
  return [timeSubtracted7h.strftime('%Y-%m-%d-%H-%M-%S'), timeFromName, timeObj]

arg=sys.argv[1]
CAN_GPS=arg[-16:-13]
listOfNewAndOldTimes=processFileName(arg)
newFilename=arg.replace(listOfNewAndOldTimes[1], listOfNewAndOldTimes[0])
# print( arg,'\n',newFilename)
if CAN_GPS == 'CAN':
  subprocess.run('touch '+ newFilename, shell=True) # cp the original file with a new name
if CAN_GPS == 'GPS':
  subprocess.run('cp '+arg+ ' '+ newFilename, shell=True) # cp the original file with a new name

removeFileExt=arg.replace('.csv','')
subprocess.run('echo '+'"original filename: '+arg[-54:]+'"'+ ' >> '+ removeFileExt+'_back_in_time.txt', shell=True) # create a file named {ORIGINALFILENAME}_back_in_time.txt
#whose contents are the original filename, and the new file name
subprocess.run('echo '+'"new filename: '+newFilename[-54:]+'"'+ ' >> '+ removeFileExt+'_back_in_time.txt', shell=True)

originalStartTime=listOfNewAndOldTimes[2] #original starting time
inFile=arg
outfile=newFilename
if CAN_GPS == 'CAN': 
  with open(inFile, 'r') as in_csv, open(outfile , 'w') as out_csv:
      reader = csv.reader(in_csv)
      writer = csv.writer(out_csv)
      header = next(reader) #first line of the csv
      writer.writerow(header)
      for row in reader:
        line=row
        Time=line[0]
        ts=float(Time)
        TimefromFile=dt.datetime.fromtimestamp(ts) # creating a datetime object
        if (TimefromFile > originalStartTime):
          ts=ts-(3600*7) #subtract 7h
          line[0]=ts
        else:
          pass
          #do nothing
        writer.writerow(line)







