# PREREQUISTES:
# A basic familiarity with drawing simple shapes in arcade, including the
# following commands:
# arcade.open_window, arcade.set_background_color, arcade.start_render,
# arcade.finish_render, arcade.draw_line, arcade.draw_rectangle,
# and use of named colors.
#
# Basic familiarity with lists, for loops, and range.

# TOPICS COVERED:
# 1) How to make a list of colors
# 2) Drawing multiple rectangles using a for loop
# 3) Drawing primitives API for draw_rectangle_filled
# 4) Looking up drawing primitives API in the arcade documentation
#    for other commands


# EXPLANATION:
# Here you can look up drawing primitives (commands) and their
# list of arguments and the meaning of the arguments: Use ctrl-click,
# alt-click, or option-click on this link depending on what kind of
# computer you have:
# https://api.arcade.academy/en/latest/api/drawing_primitives.html


import arcade
import arcade.csscolor as color
import random

# colors = [color.FLORAL_WHITE, color.GOLDENROD, color.HOTPINK, color.INDIANRED, color.KHAKI, color.LAVENDER]
colors = [color.FLORAL_WHITE, color.GOLDENROD, color.HOTPINK, color.INDIANRED,]
# random_numbers = [100, 200, 300]
arcade.open_window(600, 600, "My Arcade Game")
arcade.set_background_color(color.BLACK) 
arcade.start_render()
x = 100
y = 100
# for i in range(6): # just to count six loops
#     c = random.choice(colors)
#     arcade.draw_rectangle_filled(x, y, 60, 60, c) 
#     x = random.choice(list(range(0, 600, 100)))
#     y = random.choice(list(range(600)))

for x in range(0, 600, 100):
    for y in range(0, 600, 100):
        c = random.choice(colors)
        arcade.draw_rectangle_filled(x, y, 60, 60, c)
# (100, 100), (100, 200), (200, 300)

arcade.finish_render()
arcade.run()

# Question 1:

# Modify this program to draw larger rectangles.
# Ok

# Question 2:
# Ok
# Modify this program to draw rectangles in a horizontal row, instead of a diagonal.

# Question 3:
#Ok
# Modify this program to draw rectangles in a vertical row.

# Question 4:
#Ok
# Modify this program to draw the rectangles further apart.

