
class PaddleController(object):
    """ Controls input to Paddle """

    def __init__(self, Paddle, Height):
        self.Paddle = Paddle;
        self.maxY = Height;
    
    def setShape(self, width, height):
        self.Paddle.Width = width;
        self.Paddle.Height = height;
    
    def Move_Up(self):
        if self.Paddle.Y > 0:
            self.Paddle.Y -= 1;

    def Move_Down(self):
        if self.Paddle.Y < self.maxY - self.Paddle.Height:
            self.Paddle.Y += 1;

