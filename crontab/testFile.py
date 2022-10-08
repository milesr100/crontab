import os
import sys
import time
import crontab
import pandas as pd

#working directory
cwd = os.getcwd()
print(cwd)


#create dictionary w/ dummy data
MBZ = pd.read_json('http://musicbrainz.org/ws/2/artist/5b11f4ce-a62d-471e-81fc-a69a8278c7da?fmt=json')
MBZ.to_csv('data/MBZ.csv',)


#current time
now = time.time()
nowStr = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime(now))
print('This program started running at: ', timestart)


# save current time as string
nowStr = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime(now))


# create a new file in the current working directory
with open(cwd + '/home/miles/crontab/testFile_' + nowStr + '.txt', 'w') as f:
    f.write(str(MBZ))


