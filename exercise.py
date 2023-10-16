from gpiozero import Button
from gpiozero import LED
from time import sleep
print("Hello world!")

led = LED(2)

button = Button(4)
flag = 0

while True:
    if (button.is_pressed) and (flag == 0):
        print("Button is pressed")
        led.toggle()
        flag = 1
    else:
        print("Button is not pressed")
        flag = 0



print("finish")
