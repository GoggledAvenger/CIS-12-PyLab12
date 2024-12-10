import math, turtle

class Planet:
    """spherical heavenly body with relatively clear orbit"""

    def __init__(self,
                 name:str,
                 mass:float,
                 position_x:float,
                 position_y:float,
                 velocity_x:float,
                 velocity_y:float,
                 color:str='black'
                 ):
        self.name = name
        self.mass = mass
        self.distance = position_x
        self.position_x = position_x
        self.position_y = position_y
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        # graphics
        self.t = turtle.Turtle()
        self.t.shape('circle')
        self.t.color(color)
        # initial positioning of planet
        self.t.penup()
        self.t.goto(self.position_x, self.position_y)
        self.t.pendown()

    def get_mass(self) -> float:
        return self.mass

    def get_distance(self) -> float:
        return self.distance

    @staticmethod
    def set_distance(planet, sun_x, sun_y):
        dist_x = sun_x - planet.get_x_pos()
        dist_y = sun_y - planet.get_y_pos()
        return math.sqrt(dist_x ** 2 + dist_y ** 2)

    def get_x_pos(self) -> float:
        return self.position_x

    def get_y_pos(self) -> float:
        return self.position_y

    def get_x_vel(self) -> float:
        return self.velocity_x

    def get_y_vel(self) -> float:
        return self.velocity_y

    def set_x_vel(self, new_x_vel:float):
        self.velocity_x = new_x_vel

    def set_y_vel(self, new_y_vel:float):
        self.velocity_y = new_y_vel

    def move_to(self, new_x:float, new_y:float):
        self.position_x = new_x
        self.position_y = new_y
        self.t.goto(new_x, new_y)

    def __str__(self):
        return (f"Planet("
                f"name: {self.name}, mass: {self.mass}, distance: {self.distance},"
                f"position: {self.position_x},{self.position_y}, "
                f"velocity: {self.velocity_x},{self.velocity_y})")