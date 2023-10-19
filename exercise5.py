from gpiozero import LED
from time import sleep

print("Start!")

led = LED(2)

while True:
    led.toggle()
    sleep(1)
