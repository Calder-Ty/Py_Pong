import pygame.display;


class Display(object):
    """Class for the main screen of the game"""
    _SCREEN_WIDTH = 600;
    _SCREEN_HEIGHT = 400;

    def __init__(self):
        # should Console be public? 
        # Yes it should be but does it need to be 
        # Encapsulated?
        self.Screen = pygame.display.set_mode([self._SCREEN_WIDTH,
                                               self._SCREEN_HEIGHT]);
        pygame.display.set_caption("PyPong!");
        self.Background = pygame.Surface(self.Screen.get_size());
        self.Background.convert();
        self.Background.fill((0,250,0));
    
        # blit Background onto screen:
        self.Screen.blit(self.Background, (0,0));
        pygame.display.flip();

    def update(self):
        pass