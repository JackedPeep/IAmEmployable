import sys
import time
from tkinter import Tk, Canvas, PhotoImage, mainloop


IMAGESIZE = 512
class ImagePainter():
    def __init__(self, Fractal, Palette, fractalInfo, image):
        self.Fractal = Fractal
        self.Palette = Palette
        self.fractalInfo = fractalInfo
        self.image = image

    def paintImage(self, window, tkPhotoImage):
        """Paint a Fractal image into the TKinter PhotoImage canvas.
        This code creates an image which is 512x512 pixels in size."""

        #fractal = fractals[imagename]

        # Figure out how the boundaries of the PhotoImage relate to coordinates on
        # the imaginary plane.
        minx = (float(self.fractalInfo['centerx']) - float((self.fractalInfo['axislength'])) / 2.0)
        maxx = (float(self.fractalInfo['centerx']) + float((self.fractalInfo['axislength'])) / 2.0)
        miny = (float(self.fractalInfo['centery']) - float((self.fractalInfo['axislength'])) / 2.0)
        maxy = (float(self.fractalInfo['centery']) + float((self.fractalInfo['axislength'])) / 2.0)

        # Display the image on the screen
        canvas = Canvas(window, width=IMAGESIZE, height=IMAGESIZE, bg='#000000')
        canvas.pack()
        canvas.create_image((IMAGESIZE/2, IMAGESIZE/2), image=tkPhotoImage, state="normal")

        # At this scale, how much length and height on the imaginary plane does one
        # pixel take?
        pixelsize = abs(maxx - minx) / IMAGESIZE

        for row in range(IMAGESIZE, 0, -1):
            cc = []
            for col in range(IMAGESIZE):
                x = minx + col * pixelsize
                y = miny + row * pixelsize
                color = self.Palette.getColor(self.Fractal.count(complex(x, y), int(self.fractalInfo["iterations"])))
                cc.append(color)
            tkPhotoImage.put('{' + ' '.join(cc) + '}', to=(0, IMAGESIZE-row))
            window.update()  # display a row of pixels
            print(self.pixelsWrittenSoFar(row), end='\r', file=sys.stderr)  # the '\r' returns the cursor to the leftmost column

    def pixelsWrittenSoFar(self, rows):
        portion = (IMAGESIZE - rows) / IMAGESIZE
        status_percent = '{:>4.0%}'.format(portion)
        status_bar_width = 34
        status_bar = '=' * int(status_bar_width * portion)
        status_bar = '{:<33}'.format(status_bar)
        return ''.join(list(['[', status_percent, ' ', status_bar, ']']))

    def printSave(self):
        # Set up the GUI so that we can paint the fractal image on the screen
        print("Rendering {} fractal".format(self.image), file=sys.stderr)
        before = time.time()
        window = Tk()
        img = PhotoImage(width=IMAGESIZE, height=IMAGESIZE)
        self.paintImage(window, img)

        # Save the image as a PNG
        after = time.time()
        print(f"\nDone in {after - before:.3f} seconds!", file=sys.stderr)
        img.write(f"{self.image}.png")
        print(f"Wrote picture {self.image}.png", file=sys.stderr)

        # Call tkinter.mainloop so the GUI remains open
        print("Close the image window to exit the program", file=sys.stderr)
        mainloop()
