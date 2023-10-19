from gpiozero import Button, LED
from signal import pause
from time import sleep

print("Start!")
# 定义按钮和 LED 的引脚 #define Pin and LED
button = Button(2)
button2 = Button(17)

leds = [LED(5), LED(6), LED(13), LED(19)]

storeCount = [0, 0, 0, 0, 0]

# 初始化一个计数器变量 # initialize a counter
counter = 0
store = 0


# 函数：根据计数值更新 LED 状态 # use counter to update LED
def update_leds():
    for i in range(4):
        leds[i].value = (counter >> i) & 1  # counter right move i bit then LSB "and" with 1 = whether LSB is 0 or 1
        # decimal 10 = binary 1010
        # leds[0] = 0 & 1 = 0       right move 0 bit
        # leds[1] = 1 & 1 = 1       right move 1 bit
        # leds[2] = 0 & 1 = 0       right move 2 bit
        # leds[3] = 1 & 1 = 1       right move 3 bit


def average():
    avg = round(sum(storeCount) / 5)
    for i in range(4):
        leds[i].value = (avg >> i) & 1  # leds.value is used to set LED status, not like array


# 函数：按下按钮时递增计数器并更新 LED when button is pressed, up-count
def on_button_click():
    sleep(0.2)  # debouncing
    global counter
    counter = (counter + 1) % 16
    print("Button is pressed")
    global store
    store = (store + 1) % 5  # initial value is zero and after 1 click is 1
    storeCount[store] = counter

    update_leds()


def on_button2_click():
    sleep(0.2)  # debouncing
    print("Button2 is pressed")
    average()


# 当按下按钮时，调用 on_button_click 函数  when button is pressed, call this function

button.when_pressed = on_button_click
button2.when_pressed = on_button2_click

# not below
# if button.is_pressed:
#     on_button_click()
# elif button2.is_pressed:
#     on_button2_click()
# else:
#     pass

# 初始化 LED   initialize LED
update_leds()

# 保持程序运行    Running programme
pause()

