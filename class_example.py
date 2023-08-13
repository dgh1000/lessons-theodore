import time
class UpDown:
    def __init__(self):
        self.value = 0
        self.direction = 1
    
    def show(self):
        print(self.value)

    def update(self):
        self.value += self.direction
        if self.value >= 10 or self.value <= 0:
            self.direction *= -1

up_down = UpDown()
while True:
    up_down.update()
    up_down.show()
    time.sleep(0.5)
