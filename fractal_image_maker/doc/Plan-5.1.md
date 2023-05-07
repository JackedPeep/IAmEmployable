 # Software Development Plan

## Phase 0: Requirements Specification *(10%)*

I must create an *abstract class* called `Fractal`. 
From `Fractal` I will then derive three concrete classes 
`Phoenix`,`Mandelbrot`, & `JackedPeep`.


My fractals will have no relation to `Palettes` or `Colors`,
only to the mathematical formula I give it. `FractalFactory`
will be the driver for the program. This doesn't need to be a class.
`FractalFactory`, if not given an object to fractalize, will return a default fractal.

I will create a `FractalParser` that converts command line arguments into runnable string.
The user will also be able to declare a palette on the command line, and the `PaletteFactory` 
will be in charge of executing the proper palette.

I will then create an `ImagePainter` class. This class will be responsible for putting everything together.

Finally I will document the users manual and write 8 **non-trivial** code tests that pass.

The problem this program aims to solve is to better implement a fractal image painter for the masses.
It will give them more freedom to work with the palettes they want and they will **NO LONGER** wait
for generations as the program stands idly by and drains the RAM from their CPUs... **NO LONGER!**

Some problems that might be faced are incorrect inputs from users, calling the correct fractal, and correct communication in the painter.
## Phase 1: System Analysis *(10%)*

User *input* --> `FractalParser` --> stringPalette & stringFractal *output*

**Formula:** `sys.args`, `range()`

stringPalette *input* --> `PaletteFactory` --> palette *output*

**Formula:** `dict`, `keys`

stringFractal *input* --> `FractalFactory` --> fractal *output*

**Formula:** `dict`, `keys`

palette & fractal *input* --> `ImagePainter` --> GUI Image *output*

**Formula:** `.count()`, `Fractal`, `Palette`


## Phase 2: Design *(30%)*

**Deliver:**

*   Function signatures that include:
    *   Descriptive names.
    *   Parameter lists.
    *   Documentation strings that explain the purpose, inputs and outputs.
*   Pseudocode that captures how each function works.
    *   Pseudocode != source code.  Do not paste your finished source code into this part of the plan.
    *   Explain what happens in the face of good and bad input.
    *   Write a few specific examples that occurred to you.
*   Example:
    ```python
    def main():
        if sys.argv[1] is valid
            if sys.argv[2] is valid
                
                read file.frac into dictionary # FractalParser
                
                call ImagePainter()
    def FractalParser()
        open file.frac
        FractalDictionary += line in dictionary
        closefile.frac
    
    class Fractal():  #Parent class
        def count(ComplexNum):
            count = 0
            if absolute value of complex number > 2:
             number iteration count++
    class Phoenix():  #Child class
        self.ComplexNum = ###    
    class Malbrot():  #Child class
        self.ComplexNum = ### 
    class Euphemia():  #Child class
        self.ComplexNum = ### 
    def FractalFactory():
        if dictionary key 'type' == Phoenix:
            Phoenix.FractalMethod()
        if dictionary key 'type' == Malbrot:
            Malbrot.FractalMethod()
        if dictionary key 'type' == Euphemia:
            Euphemia.FractalMethod()
    
    class Palette(): #Parent
        def getColor(palletList):
            return color in palletList equal to the itteration from the fractal.
    class SpitUp(): #Child
        self.paletteList = {pallete}
    class Swaddle(): #Child
        self.paletteList = {pallete}
    def PaletteFactory():
        if sys.argv[2] == "SpitUp"
            Spitup.getColor():
        if sys.argv[2] == "Swaddle"
            Swaddle.getColor():
    def ImagePainter():
        uses fractalFactory and paletteFactory to gather the input to paint the fractal on the GUI.
    
    ```

## Phase 3: Implementation *(15%)*

It was alot easier to understand this assignment after the last one, but every time I looked back through the instructions there was always something else to do. I would appreciate a little more freedome with the programing especialy when the projects are this big.

## Phase 4: Testing & Debugging *(30%)*




    ```python

    def testOutputPhoenixCount(self):
        output = fractalFactory(self.dicPhoenix)
        self.assertEqual(output.count(.1234, 10), 5)
        self.assertEqual(output.count(.2345, 20), 6)
        self.assertEqual(output.count(.3456, 30), 29)

    passed

    def testOutputMandelbrotCount(self):
        output = fractalFactory(self.dicMandelbrot)
        self.assertEqual(output.count(.1234, 10), 9)
        self.assertEqual(output.count(.2345, 20), 19)
        self.assertEqual(output.count(.3456, 30), 8)

    passed

    def testOutputBurningShipCount(self):
        output = fractalFactory(self.dicBurningShip)
        self.assertEqual(output.count(.1234, 10), 5)
        self.assertEqual(output.count(.2345, 20), 3)
        self.assertEqual(output.count(.3456, 30), 2)
    
    passed

    def testOutputJuliaCount(self):
        output = fractalFactory(self.dicJulia)
        self.assertEqual(output.count(.1234, 10), 9)
        self.assertEqual(output.count(.2345, 20), 19)
        self.assertEqual(output.count(.3456, 30), 29)

    passed

    def testOutputEuphemiaCount(self):
        output = fractalFactory(self.dicEuphemia)
        self.assertEqual(output.count(.1234, 10), 5)
        self.assertEqual(output.count(.2345, 20), 5)
        self.assertEqual(output.count(.3456, 30), 8)
    
    passed

    def testOutputSwaddleGetColor(self):
        output = paletteFactory("Swaddle")
        self.assertEqual(output.getColor(1), '#D99AA5')
        self.assertEqual(output.getColor(275), "#BF0060")
        self.assertEqual(output.getColor(500), "#BF0060")

    passed

    def testOutputSpitUpGetColor(self):
        output = paletteFactory("SpitUp")
        self.assertEqual(output.getColor(1), '#E6E3B5')
        self.assertEqual(output.getColor(275), "#ffffff")
        self.assertEqual(output.getColor(500), "#fffde8")

    passed

    def testOutputFractalParser(self):
        output = fractalParser("phoenix.frac")
        self.assertEqual(output,{'type': 'phoenix', 'preal': '-0.5', 'pimag': '0.0',
                                 'creal': '0.5667', 'cimag': '0.0', 'centerx': '0',
                                 'centery': '0', 'axislength': '3.25', 'pixels': '512',
                                 'iterations': '101'})

    passed

    ```

## Phase 5: Deployment *(5%)*

**Deliver:**

*   Your repository pushed to GitLab.
*   **Verify** that your final commit was received by browsing to its project page on GitLab.
    *   Ensure the project's URL is correct.
    *   Review the project to ensure that all required files are present and in correct locations.
    *   Check that unwanted files have not been included.
    *   Make any final touches to documentation, including the Sprint Signature and this Plan.
*   **Validate** that your submission is complete and correct by cloning it to a new location on your computer and re-running it.
	*	Run your program from the command line so you can see how it will behave when your grader runs it.  **Running it in PyCharm is not good enough!**
    *   Run through your test cases to avoid nasty surprises.
    *   Check that your documentation files are all present.


## Phase 6: Maintenance


1) My palettes are sloppy.
2) I didn't understand tkinter.
3) 3 years.
4) no
5) no
6) moderatly difficult
7) unsure
8) unsure
9) unsure
