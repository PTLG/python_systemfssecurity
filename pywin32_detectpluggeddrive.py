import win32serviceutil
import win32service
import win32event
import servicemanager
import win32gui
import win32gui_struct
import win32con

struct = win32gui_struct.struct
pywintypes = win32gui_struct.pywintypes

GUID_DEVINTERFACE_USB_DEVICE = "{A5DCBF10-6530-11D2-901F-00C04FB951ED}"
DBT_DEVICEARRIVAL = 0x8000
DBT_DEVICEREMOVECOMPLETE = 0x80004

import ctypes

def _UnpackDEV_BROADCAST (lparam):

    if lparam == 0: return None

    hdr_format              =   "iii"
    hdr_size                =   struct.calcsize(hdr_format)
    hdr_buf                 =   win32gui.PyGetMemory(lparam, hdr_size)
    size, devtype, reserved =   struct.unpack("iii", hdr_buf)
    buf                     =   win32gui.PyGetMemory(lparam, size)

    extra                   =   {}


    if devtype == win32con.DBT_DEVTYP_DEVICEINTERFACE:

        fmt                 =   hdr_format + "16s"
        _, _, _, guid_bytes =   struct.unpack(fmt, buf[:struct.calcsize(fmt)])
        extra['classguid']  =   pywintypes.IID(guid_bytes, True)
        extra['name']       =   ctypes.wstring_at(lparam + struct.calcsize(fmt))

    else:

        raise NotImplementedError("unknow device type %d".format(devtype))

    return win32gui_struct.DEV_BROADCAST_INFO(devtype, **extra)



win32gui_struct.UnpackDEV_BROADCAST = _UnpackDEV_BROADCAST



class DeviceEventService(win32serviceutil.ServiceFramework):

    _svc_name               =   "DevEventHandler"
    _svc_display_name       =   "Device Event Handler"
    _svc_description_       =   "Handle device notification events"


    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop      =   win32event.CreateEvent(None, 0, 0, None)
        filter              =   win32gui_struct.PackDEV_BROADCAST_DEVICEINTERFACE(

            GUID_DEVINTERFACE_USB_DEVICE
        )
        self.hDevNotify     =   win32gui.RegisterDeviceNotification(
            self.ssh,
            filter,
            win32con.DEVICE_NOTIFY_SERVICE_HANDLE
        )


    def GetAcceptedControls(self):
        rc                  =   win32serviceutil.ServiceFramework.GetAcceptedControls(self)
        rc                  |=  win32service.SERVICE_CONTROL_DEVICEEVENT
        return rc



    def SvcOtherEx(self, control, event_type, data):
        if control == win32service.SERVICE_CONTROL_DEVICEEVENT:
            info            =   win32gui_struct.UnpackDEV_BROADCAST(data)

            if event_type == DBT_DEVICEARRIVAL:
                servicemanager.LogMsg(
                    servicemanager.EVENTLOG_INFORMATION_TYPE,
                    0xF000,
                    ("Device %s arrived".format(info.name), "")

                )
            elif event_type == DBT_DEVICEREMOVECOMPLETE:
                servicemanager.LogMsg(
                    servicemanager.EVENTLOG_INFORMATION_TYPE,
                    0xF000,
                    ("Device %s removed".format(info.name), "")

                )


    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)


    def SvcDoRun(self):
        win32event.WaitForSingleObject(self.hWaitStop, win32event.INFINITE)
        servicemanager.LogMsg(
            servicemanager.EVENTLOG_INFORMATION_TYPE,
            servicemanager.PYS_SERVICE_STOPPED,
            (self._svc_name, '')

        )



if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(DeviceEventService)