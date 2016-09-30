from Py_Pong.Models import paddle

class game(object):

    def __init__(self):

        # Give the game some Paddle Objects
        self.PlayerPaddle = paddle.Paddle(300,10);
        self.ComputerPaddle = paddle.Paddle(50,10);
