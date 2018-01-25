import psutil, sys
import wmi, pythoncom
import socket

try:
    pythoncom.CoInitialize()
    connection = wmi.WMI()
    watcher = connection.Win32_Process.watch_for("creation")

    while True:
        new_process = watcher()
        if psutil.Process(new_process.ProcessID).connections(kind="all"):
            open_connection = psutil.Process(new_process.ProcessID).connections(kind="all")
        elif psutil.Process(new_process.ParentProcessId).connections(kind="all"):
            open_connection = psutil.Process(new_process.ParentProcessId).connections(kind="all")

        ip_list = []

        for jump in open_connection:
            try:
                if jump[4][0] != None and jump[4][0] != '':
                    if not any(ip in jump[4][0] for ip in ip_list):
                        ip_list.append(jump[4][0])
            except:
                continue
        print(ip_list)
        for item in ip_list:
            try:
                print(socket.gethostbyaddr(item)[0])
            except:
                continue
except Exception as e:
    print(e)
finally:
    pythoncom.CoUninitialize()