print("Hello world!")

from gpiozero import Button
from gpiozero import LED

led = LED(3) # GPIO4 Led lightened for while and then off?

button = Button(2)  # I don't know why I can't use GPIO4 for button: runtime error: failed to add edge detection,
# another GPIO is feasible

while True:
    if button.is_pressed:
        print("Button is pressed")
        led.on()
    else:
        print("Button is not pressed")
        led.off()

# print("finish")

# 1. Show the status of a button on an LED.
# Connect a button to GPIO4 and an LED to GPIO2.
# When the button is pressed the LED should be turned on and when the button is released the LED should be turned off


# import RPi.GPIO as GPIO
# import time
# # 设置编码方式
# GPIO.setmode(GPIO.BOARD)
#
# # 设置GPIO引脚
# GPIO.setup(16, GPIO.OUT)
#
# GPIO.output(16, GPIO.HIGH)
#
# # 等3秒
# time.sleep(3)
#
# # 用16号引脚输出一个低电平，灯灭
# GPIO.output(16, GPIO.LOW)
#
# GPIO.cleanup()
