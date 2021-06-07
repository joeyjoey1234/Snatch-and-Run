import subprocess
import os
##  %USERPROFILE%
## com_user = subprocess.run(["whoami"],stdout=subprocess.PIPE)
### print(com_user.stdout.decode('utf-8'))'
## exit_code sample
#exit_codes = {'0': 'success','1':'access denied','128':'no such process'}
## this is the args with the sub process
#firefox_pro = '/IM /F firefox.exe'
#chrome_pro = '/IM /F chrome.exe'
#outlook_pro = '/IM /F OUTLOOK.EXE'
#test = '/IM cmd.exe'
## process is ran as soon as its quoted as seen here
#kill_firefox = subprocess.run(['taskkill',[firefox_pro]],stdout=subprocess.PIPE)
#kill_chrome = subprocess.run(['taskkill',[chrome_pro]],stdout=subprocess.PIPE)

#kill_outlook = subprocess.run(['taskkill',[outlook_pro]],stdout=subprocess.PIPE)
#kill_test = subprocess.run(['taskkill',[test]])
## all this does is print the stdout
## this func filters the return code from a taskkill command
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
## func to check for compeltion
def return_for_code(x):
    for y in exit_codes:
        if y == filter_kill_code(x):
            print(exit_codes[y])
#how to use this kill check code status return!
# how to use     return_for_code(kill_test)
#this is the final!!
def kill():
    exit_codes = {'0': 'success', '1': 'access denied', '128': 'no such process'}
    firefox_pro = '/F /IM firefox.exe'
    chrome_pro = '/F /IM chrome.exe'
    outlook_pro = '/F /IM OUTLOOK.EXE'
    firefox_crash = '/F /IM crashreporter.exe'
    kill_chrome = subprocess.run(['taskkill', [chrome_pro]], stdout=subprocess.PIPE)
    kill_firefox = subprocess.run(['taskkill', [firefox_pro]], stdout=subprocess.PIPE)
    kill_firefox
    kill_outlook = subprocess.run(['taskkill', [outlook_pro]], stdout=subprocess.PIPE)
    kill_firefox_crash = subprocess.run(['taskkill',[firefox_crash]],stdout=subprocess.PIPE)

kill()





