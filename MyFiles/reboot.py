import os

shut = "shutdown -r -t 0"
desl = os.system(shut)
print("O computador será reinicidado", desl)
