from Fractal import Fractal
class Euphemia(Fractal):
    """
    Return the index of the color of the current pixel
    within the Phoenix fractal in the palette array
    """
    def __init__(self):
        super().__init__()
    def count(self,z ,paletteLength):
        # c is the Julia Constant; varying this value gives rise to a variety of variated images
        c = complex(0.5667, 0.0)

        # effy is the Euphemia Constant; same deal as above - adjust this to get different results
        effy = complex(-2.1459, 6.02E-25)

        zPrev = 0+0j


        for count in range(paletteLength):
            zSave = z
            z = (z - z * abs(complex(z, z))/effy) + c + (effy * z * zPrev)
            zPrev = zSave

            if abs(z) > 2:
                return count

        return paletteLength-1

def main():
    demo = Euphemia()
    print(demo.count(.345, 30))

main()