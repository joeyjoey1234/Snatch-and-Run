import os
import subprocess


#Use regedit keys to enable brave proxy
##key.reg and mitm proxy pem needs to be in the root exe
os.system('regedit.exe /S ./key.reg')
os.system('certutil –addstore –f "Root" ./mitmproxy-ca-cert.pem')