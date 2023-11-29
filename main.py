import check

check.regkey(path="HKLM:\SOFTWARE\Microsoft\WindowsUpdate", key="SupportsUUP")


if check.regkey_path(path="HKLM:\SOFTWARE\Microsoft\WindowsUpdate", key="SupportsUUP"):
    print("Registry key exists")


if check.regkey_value(path="HKLM:\SOFTWARE\Microsoft\WindowsUpdate", key="SupportsUUP", value="1"):
    print("Garry Set - 1 point gained")




