import pygame.display;
import pygame.font;
from Py_Pong.Views.ballSprite import BallSprite
from Py_Pong.Views.paddleSprite import PaddleSprite


class Display(object):
    """Class for the main screen of the game"""
    #_SCREEN_WIDTH = 600;
    #_SCREEN_HEIGHT = 400;

    def __init__(self, GameData):
        pygame.font.init();
        self.Screen = pygame.display.set_mode([GameData.Field_Width, GameData.Field_Height]);
        pygame.display.set_caption("PyPong!");
        self.Background = pygame.Surface(self.Screen.get_size());
        self.Background.convert();
        self.Ball_Sprite = BallSprite(GameData.ball);
        self.Player_Sprite = PaddleSprite(GameData.PlayerPaddle);
        self.Computer_Sprite = PaddleSprite(GameData.ComputerPaddle);
        self.Score = pygame.font.SysFont('lucidasans', 15);
        self.GameData = GameData

        # REFACTOR: 
        # Currently the Screen is Black, here rather than
        # Setting a black color
        self.Background.fill((0,0,0));

    def show(self):
        labelText = "Computer: " + str(self.GameData.points_computer) + "    Player: " + str(self.GameData.points_player);
        label = self.Score.render(labelText, 1, (0,255,0));
        self.Screen.blit(self.Background, (0,0));
        self.Screen.blit(self.Ball_Sprite.image, self.Ball_Sprite.rect);
        self.Screen.blit(self.Player_Sprite.image, self.Player_Sprite.rect);
        self.Screen.blit(self.Computer_Sprite.image, self.Computer_Sprite);
        self.Screen.blit(label, (0, 0))
        pygame.display.flip();


    def update(self):
        pass