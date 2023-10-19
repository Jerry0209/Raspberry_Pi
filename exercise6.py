from gpiozero import PWMLED, Button
from signal import pause
from time import sleep

print("Start!")

button = Button(17)
led = PWMLED(2)

counter = 0


#  Every time click the button, the duty cycle of our PWM should increase by 10%.
def increase_duty_cycle():
    sleep(0.2)  # debouncing
    print("Button is pressed")
    global counter
    counter = counter + 1
    led.value = (counter % 11) * 0.1
    print(led.value)


button.when_pressed = increase_duty_cycle

pause()
