import wmi

c = wmi.WMI()

# #this one it's gonna be good for checking by some measurement amount of time what
# #processes are actually running on monitored OS
#
# for process in c.Win32_Process():
#     print(process.ProcessId, process.Name)


#
# #this one returns the running operation system
# for os in c.Win32_OperatingSystem():
#     print(os.Caption)


# #this one is the monitor of creation of new processes on the running operation system
# process_watcher = c.Win32_Process.watch_for("creation")
# while True:
#     new_process = process_watcher()
#     print(new_process.Caption)

# #this one give me a view at the logical drives working on running device
# #except TypeError is used, because the LogicalDisk class returns some uninteresting shit
# #for my expectation about this for instruction ;D
# try:
#     for disk in c.Win32_LogicalDisk():
#         print(disk.Caption, disk.Name, ((int(disk.size)/1024)/1024)/1024, ((int(disk.FreeSpace)/1024)/1024)/1024, disk.FileSystem)
# except TypeError:
#     pass

# #wmi also can return some informations by passing for the query method the query message, like
# #on the example written below:
# wql = "SELECT Caption, Description FROM Win32_LogicalDisk"
# for disk in c.query(wql):
#     print(disk)

# # listing available subclasses of the classes in WMI enivronment
# for i in c.subclasses_of("__ExtrinsicEvent"):
#     print(i)

# # listing available method of given Win32 class
# print(c.Win32_ComputerSystem.methods.keys())

# #this code returns the structure of given object/class in readable output
# print(c.Win32_OperatingSystem)
# for os in c.Win32_OperatingSystem():
#     print(os)

# #listing all explorer.exe processes
# for process in c.Win32_Process(name="explorer.exe"):
#     print(process.ProcessId, process.Name)


# #following code creates, and then destroy 50 processes of notepad
# #in for construction each process returns his id and process name itself
# for i in range(50):
#     process_id, return_value = c.Win32_Process.Create(CommandLine="notepad.exe")
#
#     for process in c.Win32_Process(ProcessId=process_id):
#         print(process.ProcessId, process.Name)
#
#     result = process.Terminate()

# #this one bellow returns services, which are not runned, but they are declared as automatic services,
# #like for example - google update daemon/service
#
# stopped_services = c.Win32_Service(StartMode='Auto', State='Stopped')
# if stopped_services:
#     for s in stopped_services:
#         print(s.Caption, "service is not running")
# else:
#     print("no auto services stopped")


# #this one returns all services on the running operating system
# for s in c.Win32_Service():
#     print(s.Caption)

# #this one returns value(measured in percents) how much space is still available on drives
# #under running operating system
# for disk in c.Win32_LogicalDisk(DriveType=3):
#     print(disk.Caption, "%0.2f%% free" %(100.0* float(disk.FreeSpace)/float(disk.Size)))

# #below one prints all active network interfaces on the running operating system, with informations
# #about ipaddress (ipv4 and ipv6) and with attached MAC address of that interface
# for interface in c.Win32_NetworkAdapterConfiguration(IPEnabled=1):
#     print(interface.Description, interface.MACAddress)
#     for ip_address in interface.IPAddress:
#         print(ip_address)
#

# #this one show all running, at startup of the system, applications
# for s in c.Win32_StartupCommand():
#     print(s.Location, s.Caption, s.Command)

