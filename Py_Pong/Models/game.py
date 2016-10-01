from Py_Pong.Models import paddle, ball;


class Game(object):

    def __init__(self):

        # Give the game some Paddle Objects
        self.PlayerPaddle = paddle.Paddle(300,10);
        self.ComputerPaddle = paddle.Paddle(50,10);

        # Give the Game a Ball
        self.ball = ball.Ball(150,150,0,1);

        # Set Field Dimensions 
        self.Field_Width = 900;
        self.Field_Height = 600;
        
    
    def update(self):
        # move the ball
        self.ball.calc_new_pos();
        if self.ball.X > self.Field_Width or self.ball.X < 0:
            raise Exception("Balls X position Is out Of Bounds!");
        if self.ball.Y > self.Field_Height or self.ball.Y <0:
            raise Exception("Balls Y position Is Out of Bounds!");
        
    

    

    
