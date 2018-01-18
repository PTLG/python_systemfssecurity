import psutil
import wmi, pythoncom, os

try:
    pythoncom.CoInitialize()
    connection = wmi.WMI()
    watcher = connection.Win32_Process.watch_for("creation")

    while True:
        new_process = watcher()
        if len(psutil.Process(new_process.ProcessID).cmdline()) == 2 and (os.path.exists(psutil.Process(new_process.ProcessID).cmdline()[1])):
            print("PID: ", new_process.ProcessID)
            print("Name: ", new_process.Caption)
            print("Priority: ", new_process.Priority)
            print("Filename: ", psutil.Process(new_process.ProcessID).cmdline()[1])
            print("Software used: ", psutil.Process(new_process.ProcessID).cmdline()[0])
        if psutil.Process(new_process.ParentProcessId):
            print("Parent PID: ", new_process.ParentProcessId)
            print("Parent Name: ", psutil.Process(new_process.ParentProcessId).name())
            print("Parent Executable: ", psutil.Process(new_process.ParentProcessId).cmdline()[0])

except KeyboardInterrupt as e:
    print(e)
finally:
    pythoncom.CoUninitialize()