import wmi, logging

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(message)s')

def proccessDescription():
    while True:
        log1 = logging.getLogger("processdescription_logger")
        c2 = wmi.WMI()
        for j in c2.Win32_Process():
            log1.info((j.Caption, j.ExecutablePath, j.ProcessId))





if __name__ == "__main__":
    while True:
        proccessDescription()