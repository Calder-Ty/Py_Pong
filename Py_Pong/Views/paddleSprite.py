import pygame.sprite;
import pygame.image;

class PaddleSprite(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__();

        # Add additional info about the Sprite
        self.image = pygame.image.load("Resources/paddle.bmp");
        self.rect = self.image.get_rect();
    



