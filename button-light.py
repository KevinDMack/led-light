from signal import pause
from gpiozero import LED, Button
import time

time.sleep(10)
button = Button(17)
led = LED(4)

button.when_pressed = led.on
button.when_released = led.off

pause()
