# Fractal Visualizer User Manual

**Purpose:**

This program produces a chosen image to your screen using your choice of palette **AND** saves a .png file of it to the directory the program is in.
There are prerequisites to run this program.

**Prerequisites:**

- Have python version 3 installed.
- Have linux based shell.bash command line.

**Tutorial:**

1) Go to your bash command line.
2) Change your directory tail to `... cs1440-assn5/src`
3) Run ```bash python3 main.py phoenix Swaddle```

**Output if valid argument is given:**

```bash
USERNAME@COMPUTER:~/python_projects/CS_1440_KBC_2022/cs1440-assn5$ python3 src/main.py spiral1
Rendering spiral1 fractal
[100% =================================]
Done in 95.749 seconds!
Wrote picture spiral1.png
Close the image window to exit the program
```
**Fractal image:**

![pheonix.png](pheonix.png) This should have your choice of palette.

**Output if invalid argument is given for fractal:**

```bash
USERNAME@COMPUTER:~/python_projects/CS_1440_KBC_2022/cs1440-assn5$ python3 src/main.py NOT_ON_LIST
ERROR: NOT_ON_LIST is not a valid fractal
Please choose one of the following:
        phoenix
        peacock
        monkey-knife-fight
        shrimp-cocktail
        elephants
        leaf
        mandelbrot
        mandelbrot-zoomed
        seahorse
        spiral0
        spiral1
        starfish
       
```

**Output if invalid argument is given for palette:**
```bash
USERNAME@COMPUTER:~/python_projects/CS_1440_KBC_2022/cs1440-assn5$ python3 src/main.py NOT_ON_LIST
ERROR: NOT_A_PALETTE is not a valid palette
Please choose one of the following:
        SpitUp
        Swaddle
       
```

**Example:**

```bash

USERNAME@COMPUTER:~/python_projects/CS_1440_KBC_2022/cs1440-assn5$ python3 main.py IMAGE_REQUEST 

```
IMAGE_REQUEST: is a placeholder for your choice of image.

List of choices:
- mandelbrot
- mandelbrot-zoomed
- spiral0
- spiral1
- seahorse
- elephants
- leaf
- starfish
- phoenix
- peacock
- monkey-knife-fight
- shrimp-cocktail