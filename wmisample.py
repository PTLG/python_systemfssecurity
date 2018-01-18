import wmi


def GetSomeParticularData():
    return_message=[]
    try:
        for netParams in wmi.WMI().Win32_NetworkAdapterConfiguration():
            if netParams.MACAddress != None and netParams.IPAddress != None and netParams.IPSubnet != None:
                if netParams.DNSDomain != None:
                    return_message.append(''.ljust(60,'=')+'\n')
                    return_message.append('Domain: ' + netParams.DNSDomain + '\n')
                    return_message.append('MAC:' + netParams.MACAddress.lower() + '\n')
                    return_message.append('IP: ' + netParams.IPAddress[0] + '\n')
                    return_message.append('mask:' + netParams.IPSubnet[0] + '\n')

        for profileParams in wmi.WMI().Win32_NetworkLoginProfile():
            if profileParams.Name != None:
                return_message.append(''.ljust(60, '=') + '\n')
                return_message.append('Profile: ' + profileParams.Name + '\n')

        for SOParams in wmi.WMI().Win32_OperatingSystem():
            return_message.append(''.ljust(60, '=') + '\n')
            return_message.append('OS: ' + SOParams.caption + '\n')
            return_message.append('Computer Name: ' + SOParams.CSName + '\n')
            return_message.append('Architecture: ' + SOParams.OSArchitecture + '\n')
            return_message.append('User Registered: ' + SOParams.RegisteredUser + '\n')

    except Exception as e:
        print(e)

    return return_message