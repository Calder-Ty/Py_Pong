from Py_Pong.Models import paddle, ball;


class Game(object):

    def __init__(self):

        # Set Field Dimensions 
        self.Field_Width = 900;
        self.Field_Height = 600;

        # Give the game some Paddle Objects
        self.PlayerPaddle = paddle.Paddle(self.Field_Width -10 , self.Field_Height/2);
        self.ComputerPaddle = paddle.Paddle(self.Field_Width - 10, self.Field_Height/2);

        # Give the Game a Ball
        self.ball = ball.Ball(self.Field_Width/2,self.Field_Height/2,0,1);

                
    
    def update(self):
        # move the ball
        self.ball.calc_new_pos();
        if self.ball.X > self.Field_Width or self.ball.X < 0:
            raise Exception("Balls X position Is out Of Bounds!");
        if self.ball.Y > self.Field_Height or self.ball.Y <0:
            raise Exception("Balls Y position Is Out of Bounds!");
    

    

    
