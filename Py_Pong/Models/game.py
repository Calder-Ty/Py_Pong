from Py_Pong.Models import paddle, ball;
import time;


class Game(object):

    def __init__(self):

        # Set Field Dimensions 
        self.Field_Width = 900;
        self.Field_Height = 600;
        self.points_player = 0;
        self.points_computer = 0;

        # Give the game some Paddle Objects
        self.PlayerPaddle = paddle.Paddle(self.Field_Width -10 , self.Field_Height/2);
        self.ComputerPaddle = paddle.Paddle(10, self.Field_Height/2);

        # Give the Game a Ball
        self.ball = ball.Ball(self.Field_Width/2,self.Field_Height/2,1,1);

        # 

    def check_Colisions(self):
        # Did it go past the Edge?
        if self.ball.X > self.Field_Width or self.ball.X + self.ball.Width < 0:
            if self.ball.X < 0:
                self.points_player += 1;
            else:
                self.points_computer +=1;
            self.ball.reset(self.Field_Width/2, self.Field_Height/2);

        
        # Did it hit the walls?
        if self.ball.Y + self.ball.Height > self.Field_Height or self.ball.Y < 0:
            self.ball.bounceWall();

        # Did Player Paddle Get collieded with?
        if self.ball.Y <= self.PlayerPaddle.Y + self.PlayerPaddle.Height and\
        self.ball.Y + self.ball.Height >= (self.PlayerPaddle.Y) and\
        (self.ball.X + self.ball.Width) >= self.PlayerPaddle.X:
            self.ball.bouncePaddle();        

        # Did Computer Paddle Get Collided with?
        if self.ball.Y <= self.ComputerPaddle.Y + self.ComputerPaddle.Height and\
        self.ball.Y +self.ball.Height >= (self.ComputerPaddle.Y) and\
        (self.ball.X <= self.ComputerPaddle.X + self.ComputerPaddle.Width):
            self.ball.bouncePaddle();




    def update(self):
        # move the ball
        self.ball.calc_new_pos();
        self.check_Colisions();
        self.ComputerPaddle.movePaddle(self.ball);

    

    

    
