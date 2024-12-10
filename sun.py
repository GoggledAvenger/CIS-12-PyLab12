import turtle

class Sun:
    """the star which Earth orbits"""

    def __init__(self,name:str,mass:float,position_x:float=0.0,position_y:float=0.0):
        self.name = name
        self.mass = mass
        self.position_x = position_x
        self.position_y = position_y
        # graphics
        self.t = turtle.Turtle()
        self.t.shape('circle')
        self.t.color('yellow')
        # position of sun
        self.t.penup()
        self.t.goto(self.position_x, self.position_y)
        self.t.pendown()

    def get_mass(self) -> float:
        return self.mass

    def get_x_pos(self) -> float:
        return self.position_x

    def get_y_pos(self) -> float:
        return self.position_y

    def __str__(self):
        return f"Sun(name = {self.name}, mass = {self.mass}, position = {self.position_x},{self.position_y})"