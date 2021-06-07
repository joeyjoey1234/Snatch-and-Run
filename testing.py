import os
import subprocess
logged_user_dir = '%USERPROFILE%'
folder_loc = '{}\lmao'.format(logged_user_dir)


outlook_pro = '/F /IM OUTLOOK.EXE'
kill_outlook = subprocess.run(['taskkill', [outlook_pro]], stdout=subprocess.PIPE)
kill_outlook