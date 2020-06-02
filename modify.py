import os
import sys
import subprocess
import datetime as dt
import csv
import shutil

os.system("date")
# os.system("ils")

hours_removed = dt.timedelta(hours = 7)
# os.chdir('/home/safwan/Documents/change_file_name/2020_05_30')

# for f in os.listdir():
#     print(f)


def processFileName(arg):

  timeFromName=arg[-54:-35] #time string: 2020-05-30-19-55-00
  print('time from file name: ',timeFromName)
  timeObj= dt.datetime.strptime(timeFromName,'%Y-%m-%d-%H-%M-%S')
  timeSubtracted7h=timeObj-hours_removed
  print(["Original time: " + timeObj.strftime('%Y-%m-%d-%H-%M-%S'), "Subtracted time: " + timeSubtracted7h.strftime('%Y-%m-%d-%H-%M-%S')])
  return [timeSubtracted7h.strftime('%Y-%m-%d-%H-%M-%S'), timeFromName]

arg=sys.argv[1]
listOfNewAndOldTimes=processFileName(arg)
#print(listOfNewAndOldTimes)
newFilename=arg.replace(listOfNewAndOldTimes[1], listOfNewAndOldTimes[0])
print( arg, '\n',newFilename)
# dest = shutil.copyfile(arg, newFilename) 
# print("New file was created at ", dest)
subprocess.run('cp '+arg+' '+ newFilename, shell=True) # cp the original file with a new name
removeFileExt=arg.replace('.csv','')
subprocess.run('echo '+'"original filename: '+arg[-54:]+'"'+ ' >> '+ removeFileExt+'_back_in_time.txt', shell=True) # create a file named {ORIGINALFILENAME}_back_in_time.txt
#whose contents are the original filename, and the new file name
subprocess.run('echo '+'"new filename: '+newFilename[-54:]+'"'+ ' >> '+ removeFileExt+'_back_in_time.txt', shell=True)






# ts = float("1590893701.741696") # time to read from file

# # if you encounter a "year is out of range" error the timestamp
# # may be in milliseconds, try `ts /= 1000` in that case
# timeStr=dt.datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d-%H-%M-%S') # converting unix to readable date
# print(timeStr) # print data




# print ('Current date/time: {}'.format(dt.datetime.utcfromtimestamp(ts)-hours_removed)) # adding hours to the unix time 

# fomatting=dt.datetime.utcfromtimestamp(ts)-hours_removed

# print(fomatting.strftime('%Y-%m-%d-%H-%M-%S'))