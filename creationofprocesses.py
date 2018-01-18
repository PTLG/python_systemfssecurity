# import psutil
# import wmi, pythoncom, os
#
# try:
#     pythoncom.CoInitialize()
#     connection = wmi.WMI()
#     watcher = connection.Win32_Process.watch_for("creation")
#
#     while True:
#         new_process = watcher()
#             if:
#                 len(psutil.Process(new_process.ProcessID).cmdline()) == 2 and (os.path.exists(psutil.Process(new_process.ProcessID).cmdline()):
#                     print("PID: ", new_process.ProcessID)
