from sense_hat import SenseHat
import time
from signal import pause
import random

hat = SenseHat()
sense = SenseHat()
violet = (200, 0, 200)
red = (255, 0, 0)

X1 = random.randint(0, 7)
Y1 = random.randint(0, 7)


print("hello everyone")

sense.show_message("hello everyone", text_colour = red)

print(" ")
print("BBBBBBBB")
print("B______B")
print("B_R__R_B")
print("B______B")
print("BJ____JB")
print("B_JJJJ_B")
print("B______B")
print("BBBBBBBB")

hat.clear()
hat.set_pixel(0, 0, 0, 0, 255)

hat.set_pixel(1, 0, 0, 0, 255)

hat.set_pixel(2, 0, 0, 0, 255)

hat.set_pixel(3, 0, 0, 0, 255)

hat.set_pixel(4, 0, 0, 0, 255)

hat.set_pixel(5, 0, 0, 0, 255)

hat.set_pixel(6, 0, 0, 0, 255)

hat.set_pixel(7, 0, 0, 0, 255)

hat.set_pixel(0, 7, 0, 0, 255)

hat.set_pixel(1, 7, 0, 0, 255)

hat.set_pixel(2, 7, 0, 0, 255)

hat.set_pixel(3, 7, 0, 0, 255)

hat.set_pixel(4, 7, 0, 0, 255)

hat.set_pixel(5, 7, 0, 0, 255)

hat.set_pixel(6, 7, 0, 0, 255)

hat.set_pixel(7, 7, 0, 0, 255)

hat.set_pixel(0, 1, 0, 0, 255)

hat.set_pixel(0, 2, 0, 0, 255)

hat.set_pixel(0, 3, 0, 0, 255)

hat.set_pixel(0, 4, 0, 0, 255)

hat.set_pixel(0, 5, 0, 0, 255)

hat.set_pixel(0, 6, 0, 0, 255)

hat.set_pixel(0, 7, 0, 0, 255)

hat.set_pixel(7, 1, 0, 0, 255)

hat.set_pixel(7, 2, 0, 0, 255)

hat.set_pixel(7, 3, 0, 0, 255)

hat.set_pixel(7, 4, 0, 0, 255)

hat.set_pixel(7, 5, 0, 0, 255)

hat.set_pixel(7, 6, 0, 0, 255)

hat.set_pixel(7, 7, 0, 0, 255)

hat.set_pixel(2, 2, 200, 0, 0)

hat.set_pixel(5, 2, 200, 0, 0)

hat.set_pixel(2, 5, 200, 200, 0)

hat.set_pixel(5, 5, 200, 200, 0)

hat.set_pixel(3, 5, 200, 200, 0)

hat.set_pixel(4, 5, 200, 200, 0)

hat.set_pixel(6, 4, 200, 200, 0)

hat.set_pixel(1, 4, 200, 200, 0)

time.sleep(5)

hat.clear()

print(" ")
print("go to the red dot")

sense.show_message("go to the red dot", text_colour = violet)

print(" ")
print("Y = ")
print(Y1)
print(" ")
print("X = ")
print(X1)

x = y = 4
hat = SenseHat()

def update_screen():
    hat.clear()
    hat.set_pixel(X1, Y1, 255, 0, 0)
    hat.set_pixel(x, y, 255, 255, 255)
    if Y1 == y :

      if X1 == x :

        print ("well done")
        sense.show_message("well done", text_colour = violet)
        exit()

def clamp(value, min_value=0, max_value=7):
    return min(max_value, max(min_value, value))

def move_dot(event):
    global x, y
    if event.action in ('pressed', 'held'):
        x = clamp(x + {
            'left': -1,
            'right': 1,
            }.get(event.direction, 0))

        y = clamp(y + {
            'up': -1,
            'down': 1,
            }.get(event.direction, 0))


update_screen()
hat.stick.direction_up = move_dot
hat.stick.direction_down = move_dot
hat.stick.direction_left = move_dot
hat.stick.direction_right = move_dot
hat.stick.direction_any = update_screen
pause()
