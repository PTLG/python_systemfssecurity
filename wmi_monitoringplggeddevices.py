import wmi
import time
import datetime


def hardDriveMonitor():

    while True:
        c = wmi.WMI()
        for disk in c.Win32_LogicalDisk(DriveType='3'):  #DriveType='3' or DriveType='2'
            #print(disk)
            ts = time.time()
            ds=datetime.datetime.fromtimestamp(ts)
            print(ds ,disk.Caption, disk.Description, disk.DriveType, disk.FileSystem, "{:.2f}".format(int(disk.FreeSpace)/1024/1024/1024), 'GB', "{:.2f}".format(int(disk.Size)/1024/1024/1024), 'GB', disk.VolumeName)
        c1 = wmi.WMI()
        for disk in c1.Win32_LogicalDisk(DriveType='2'):  #DriveType='3' or DriveType='2'
            if disk.Caption=="A:":
                pass
            else:
                ts = time.time()
                ds = datetime.datetime.fromtimestamp(ts)
                print(ds ,disk.Caption, disk.Description, disk.DriveType, disk.FileSystem, "{:.2f}".format(int(disk.FreeSpace)/1024/1024/1024), 'GB', "{:.2f}".format(int(disk.Size)/1024/1024/1024), "GB", disk.VolumeName)



hardDriveMonitor()