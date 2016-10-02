import Py_Pong.Views.display as display;
import Py_Pong.Models.game as game;
import Py_Pong.Controlers.paddleController as paddleController
import pygame;
import sys;



class Py_PongMain():


    def main(self):
        # Setup Game
        GameData = game.Game();
        Console = display.Display(GameData);
        Player = paddleController.PaddleController(GameData.PlayerPaddle, GameData.Field_Height);
        Player.setShape(Console.Player_Sprite.rect.width, Console.Player_Sprite.rect.height);
        Computer = paddleController.PaddleController(GameData.ComputerPaddle, GameData.Field_Height);
        Computer.setShape(Console.Computer_Sprite.rect.width, Console.Computer_Sprite.rect.height);
        GameData.ball.setShape(Console.Ball_Sprite.rect.width, Console.Ball_Sprite.rect.height);
        # Handle Events
        while True:
            if pygame.event.get(pygame.QUIT):
                sys.exit();
            pygame.event.pump();
            keys = pygame.key.get_pressed();
            if keys[pygame.K_ESCAPE]:
                sys.exit();
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