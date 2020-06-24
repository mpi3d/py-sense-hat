from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
import time
import random
sense = SenseHat()
sense.clear()
sense.set_rotation(270)
sense.low_light = True
sense.set_imu_config(True, False, False)

s = 200

def pushed_up(event):
    global xh
    global zz
    if event.action != ACTION_RELEASED:
        xh = xh + 1
        if xh > 5 :
            xh = 5
        else :
            zz = 0

def pushed_down(event):
    global xh
    global zz
    if event.action != ACTION_RELEASED:
        xh = xh - 1
        if xh < 1 :
            xh = 1
        else :
            zz = 0

def pushed_left(event):
    global yh
    global zz
    if event.action != ACTION_RELEASED:
        yh = yh - 1
        if yh < 1 :
            yh = 1
        else :
            zz = 0

def pushed_right(event):
    global yh
    global zz
    if event.action != ACTION_RELEASED:
        yh = yh + 1
        if yh > 5 :
            yh = 5
        else :
            zz = 0

def re():
    global p1,p2,p3,p4,p5
    global r1,r2,r3,r4,r5
    global xh,yh
    global zz,zzz
    sense.clear()
    u = 7
    while u > 0 :
        if r3 < u :
            sense.set_pixel(u,7,255,255,255)
        if p3 < u :
            sense.set_pixel(7,u,255,255,255)
        u = u - 1
    sense.set_pixel(r3,7,255,255,255)
    sense.set_pixel(7,p3,255,255,255)
    sense.set_pixel(xh - 1,yh,0,0,255)
    sense.set_pixel(xh,yh - 1,0,0,255)
    sense.set_pixel(xh,yh + 1,0,0,255)
    sense.set_pixel(xh + 1,yh,0,0,255)
    p4 = p3
    r4 = r3
    zz = 1

while True :
    sense.clear()
    xh = 3
    yh = 3
    raw = sense.get_compass_raw()
    a = ("{x}.{y}.{z}".format(**raw))
    p,p0,r,r0,y,y0 = a.split(".")
    p3 = round(int(p) * 7 / -52)
    r3 = round(int(r) * 7 / -52)
    if p3 > 7 :
        p3 = 7
    elif p3 < 0 :
        p3 = 0
    if r3 > 7 :
        r3 = 7
    elif r3 < 0 :
        r3 = 0
    p4 = p3
    r4 = r3
    zz = 1
    zzz = 0
    u = 7
    sense.show_message("Visibilite : " + str(s), text_colour=[0, 255, 0],scroll_speed=(0.06))
    while u > 0 :
        if r3 < u :
            sense.set_pixel(u,7,255,255,255)
        if p3 < u :
            sense.set_pixel(7,u,255,255,255)
        u = u - 1
        time.sleep(0.05)
    sense.set_pixel(xh - 1,yh,0,0,255)
    time.sleep(0.05)
    sense.set_pixel(xh,yh - 1,0,0,255)
    time.sleep(0.05)
    sense.set_pixel(xh + 1,yh,0,0,255)
    time.sleep(0.05)
    sense.set_pixel(xh,yh + 1,0,0,255)
    p1 = random.randint(-52,32)
    r1 = random.randint(-52,32)
    i = True
    while i :
        raw = sense.get_compass_raw()
        a = ("{x}.{y}.{z}".format(**raw))
        p,p0,r,r0,y,y0 = a.split(".")
        sense.stick.direction_up = pushed_up
        sense.stick.direction_down = pushed_down
        sense.stick.direction_left = pushed_left
        sense.stick.direction_right = pushed_right
        p3 = round(int(p) * 7 / -52)
        r3 = round(int(r) * 7 / -52)
        if p3 > 7 :
            p3 = 7
        elif p3 < 0 :
            p3 = 0
        if r3 > 7 :
            r3 = 7
        elif r3 < 0 :
            r3 = 0
        if  int(p1) + s > int(p) and int(p1) - s < int(p) and int(r1) + s > int(r) and int(r1) - s < int(r) :
            p2 = round(int(p) * 3 / int(p1))
            r2 = round(int(r) * 3 / int(r1))
            if zzz == 0 :
                p5 = p2
                r5 = r2
                zzz = 1
            if p2 > 6 or p2 < 0 or r2 > 6 or r2 < 0 :
                zz = 0
                re()
            else :
                if zz == 0 or p5 != p2 or r5 != r2 or p3 != p4 or r3 != r4:
                    re()
                    sense.set_pixel(r2,p2,255,0,0)
                    p5 = p2
                    r5 = r2
                if p2 == yh and r2 == xh :
                    time.sleep(0.1)
                    sense.set_pixel(xh - 1,yh,255,0,0)
                    time.sleep(0.1)
                    sense.set_pixel(xh,yh - 1,255,0,0)
                    time.sleep(0.1)
                    sense.set_pixel(xh + 1,yh,255,0,0)
                    time.sleep(0.1)
                    sense.set_pixel(xh,yh + 1,255,0,0)
                    sense.set_pixel(xh,yh,0,0,0)
                    time.sleep(0.1)
                    m = random.randint(20,50)
                    randlis = []
                    while m > 0 :
                        xra = random.randint(0,6)
                        yra = random.randint(0,6)
                        randlis.append(xra)
                        randlis.append(yra)
                        sense.set_pixel(xra,yra,random.randint(150,255),random.randint(50,100),0)
                        sense.set_pixel(xh - 1,yh,255,0,0)
                        sense.set_pixel(xh,yh - 1,255,0,0)
                        sense.set_pixel(xh,yh + 1,255,0,0)
                        sense.set_pixel(xh + 1,yh,255,0,0)
                        m = m - 1
                        time.sleep(0.005)
                    while len(randlis) > 0 :
                        sense.set_pixel(randlis[0],randlis[1],0,0,0)
                        sense.set_pixel(xh - 1,yh,255,0,0)
                        sense.set_pixel(xh,yh - 1,255,0,0)
                        sense.set_pixel(xh,yh + 1,255,0,0)
                        sense.set_pixel(xh + 1,yh,255,0,0)
                        del randlis[0]
                        del randlis[0]
                        time.sleep(0.005)
                    time.sleep(0.1)
                    sense.set_pixel(xh - 1,yh,0,255,0)
                    sense.set_pixel(xh,yh - 1,0,255,0)
                    sense.set_pixel(xh,yh + 1,0,255,0)
                    sense.set_pixel(xh + 1,yh,0,255,0)
                    time.sleep(0.1)
                    sense.set_pixel(xh - 1,yh,0,0,0)
                    time.sleep(0.1)
                    sense.set_pixel(xh,yh - 1,0,0,0)
                    time.sleep(0.1)
                    sense.set_pixel(xh + 1,yh,0,0,0)
                    time.sleep(0.1)
                    sense.set_pixel(xh,yh + 1,0,0,0)
                    s = round(s / 2)
                    i = False
        elif p3 != p4 or r3 != r4 or zz == 0:
            re()
        time.sleep(0.1)
