import os
import win32con, win32file
import pythoncom

pythoncom.CoInitialize()

ACTIONS = {
    1: "Created",
    2: "Deleted",
    3: "Updated",
    4: "Renamed from something",
    5: "Renamed to something"
}

accessMode = 0x0001

FileSystemPath = "C:\\"

hDir = win32file.CreateFile(
    FileSystemPath,
    accessMode,
    win32file.FILE_SHARE_READ | win32file.FILE_SHARE_WRITE | win32file.FILE_SHARE_DELETE,
    None,
    win32file.OPEN_EXISTING,
    win32con.FILE_FLAG_OVERLAPPED | win32con.FILE_FLAG_BACKUP_SEMANTICS,
    None
)

flag_exit = 0

while flag_exit == 0:
    try:
        results = win32file.ReadDirectoryChangesW(
            hDir,
            5012,
            True,
            win32con.FILE_NOTIFY_CHANGE_FILE_NAME |
            win32con.FILE_NOTIFY_CHANGE_DIR_NAME |
            win32con.FILE_NOTIFY_CHANGE_ATTRIBUTES |
            win32con.FILE_NOTIFY_CHANGE_SIZE |
            win32con.FILE_NOTIFY_CHANGE_LAST_WRITE |
            win32con.FILE_NOTIFY_CHANGE_SECURITY,
            None,
            None
        )
        for action, file in results:
            full_filename = os.path.join(FileSystemPath, file)
            if os.path.isfile(full_filename):
                print("File ", ACTIONS[action], ": ", full_filename)
            if action == 2:
                print("File deleted: " + full_filename)
        if not os.path.exists(FileSystemPath):
            flag_exit = 1
            print(FileSystemPath, " storage unit has been extracted")
    except Exception as e:
        print(e)
    finally:
        pythoncom.CoUninitialize()

