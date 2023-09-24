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

# two things that coding can do:
# - remember things (variables)
# - run code (do things)

# make an object out of a class
# TheQuickFoxJumpedOverTheLazyDog
# SphinxOfBlackQuartzJudgeMyVow
# sphinx_of_black_quartz_judge_my_vow

# create it. it creates the memory (it creates the variable)
up_down = UpDown()
while True:
    up_down.update()
    up_down.show()
    time.sleep(0.5)

# val = 1
# direction = 1
# while True:
#     if val >= 10:
#         # we have to adjust val and direction
#         val = 10
#         direction =-1
#     elif val < 1:
#         val = 0
#         direction =1
#     val += direction
#     time.sleep(0.5)
#     print(val)