# -*- coding: utf-8 -*-

import os
from datetime import datetime
import shutil
##Utils copy, etc.

dt = datetime.now()
cur_date = dt.strftime("%A, %d %B %Y %I:%M%p\n")

filersa = 'remote_rsa'
user_ssh_dir = '/home/oracle/.ssh'
cur_dir = '/tmp'
result_good_file = 'TestGood'
result_bad_file = 'TestBad'
log_file = 'steps.log'

print('Current date: ' + cur_date)

def writeToFile(file='',str=''):
    os.chdir(cur_dir)
    fd = open(file,'a')
    fd.write(str)
    fd.close()

def touch(path=''):
    with open(path,'a'):
        os.utime(path,None)
        ##os.close(path)

def checkCreateRSA(file,path):
    """Check exist file RSA. If not exists - Create """
    cmd = 'ssh-keygen -t rsa -b 4096 -N \'\' -f' + path + '/' + file

    os.chdir(path)
    if os.path.isfile(file):
        return True
    else:
        result = os.system(cmd)
        if result == 0:
            return True
        else:
            return False

if not os.path.isfile(log_file):
    touch(log_file)
else:
    writeToFile(log_file,cur_date)

if checkCreateRSA(filersa,user_ssh_dir):
    writeToFile(log_file,'')