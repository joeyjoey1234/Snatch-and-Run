kill_brave = subprocess.run(['taskkill', [brave_pro]], stdout=subprocess.PIPE)
for x in range(1, 14):
    kill_brave