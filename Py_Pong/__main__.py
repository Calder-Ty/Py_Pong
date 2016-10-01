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

        # # setup
        # Screen = display.Display();
        # speed = [2,2];
        # black = (0,0,0);

        # ball = pygame.image.load('Resources/ball.bmp');
        # ballrect = ball.get_rect();
        # # Main Loop
        # while True:
            
        #     # Event Handlers
        #     for event in pygame.event.get():
        #         if event.type == pygame.QUIT: 
        #             sys.exit();
            
        #     ballrect = ballrect.move(speed);
        #     if ballrect.left < 0 or ballrect.right > Screen._SCREEN_WIDTH:
        #         speed[0] = -speed[0];
        #     if ballrect.top < 0 or ballrect.bottom > Screen._SCREEN_HEIGHT:
        #         speed[1] = -speed[1];
            
        #     Screen.Screen.fill(black);
        #     Screen.Screen.blit(ball,ballrect);
        #     pygame.display.flip();

        #     # Game Logic

            # Render
if __name__ == "__main__":
    Game = Py_PongMain();
    Game.main();
