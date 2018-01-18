from time import sleep
import wmi


connection=wmi.WMI()

while True:
    try:
        for physical_disk in connection.Win32_DiskDrive():
            for partition in physical_disk.associators("Win32_DiskDriveToDiskPartition"):
                for logical_unit in partition.associators("Win32_LogicalDiskToPartition"):
                    print("Logical disk: " + logical_unit.Caption)
                    print("Volume Name: " + logical_unit.VolumeName)
                    print("File system type: " + logical_unit.FileSystem)
                    sizevalue=int(float(logical_unit.Size)/1073741824)
                    print("Size (GB): ", sizevalue)


        sleep(10)
    except Exception as e:
        print(e)