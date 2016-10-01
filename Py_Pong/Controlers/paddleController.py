
class PaddleController(object):
    """ Controls input to Paddle """

    def __init__(self, Paddle):
        self.Paddle = Paddle
    
    def Move_Up(self):
        self.Paddle.Y -= 1

    def Move_Down(self):
        self.Paddle.Y += 1

