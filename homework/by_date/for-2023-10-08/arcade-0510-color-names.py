# PREQUISITES: basic famimliarity with drawing simple
# shapes in arcade, including the following commands:
# arcade.open_window, arcade.set_background_color,
# arcade.start_render, arcade.finish_render, arcade.draw_line,
# arcade.draw_rectangle

# EXPLANATION: this should be the first line of code
# in any arcade file. Don't put other code above it.
import arcade
import arcade.csscolor as color

# EXPLANATION:
# The arcade library has a list of color names you can use.
# The list is here:
# https://api.arcade.academy/en/latest/arcade.color.html
# Try clicking on this link while holding down the control key
# or Alt key (not sure which one works on your computer).
# This should open the link in a new tab.

arcade.open_window(600, 600, "My Arcade Game")
arcade.set_background_color(color.BLACK) # black
arcade.start_render()
arcade.draw_rectangle_filled(300, 300, 50, 50, color.WHITE) # white
arcade.finish_render()
arcade.run()

# Question 1:
#
# Try different colors names for the rectangle and background
# colors, finding them in the list at the link above. Try
# at least three different colors for the background and three
# different colors for the rectangle. What colors did you try?

