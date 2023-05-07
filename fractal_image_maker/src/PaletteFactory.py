from SpitUp import SpitUp
from Swaddle import Swaddle
def paletteFactory(palette):
    if palette == "Swaddle":
        swaddle = Swaddle()
        return swaddle
    elif palette == "SpitUp":
        spitUp = SpitUp()
        return spitUp
    else:
        swaddle = Swaddle()
        return swaddle