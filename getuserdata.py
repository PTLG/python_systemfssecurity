import wmi



def MountedDrivesScanner(name):
    c=wmi.WMI()     #monitor interface initialization

    wmi_service = c.Win32_ProcessStartup()

    while True:
        while wmi_service == None:
            print(wmi_service)


MountedDrivesScanner("Tom")