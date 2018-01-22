import wmi
import os
import re

"""mounted drives monitor"""


def MountedDrivesScanner():
    c=wmi.WMI()     #monitor interface initialization

    wmi_service = c.Win32_Group()

    for i in range(len(wmi_service)):
        print(wmi_service[i])


MountedDrivesScanner()