import pygame.sprite;
import pygame.image;


class BallSprite(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__();

        self.image = pygame.image.load("Resources/ball.bmp");
        self.rect = self.image.get_rect();

    def update_pos(self, x, y):
        self.rect.x = x
        self.rect.y = y;
