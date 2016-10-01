import pygame.sprite;
import pygame.image;


class PaddleSprite(pygame.sprite.Sprite):

    def __init__(self, paddle):
        super().__init__();

        self.image = pygame.image.load("Resources/paddle.bmp");
        self.rect = self.image.get_rect();
        self.__paddle = paddle
        self.rect.x = paddle.X;
        self.rect.y = paddle.Y;
        paddle.paddleMoveEvent += self.update_pos

    def update_pos(self, subject, x, y):
        self.rect.x = x;
        self.rect.y = y;

    def close(self, subject):
        __paddle.paddleMoveEvent -= self




