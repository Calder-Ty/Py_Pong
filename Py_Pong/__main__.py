import Py_Pong.Views.display as display;
import pygame;
import sys;

class Py_PongMain():

    def main(self):
        Console = display.Display();
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit();
            
            # Handle Events

            # Update Game Data with Logic

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
