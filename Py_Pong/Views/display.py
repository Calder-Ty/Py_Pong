import pygame.display;
from Py_Pong.Views.paddleSprite import PaddleSprite


class Display(object):
    """Class for the main screen of the game"""
    _SCREEN_WIDTH = 600;
    _SCREEN_HEIGHT = 400;

    def __init__(self):
        self.Screen = pygame.display.set_mode([self._SCREEN_WIDTH,
                                               self._SCREEN_HEIGHT]);
        pygame.display.set_caption("PyPong!");
        self.Background = pygame.Surface(self.Screen.get_size());
        self.Background.convert();
        self.PlayerSprite = PaddleSprite();

        # REFACTOR: 
        # Currently the Screen is Black, here rather than
        # Setting a black color
        self.Background.fill((0,0,0));
    
        # blit Background onto screen:


    def show(self):
        self.Screen.blit(self.Background, (0,0));
        self.Screen.blit(self.PlayerSprite.image, self.PlayerSprite.rect);
        pygame.display.flip();


    def update(self):
        pass