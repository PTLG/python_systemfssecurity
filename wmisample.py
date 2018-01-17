import wmi

try:
    for netParams in wmi.WMI().Win32_NetworkAdapterConfiguration():
        if netParams.MACAddress != None and netParams.IPAddress != None and netParams.IPSubnet != None:
            if netParams.DNSDomain != None:
                print(''.ljust(60,'='))
                print('Domain: ' + netParams.DNSDomain)
                print('MAC:' + netParams.MACAddress.lower())
                print('IP: ' + netParams.IPAddress[0])
                print('mask:' + netParams.IPSubnet[0])

    for profileParams in wmi.WMI().Win32_NetworkLoginProfile():
        if profileParams.Name != None:
            print(''.ljust(60, '='))
            print('Profile: ' + profileParams.Name)

    for SOParams in wmi.WMI().Win32_OperatingSystem():
        print(''.ljust(60, '='))
        print('OS: ' + SOParams.caption)
        print('Computer Name: ' + SOParams.CSName)
        print('Architecture: ' + SOParams.OSArchitecture)
        print('User Registered: ' + SOParams.RegisteredUser)

except Exception as e:
    print(e)