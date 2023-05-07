import unittest

from FractalFactory import fractalFactory
from PaletteFactory import paletteFactory
from FractalParser import fractalParser

class TestUtilities(unittest.TestCase):

    dicPhoenix = {'type':'phoenix'}
    dicMandelbrot = {'type':'mandelbrot'}
    dicBurningShip = {'type':'burningship'}
    dicJulia = {'type':'julia'}
    dicEuphemia = {'type':'euphemia'}





    def testOutputPhoenixCount(self):
        output = fractalFactory(self.dicPhoenix)
        self.assertEqual(output.count(.1234, 10), 5)
        self.assertEqual(output.count(.2345, 20), 6)
        self.assertEqual(output.count(.3456, 30), 29)

    def testOutputMandelbrotCount(self):
        output = fractalFactory(self.dicMandelbrot)
        self.assertEqual(output.count(.1234, 10), 9)
        self.assertEqual(output.count(.2345, 20), 19)
        self.assertEqual(output.count(.3456, 30), 8)

    def testOutputBurningShipCount(self):
        output = fractalFactory(self.dicBurningShip)
        self.assertEqual(output.count(.1234, 10), 5)
        self.assertEqual(output.count(.2345, 20), 3)
        self.assertEqual(output.count(.3456, 30), 2)

    def testOutputJuliaCount(self):
        output = fractalFactory(self.dicJulia)
        self.assertEqual(output.count(.1234, 10), 9)
        self.assertEqual(output.count(.2345, 20), 19)
        self.assertEqual(output.count(.3456, 30), 29)

    def testOutputEuphemiaCount(self):
        output = fractalFactory(self.dicEuphemia)
        self.assertEqual(output.count(.1234, 10), 5)
        self.assertEqual(output.count(.2345, 20), 5)
        self.assertEqual(output.count(.3456, 30), 8)

    def testOutputSwaddleGetColor(self):
        output = paletteFactory("Swaddle")
        self.assertEqual(output.getColor(1), '#D99AA5')
        self.assertEqual(output.getColor(275), "#BF0060")
        self.assertEqual(output.getColor(500), "#BF0060")

    def testOutputSpitUpGetColor(self):
        output = paletteFactory("SpitUp")
        self.assertEqual(output.getColor(1), '#E6E3B5')
        self.assertEqual(output.getColor(275), "#ffffff")
        self.assertEqual(output.getColor(500), "#fffde8")

    def testOutputFractalParser(self):
        output = fractalParser("phoenix.frac")
        self.assertEqual(output,{'type': 'phoenix', 'preal': '-0.5', 'pimag': '0.0',
                                 'creal': '0.5667', 'cimag': '0.0', 'centerx': '0',
                                 'centery': '0', 'axislength': '3.25', 'pixels': '512',
                                 'iterations': '101'})