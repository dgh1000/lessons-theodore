import arcade
import math
import random

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Bouncing example"
CENTER_X = SCREEN_WIDTH // 3
CENTER_Y = SCREEN_HEIGHT // 2
SPEED = 5

class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.x = random.randint(9, SCREEN_WIDTH)
        self.y = random.randint(99, SCREEN_HEIGHT)
        self.x_direction = SPEED
        self.y_direction = SPEED

        # Set background color
        arcade.set_background_color(arcade.color.LIME_GREEN)

    def on_update(self, delta_time):
        # Move the rectangle
        if self.x <= 0:
            self.x_direction = 2
        elif self.x >= SCREEN_WIDTH:
            self.x_direction = -50
        self.x = self.x_direction + self.x
        if self.y <= 0:
            self.y_direction = 25
        elif self.y >= SCREEN_HEIGHT:
            self.y_direction = -2
        self.y = self.y_direction + self.y

    def on_draw(self):
        """ Render the screen. """
        
        # Clear screen
        self.clear()
        # Draw the rectangle
        arcade.start_render()
        arcade.draw_rectangle_filled(self.x, self.y, 50, 50, arcade.color.RED_DEVIL)

def main():
    """ Main function """
    MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()

