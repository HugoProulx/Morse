from gpiozero import LED
from time import sleep

led = LED(17)

led.on()
sleep(1)
led.off()
sleep(0.3)
led.On()
sleep(0.3)
led.off()
sleep(0.3)
led.on()
sleep(0.3)
led.off()

