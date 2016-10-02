from math import sin, cos, pi;
from Py_Pong.events import Event;

class Ball(object):
    """
    A Ball that moves across the screen.

    Returns: Ball object
    @Methods
    calc_new_pos
    @Attributes 
    X
    Y
    _vector: Holds information for movement
    """
    ### MAGIC METHODS ###
    def __init__(self,x:int,y:int,angle:float,speed:int):
        """
        Initalizes Ball Obect
        x: Sets Initial X coord
        y: Sets Initial Y coord
        angle: Sets angle component for _vector, in Radians
        speed: sets Speed component for _vector
        """
        self.X = x;
        self.Y = y;
        self.Width = 1;
        self.Height = 1;
        self._vector = (angle, speed);
        self.isHit = False;
    ### PROPERTIES ### 
    @property
    def X(self):
        return self._x;
    
    @X.setter
    def X(self, x):
        self._x = x;

    @property
    def Y(self):
        return self._y;
    
    @Y.setter
    def Y(self,y):
        self._y = y;

    
    ### EVENTS ###
    calcNewPosEvent = Event();
    def OnCalcNewPosEvent(self):
        Ball.calcNewPosEvent.call(self, self.X, self.Y);
    ### METHODS ###
    def calc_new_pos(self)->None:
        """ Calculates new X and Y coordinates """
        angle, z = self._vector;
        (dx,dy) = (z*cos(angle), z*sin(angle));
        self.X += dx;
        self.Y += dy;
        self.OnCalcNewPosEvent();

    def bounceWall(self)->None:
        """ Changes Angle To Bounce """
        self._vector = -self._vector[0], self._vector[1];

    def bouncePaddle(self)->None:
        """ Bounce off of Paddle """
        self._vector = (self._vector[0] + pi/2), self._vector[1];
        print(self._vector[0])

    def setShape(self, width, height)->None:
        """ Sets the Shape of Ball """
        self.Width = width;
        self.Height = height;

    def reset(self, X, Y):
        self.X = X;
        self.Y = Y;
        self._vector = pi-self._vector[0], self._vector[1]




    
