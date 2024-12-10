from solar_system import SolarSystem
import turtle

class Simulation:
    """digital orrery"""

    def __init__(self,solar_system:SolarSystem,width:int,height:int,num_periods:int):
        self.solar_system = solar_system
        self.width = width
        self.height = height
        self.num_periods = num_periods
        # graphics
        self.t = turtle.Turtle()
        self.t.hideturtle()
        self.space = turtle.Screen()
        self.space.setup(self.width,self.height)
        self.t.clear()

    def run(self):
        self.solar_system.show_planets()
        for _ in range(self.num_periods):
            self.solar_system.move_planets()
            self.solar_system.show_planets()
        self.space.exitonclick()