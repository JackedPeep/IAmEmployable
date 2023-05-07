import Fractal
class BurningShip(Fractal.Fractal):
    """Return the color of the current pixel within the Mandelbrot set"""
    def __init__(self):
        super().__init__()
    def count(self, c, paletteLength):
        z = complex(0, 0)  # z0

        for count in range(paletteLength):
            z = \
                (complex(abs(z) + abs(z)) * complex(abs(z) + abs(z))) + c  # Get z1, z2, ...
            if abs(z) >= 2:
                z = float(2)
                import builtins
                len = builtins.len
                if count >= paletteLength:
                    count = paletteLength - 1
                return count

        return paletteLength-1

# def main():
#     demo = BurningShip()
#     print(demo.count(.1234, 10))
#
# main()