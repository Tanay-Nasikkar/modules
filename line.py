import math

#lol
class Line:
    _x_intercept: float = None
    _y_intercept: float = None
    _slope: float = None

    def __init__(self, *, x_intercept: float = None, y_intercept: float = None, slope: float = None, point_on_line: tuple = None):
        self.x_intercept = x_intercept
        self.y_intercept = y_intercept
        self.slope = slope

        if point_on_line is not None:
            try:
                self.point_slope(point_on_line, self.slope)

            except ValueError:
                if (x_intercept := self.x_intercept) is not None:
                    point = (x_intercept, 0)

                elif (y_intercept := self.y_intercept) is not None:
                    point = (0, y_intercept)

                else:
                    raise ValueError(
                        'You should give a Slope, X Intercept, or Y Intercept too, if you are giving a point_on_line.')

                self.from_two_points(point, point_on_line)

    def __repr__(self):
        return f"y = x({self.slope}) + {self.y_intercept}"

    def __copy__(self):
        new_line = self.__class__()

        new_line._x_intercept = self._x_intercept
        new_line._y_intercept = self._y_intercept
        new_line._slope = self._slope

        return new_line

    @property
    def x_intercept(self):
        if self._x_intercept is not None:
            return self._x_intercept

        if self._y_intercept is not None and self._slope is not None:
            # y = mx + b, where b is the y intercept.
            # y - b = mx
            # (y - b)/m = x

            self._x_intercept = -self._y_intercept / slope \
                if (slope := self._slope) != 0 \
                else math.nan  # When y = 0
            return self._x_intercept

        else:
            raise ValueError(
                "Y Intercept and Slope should not be None, in order to find X Intercept.")

    @x_intercept.setter
    def x_intercept(self, x_intercept: float | None):
        if x_intercept is None:
            self._x_intercept = None
            return

        if self._y_intercept is not None and self._slope is not None:
            raise ValueError(
                'Cannot change X Intercept when both Y Intercept and Slope are set.\nTry changing at least any one of them to None.'
            )

        self._x_intercept = x_intercept

    @property
    def y_intercept(self):
        if self._y_intercept is not None:
            return self._y_intercept

        if self._x_intercept is not None and self._slope is not None:
            # y/x = m
            # x/y = 1/m
            #x = y/m
            # x = y/m + c, where c is the x intercept.
            # x - c = y/m
            # m(x - c) = y

            self._y_intercept = -self._slope * self._x_intercept  # When x = 0
            return self._y_intercept

        else:
            raise ValueError(
                "X Intercept and Slope should not be None, in order to find Y Intercept.")

    @y_intercept.setter
    def y_intercept(self, y_intercept: float | None):
        if y_intercept is None:
            self._y_intercept = None
            return

        if self._x_intercept is not None and self._slope is not None:
            raise ValueError(
                'Cannot change Y Intercept when both X Intercept and Slope are set.\nTry changing at least any one of them to None.'
            )

        self._y_intercept = y_intercept

    @property
    def slope(self):
        if self._slope is not None:
            return self._slope

        # (0,b), where b is the y intercept.
        # (c,0), where c is the x intercept.
        # (b-0)/(0-c) = m, where m is the slope.
        #m = -b/c

        try:
            self._slope = - self.y_intercept / x_intercept \
                if (x_intercept := self.x_intercept) != 0 \
                else math.inf
            return self._slope

        except ValueError:
            raise ValueError(
                "Both X and Y Intercepts must be set in order to calculate slope.")

    @slope.setter
    def slope(self, slope: float | None):
        if slope is None:
            self._slope = None
            return

        if self._x_intercept is not None and self._y_intercept is not None:
            raise ValueError(
                'Cannot change Slope when both X and Y Intercept are set.\nTry changing at least any one of them to None.'
            )

        self._slope = slope

    def get_x(self, y: float):
        # y = mx + b
        # x = (y - b)/m

        return (y - self.y_intercept)/slope \
            if (slope := self.slope) != 0 \
            else math.inf

    def get_y(self, x: float):
        # y = mx + b

        return self.slope * x + self.y_intercept

    def point_slope(self, point: tuple, slope: float):
        self.x_intercept = None
        self.slope = slope

        # (y - y₁)/(x - x₁) = m, where m is the slope.
        # y - y₁ = m(x - x₁)
        # y = mx - mx₁ + y₁

        x_1, y_1 = point
        self.y_intercept = y_1 - slope*x_1  # When x = 0

        return self

    def from_two_points(self, point_1: tuple, point_2: tuple):
        x_1, y_1 = point_1
        x_2, y_2 = point_2

        slope = (y_2 - y_1) / run \
            if (run := (x_2-x_1)) != 0 \
            else math.inf

        return self.point_slope(point_1, slope)  # or point_2, slope

    def rotate(self, pivot: tuple, angle: float):
        '''
        Angle should be in radians.
        '''

        prev_angle = math.atan(self.slope)

        slope = math.tan(new_angle := (prev_angle + angle))

        self.point_slope(pivot, slope)

        return new_angle

    def rotate_deg(self, pivot: tuple, angle: float):
        '''
        Angle should be in degrees.
        '''

        return math.degrees(
            self.rotate_rad(
                pivot,
                math.radians(angle)
            )
        )

    rotate_radian = rotate_radians = rotate_rad = rotate
    rotate_degree = rotate_degrees = rotate_deg

    def copy(self):
        return self.__copy__()
