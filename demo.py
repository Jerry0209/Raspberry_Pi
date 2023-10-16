print("Hello world!")

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

from gpiozero import Button
from gpiozero import LED
from time import sleep

led = LED(2)

button = Button(4)

while True:
    if button.is_pressed:
        print("Button is pressed")
        led.on()
    else:
        print("Button is not pressed")
        led.off()



print("finish")
