# PREQUISITES: basic famimliarity with drawing simple
# shapes in arcade, including the following commands:
# arcade.open_window, arcade.set_background_color,
# arcade.start_render, arcade.finish_render, arcade.draw_line,
# arcade.draw_rectangle

# EXPLANATION: this should be the first line of code
# in any arcade file. Don't put other code above it.
import arcade

arcade.open_window(600, 600, "My Arcade Game")
arcade.set_background_color((0, 0, 0)) # black
arcade.start_render()
arcade.draw_rectangle_filled(300, 300, 50, 50, (255, 255, 255)) # white
arcade.finish_render()
arcade.run()

# Question 0:
# Please retype the code above to get it under your fingers. Pay attention to
# the order of commands, the spelling of commands. Then delete the code
# above and use the code you typed for the rest of the exercise.

# Question 1: Why does (0, 0, 0) produce black and
# (255, 255, 255) produce white?
#
# Hint: remember that the three numbers are the red strength
# (0-255), green strength (0-255), and blue strength (0-255).
# The three numbers are called "RGB" for short.

# Question 2: What color is (255, 0, 0)? What color is
# (0, 255, 0)? What color is (0, 0, 255)? What color is
# (255, 255, 0)? What color is (255, 0, 255)? What color is
# (0, 255, 255)?
# Answer this by changing the color in the draw_rectangle_filled
# command above and running the program.


