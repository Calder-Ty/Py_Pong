from math import sin, cos;
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
        self._vector = (angle, speed);

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


    
