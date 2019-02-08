import arcade
 
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
 
class SnakeWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
 
        arcade.set_background_color(arcade.color.BLACK)
        self.snake_sprite = arcade.Sprite('images/block.png')
        self.snake_sprite.set_position(300,300)
        
    def on_draw(self):
        arcade.start_render()
 
        self.snake_sprite.draw()
 
def main():
    window = SnakeWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()
 
if __name__ == '__main__':
    main()