import os
import subprocess
##prefs.js need to be in same folder as script
## also get prefs.js from andys orginal folder and edit that one then put in root exe folder
### also get cert9.db with cert added allready from og profile\

## put both cert9.db and prefs.js into root of exe file
logged_user_os_fix = os.environ['USERPROFILE']
all_profiles = '{}\AppData\Roaming\Mozilla\Firefox\Profiles\*.default*'.format(logged_user_os_fix)

def proxy_settings_cert_settings():
    all_firefox_profiles = subprocess.run(['cmd.exe',['/c dir {} /s /b '.format(all_profiles)]],stdout=subprocess.PIPE)
    all_firefox_profiles = all_firefox_profiles.stdout.decode('utf-8')
    all_firefox_profiles = str(all_firefox_profiles)
    all_firefox_profiles = all_firefox_profiles.split()
    for x in all_firefox_profiles:
        os.system('robocopy ./ {}\ prefs.js'.format(x))
        os.system('robocopy ./ {}\ cert9.db'.format(x))

