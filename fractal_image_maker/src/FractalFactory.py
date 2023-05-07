from Fractal import Fractal
from Phoenix import Phoenix
from Euphemia import Euphemia
from Mandelbrot import Mandelbrot
from Julia import Julia
from BurningShip import BurningShip
def fractalFactory(fractalInfo):
    '''
    takes dictionary from user OR default dictionary and checks the type of fractal
    count method using the 'type' key pair to identify which count method to use.
    '''
    type = fractalInfo["type"]

    if type == "phoenix":
        phoenix = Phoenix()
        return phoenix
    elif type == "mandelbrot":
        mandelbrot = Mandelbrot()
        return mandelbrot
    elif type == "euphemia":
        euphemia = Euphemia()
        return euphemia
    elif type == "julia":
        julia = Julia()
        return julia
    elif type == "burningship":
        burningShip = BurningShip()
        return burningShip
    else:
        print("Error: Not a valid fractal type")