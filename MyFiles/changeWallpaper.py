import ctypes
SPI_SETDESKWALLPAPER = 20 
ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, "imagem.jpg" , 0)

print("Wallpaper mudado!")
