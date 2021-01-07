from sense_hat import SenseHat
import time
import random
sense = SenseHat()
sense.clear()
sense.set_rotation(180)
sense.low_light = True
sense.set_imu_config(False, False, True)

s = 30

b = [255,255,255]

n = [0,0,0]

d1 = [n,n,n,n,n,n,n,n,
      n,n,n,n,n,n,n,n,
      n,n,n,n,n,n,n,n,
      n,n,n,b,b,n,n,n,
      n,n,n,b,b,n,n,n,
      n,n,n,n,n,n,n,n,
      n,n,n,n,n,n,n,n,
      n,n,n,n,n,n,n,n]

d2 = [b,b,n,n,n,n,n,n,
      b,b,n,n,n,n,n,n,
      n,n,n,n,n,n,n,n,
      n,n,n,n,n,n,n,n,
      n,n,n,n,n,n,n,n,
      n,n,n,n,n,n,n,n,
      n,n,n,n,n,n,b,b,
      n,n,n,n,n,n,b,b]

d3 = [b,b,n,n,n,n,n,n,
      b,b,n,n,n,n,n,n,
      n,n,n,n,n,n,n,n,
      n,n,n,b,b,n,n,n,
      n,n,n,b,b,n,n,n,
      n,n,n,n,n,n,n,n,
      n,n,n,n,n,n,b,b,
      n,n,n,n,n,n,b,b]

d4 = [b,b,n,n,n,n,b,b,
      b,b,n,n,n,n,b,b,
      n,n,n,n,n,n,n,n,
      n,n,n,n,n,n,n,n,
      n,n,n,n,n,n,n,n,
      n,n,n,n,n,n,n,n,
      b,b,n,n,n,n,b,b,
      b,b,n,n,n,n,b,b]

d5 = [b,b,n,n,n,n,b,b,
      b,b,n,n,n,n,b,b,
      n,n,n,n,n,n,n,n,
      n,n,n,b,b,n,n,n,
      n,n,n,b,b,n,n,n,
      n,n,n,n,n,n,n,n,
      b,b,n,n,n,n,b,b,
      b,b,n,n,n,n,b,b]

d6 = [b,b,n,n,n,n,b,b,
      b,b,n,n,n,n,b,b,
      n,n,n,n,n,n,n,n,
      b,b,n,n,n,n,b,b,
      b,b,n,n,n,n,b,b,
      n,n,n,n,n,n,n,n,
      b,b,n,n,n,n,b,b,
      b,b,n,n,n,n,b,b]

accel_only = sense.get_accelerometer()
a = ("{pitch}.{roll}.{yaw}".format(**accel_only))
p,p0,r,r0,y,y0 = a.split(".")
p1 = p
r1 = r
y1 = y
while True :
    accel_only = sense.get_accelerometer()
    a = ("{pitch}.{roll}.{yaw}".format(**accel_only))
    p,p0,r,r0,y,y0 = a.split(".")
    if int(p) + s < int(p1) or int(p) - s > int(p1) or int(r) + s < int(r1) or int(r) - s > int(r1) or int(y) + s < int(y1) or int(y) - s > int(y1) :
        i = random.randint(10,20)
        while i > 0 :
            w = random.randint(1,6)
            if w == 1 :
                sense.set_pixels(d1)
            elif w == 2 :
                sense.set_pixels(d2)
            elif w == 3 :
                sense.set_pixels(d3)
            elif w == 4 :
                sense.set_pixels(d4)
            elif w == 5 :
                sense.set_pixels(d5)
            elif w == 6 :
                sense.set_pixels(d6)
            t = 0.5 / i
            time.sleep(t)
            i = i - 1
        i = 5
        while i > 0 :
            time.sleep(0.2)
            sense.clear()
            time.sleep(0.2)
            if w == 1 :
                sense.set_pixels(d1)
            elif w == 2 :
                sense.set_pixels(d2)
            elif w == 3 :
                sense.set_pixels(d3)
            elif w == 4 :
                sense.set_pixels(d4)
            elif w == 5 :
                sense.set_pixels(d5)
            elif w == 6 :
                sense.set_pixels(d6)
            i = i - 1
        accel_only = sense.get_accelerometer()
        a = ("{pitch}.{roll}.{yaw}".format(**accel_only))
        p,p0,r,r0,y,y0 = a.split(".")
        p1 = p
        r1 = r
        y1 = y
    time.sleep(0.01)
