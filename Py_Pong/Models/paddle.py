

class Paddle(object):

    def __init__(self, x, y):
        # X,Y are pos of upper left corner
        self.X = x;
        self.Y = y;

    @property
    def X(self):
        return self._x;
    @X.setter
    def X(self, x):
        if x < 0:
            raise Exception("X is out of bounds");
        self._x = x;
    @property
    def Y(self):
        return self._y;
    @Y.setter
    def Y(self, y):
        if y < 0:
            raise Exception("Y is out of bounds");
        self._y = y;