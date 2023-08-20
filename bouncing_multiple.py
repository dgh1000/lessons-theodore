import arcade
import math
import random

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
SCREEN_TITLE = "Multiple Bouncing Balls Example"
CENTER_X = SCREEN_WIDTH // 2
CENTER_Y = SCREEN_HEIGHT // 2
SPEED = 3

class Ball:
    def __init__(self, position_x, position_y, speed, color):
        self.position_x = position_x
        self.position_y = position_y
        self.speed_x = speed
        self.speed_y = speed
        self.color = color

    def update(self):
        self.position_y += self.speed_y
        self.position_x += self.speed_x
        if self.position_y >= SCREEN_HEIGHT or self.position_y <= 0:
            self.speed_y *= -1
        if self.position_x >= SCREEN_WIDTH or self.position_x <= 0:
            self.speed_x *= -1

    def draw(self):
        arcade.draw_circle_filled(self.position_x, self.position_y, 15, self.color)

class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        pos_x_1 = random.randint(20, SCREEN_WIDTH)
        pos_y_1 = random.randint(24, SCREEN_HEIGHT)
        # implicitly calls __init__
        self.ball1 = Ball(pos_x_1, pos_y_1, 8, arcade.color.LIME)
        self.ball2 = Ball(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT), 7, arcade.color.BLUE)

        # Set background color
        arcade.set_background_color(arcade.color.BLACK)

    def on_update(self, delta_time):
        # Move the rectangle
        self.ball1.update()
        self.ball2.update()

    def on_draw(self):
        """ Render the screen. """

        # Clear screen
        self.clear()
        # Draw the rectangle
        arcade.start_render()
        self.ball1.draw()
        self.ball2.draw()
        # arcade.draw_line(self.ball1.position_x, self.ball1.position_y, self.ball2.position_x, self.ball2.position_y, arcade.color.WHITE, 1)

def main():
    """ Main function """
    MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()
