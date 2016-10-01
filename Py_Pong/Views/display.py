import pygame.display;
from Py_Pong.Views.ballSprite import BallSprite


class Display(object):
    """Class for the main screen of the game"""
    #_SCREEN_WIDTH = 600;
    #_SCREEN_HEIGHT = 400;

    def __init__(self, width, height):
        self.Screen = pygame.display.set_mode([width, height]);
        pygame.display.set_caption("PyPong!");
        self.Background = pygame.Surface(self.Screen.get_size());
        self.Background.convert();
        self.Ball_Sprite = BallSprite();

        # REFACTOR: 
        # Currently the Screen is Black, here rather than
        # Setting a black color
        self.Background.fill((0,0,0));

    def show(self):
        self.Screen.blit(self.Background, (0,0));
        self.Screen.blit(self.Ball_Sprite.image, self.Ball_Sprite.rect);
        pygame.display.flip();


    def update(self):
        pass