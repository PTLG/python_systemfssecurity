import wmi
import time
import datetime
from threading import Thread
import watchdog


"""
TODO:
*push the git things at next level - canceling pushed changes on github, and other things :D
*gets familiar with watchdog module(for filesystem monitoring)
*gets familiar with python design patterns
*gets familiar with python application development
*in the name of getting things done - gettings done python threading, mutlithreading, multiprocessing book

TODO_EXTRA:
*gets familiar with gathering data from kafka(producer/consumer) in more civilisated way than reading output
from file/cli(probably delegate the log management to kibana instance? ... issue worth to think about it)


"""


def hardDriveMonitor():

    while True:
        c = wmi.WMI()
        # for disk in c.Win32_LogicalDisk(DriveType='3'):  #DriveType='3' or DriveType='2'
        #     #print(disk)
        #     ts = time.time()
        #     ds=datetime.datetime.fromtimestamp(ts)
        #     print(ds ,disk.Caption, disk.Description, disk.DriveType, disk.FileSystem, "{:.2f}".format(int(disk.FreeSpace)/1024/1024/1024), 'GB', "{:.2f}".format(int(disk.Size)/1024/1024/1024), 'GB', disk.VolumeName)
        c1 = wmi.WMI()
        for disk in c1.Win32_LogicalDisk(DriveType='2'):  #DriveType='3' or DriveType='2'
            if disk.Caption=="A:":
                pass
            else:
                ts = time.time()
                ds = datetime.datetime.fromtimestamp(ts)
                print(ds ,disk.Caption, disk.Description, disk.DriveType, disk.FileSystem, "{:.2f}".format(int(disk.FreeSpace)/1024/1024/1024), 'GB', "{:.2f}".format(int(disk.Size)/1024/1024/1024), "GB", disk.VolumeName)
        time.sleep(30)



def startMonitoring():
    t1 = Thread(target=hardDriveMonitor())
    t1.start()



if __name__=="__main__":
    startMonitoring()