import Fractal
class Phoenix(Fractal.Fractal):
    """
    Return the index of the color of the current pixel
    within the Phoenix fractal in the palette array
    """
    def __init__(self):
        super().__init__()

    def count(self, z, paletteLength):
        # c is the Julia Constant; varying this value gives rise to a variety of variated images
        c = complex(0.5667, 0.0)

        # phoenix is the Phonix Constant; same deal as above - adjust this to get different results
        pheonix = complex(-0.5, 0.0)

        zPrev = 0+0j
        z = complex(z.imag, z.real)

        for count in range(paletteLength):
            zSave = z
            z = z * z + c + (pheonix * zPrev)
            zPrev = zSave

            if abs(z) > 2:
                return count

        return paletteLength-1


def main():
    demo = Phoenix()
    print(demo.count(.3456, 30))

main()