# check.py

import subprocess, os

def regkey(path, key):
    try:
        subprocess.run(["powershell", "-Command", "powershell.exe Get-ItemProperty -Path '" + path + "' -Name " + key], check=True)
    except:
        print("Path not found")

def regkey_path(path, key): 
    try:
        if subprocess.run(["powershell", "-Command", "powershell.exe Get-ItemPropertyValue -Path '" + path + "' -Name " + key], capture_output=True):
            return True
        else:
            return False
    except:
        print("Path not found")
        return False

def regkey_value(path, key, value):
    try:
        if subprocess.run(["powershell", "-Command", "powershell.exe Get-ItemPropertyValue -Path '" + path + "' -Name " + key], capture_output=True, text=True).stdout.strip() == value:
            return True
        else:
            return False
    except:
        print("Path not found")

## design check directory cause i'm tired
