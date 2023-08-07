import time

x = 0
dir = 1
while True:
    if x >= 10:
        dir = -1
    if x <= 0:
        dir = 1
    x += dir
    print(x)
    time.sleep(0.5)

