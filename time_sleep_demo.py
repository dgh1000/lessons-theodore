import time

x = 0
dir = 1
while True:
    if x >= 5:
        dir = -1
    if x <= 0:
        dir = 1
    x += dir
    print(x)
    time.sleep(1)

