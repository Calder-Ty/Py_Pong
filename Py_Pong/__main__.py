import Py_Pong.Views.display as display;
import Py_Pong.Models.game as game;
import Py_Pong.Controlers.paddleController as paddleController
import pygame;
import sys;



class Py_PongMain():


    def main(self):
        GameData = game.Game();
        print(GameData.PlayerPaddle.X)
        Console = display.Display(GameData);
        Player = paddleController.PaddleController(GameData.PlayerPaddle)
        
        # Handle Events
        while True:
            if pygame.event.get(pygame.QUIT):
                sys.exit();
            pygame.event.pump();
            keys = pygame.key.get_pressed();
            if keys[pygame.K_UP]:
                Player.Move_Up();
            if keys[pygame.K_DOWN]:
                Player.Move_Down();
            
            

            # Update Game Data with Logic
            GameData.update();

            # Display Console
            Console.show();


if __name__ == "__main__":
    app = Py_PongMain();
    app.main();