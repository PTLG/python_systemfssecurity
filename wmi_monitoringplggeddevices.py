import wmi
import time
from watchdog import observers, events
import logging
import sys
from threading import *
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(message)s')

"""
TODO:
*gets familiar with watchdog module(for filesystem monitoring)
*gets familiar with python design patterns
*gets familiar with python application development
*in the name of getting things done - gettings done python threading, mutlithreading, multiprocessing book

TODO_EXTRA:
*gets familiar with gathering data from kafka(producer/consumer) in more civilisated way than reading output
from file/cli(probably delegate the log management to kibana instance? ... issue worth to think about it)


"""

def watchdogMonitorDirectory():

    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = events.LoggingEventHandler()
    observer = observers.Observer()
    observer.schedule(event_handler, "C:/", recursive=True)
    observer.start()


def proccessDescription():
    while True:

        c2 = wmi.WMI()
        for j in c2.Win32_Process():
            logging.info((j.Caption, j.ExecutablePath, j.ProcessId))


def hardDriveMonitor():

    while True:
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
                logging.info((disk.Caption, disk.Description, disk.DriveType, disk.FileSystem, "{:.2f}".format(int(disk.FreeSpace)/1024/1024/1024), 'GB', "{:.2f}".format(int(disk.Size)/1024/1024/1024), "GB", disk.VolumeName))
        time.sleep(5)


def run():
    t1 = Thread(target=watchdogMonitorDirectory)
    t2 = Thread(target=hardDriveMonitor)
    #t3 = Thread(target=proccessDescription)

    t1.run()
    t2.run()
    #t3.run()



if __name__=="__main__":
    while True:
        run()
        proccessDescription()