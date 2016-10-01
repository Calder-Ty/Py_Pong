import Py_Pong.Views.display as display;
import Py_Pong.Models.game as game;
import pygame;
import sys;

class Py_PongMain():

    def main(self):
        GameData = game.Game();
        Console = display.Display(GameData.Field_Width, GameData.Field_Height);
        
        # Handle Events
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit();
            
            

            # Update Game Data with Logic
            GameData.update();
            Console.Ball_Sprite.update_pos(x =GameData.ball.X, y =GameData.ball.Y);

            # Display Console
            Console.show();


if __name__ == "__main__":
    app = Py_PongMain();
    app.main();