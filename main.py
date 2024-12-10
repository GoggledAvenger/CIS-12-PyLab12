from planet import Planet
from sun import Sun
from solar_system import SolarSystem
from simulation import Simulation


if __name__ == '__main__':
    solar_system = SolarSystem()

    the_sun = Sun("SOL", 10000000, 0.0,0.0)
    solar_system.add_sun(the_sun)

    earth = Planet("EARTH", 1, 25, 0.0, 5.0, 200.0,'green')
    solar_system.add_planet(earth)

    mars = Planet("MARS", .1, 62, 0.0, 10.0, 125.0,'red')
    solar_system.add_planet(mars)

    simulation = Simulation(solar_system, 500, 500, 2000)
    simulation.run()