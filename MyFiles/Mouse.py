import win32api
import ctypes
import time
from time import sleep

## Instalar a parada abaixo
##pip install pypiwin32


savedpos = win32api.GetCursorPos()
count = 0
while(True):

    curpos = win32api.GetCursorPos()
    if savedpos != curpos:
        count = count +1
        savedpos = curpos
        print("Mouse Movement # ", count)
    sleep(0.05)


#ctypes.windll.user32.LockWorkStation()
