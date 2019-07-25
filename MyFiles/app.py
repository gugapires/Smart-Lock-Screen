from plyer import notification
from time import sleep
import win32api
import ctypes
import time


savedpos = win32api.GetCursorPos()
count = 0

start = time.time()
print(start)

while(True):
	curpos = win32api.GetCursorPos()
	if savedpos != curpos:
		count = count +1
		savedpos = curpos
		print("Mouse Movement # ", count)
		sleep(0.05)
	elif savedpos == savedpos:
			print("mesma posição")
			sleep(0.05)
