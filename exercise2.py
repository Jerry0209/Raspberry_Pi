from gpiozero import Button
from gpiozero import LED
from time import sleep

print("Hello world!")

led = LED(3)

button = Button(2)
while True:
    if button.is_pressed:
        print("Button is pressed")
        sleep(0.2)  # debouncing
        led.toggle()

    else:
        print("Button is not pressed")
