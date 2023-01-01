from rpi_backlight import Backlight 

display = Backlight()
display.fade_duration = 1
display.brightness = 60

def display_off():
    display.power = False

def display_on():
    display.power = True
