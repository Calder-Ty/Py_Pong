import pygame.sprite;
import pygame.image;


class BallSprite(pygame.sprite.Sprite):

    def __init__(self, Ball):
        super().__init__();

        self.image = pygame.image.load("Resources/ball.bmp");
        self.rect = self.image.get_rect();
        Ball.calcNewPosEvent += self.update_pos;

    def update_pos(self, subject, x, y):
        self.rect.x = x;
        self.rect.y = y;

    def close(self):
        Ball.calcNewPosEvent -= self.update_pos;
