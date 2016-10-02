import time;
from Py_Pong.events import Event;


class Paddle(object):
    """
    Object to represent Paddle

    @Methods:
    onPaddleMove
    @Properties:
    X
    Y 
    """
    timebetweenMoves = 4; 

    def __init__(self, x, y):
        # X,Y are pos of upper left corner
        self._ready = False;
        self.X = x;
        self.Y = y;
        self.Width = 1;
        self.Height = 1;
        self._ready = True;
        self.timeAtNextMove = 0

    @property
    def X(self):
        return self._x;

    @X.setter
    def X(self, x):
        self._x = x;
        if self._ready:
            self.onPaddleMove();

    @property
    def Y(self):
        return self._y;
        
    @Y.setter
    def Y(self, y):
        self._y = y;
        if self._ready:
            self.onPaddleMove();



    ### Events ###
    paddleMoveEvent = Event();
    def onPaddleMove(self):
        Paddle.paddleMoveEvent.call(self, self.X, self.Y);

    def movePaddle(self, Ball):
        """ Computer's Algorithim to Move Paddle """
        Center = Ball.Y + Ball.Height/2;
        if Center > self.Y + self.Height/2 and self.checkTime():
            self.Y += 1;
            self.timeAtNextMove = time.time() + self.timebetweenMoves/1000;
        if Center < self.Y + self.Height/2 and self.checkTime():
            self.Y -= 1;
            self.timeAtNextMove = time.time() + self.timebetweenMoves/1000;
    
    def checkTime(self)->bool:
        if time.time() > self.timeAtNextMove:
            return True;
        else:
            return False;

    def reset(self, X, Y):
        self.X = X;
        self.Y = Y;