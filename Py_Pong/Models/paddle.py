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


    def __init__(self, x, y):
        # X,Y are pos of upper left corner
        self._ready = False;
        self.X = x;
        self.Y = y;
        self._ready = True;

    @property
    def X(self):
        return self._x;

    @X.setter
    def X(self, x):
        if x < 0:
            raise Exception("X is out of bounds");
        self._x = x;
        if self._ready:
            self.onPaddleMove();

    @property
    def Y(self):
        return self._y;
        
    @Y.setter
    def Y(self, y):
        if y < 0:
            raise Exception("Y is out of bounds");
        self._y = y;
        if self._ready:
            self.onPaddleMove();



    ### Events ###
    paddleMoveEvent = Event();
    def onPaddleMove(self):
        Paddle.paddleMoveEvent.call(self, self.X, self.Y);