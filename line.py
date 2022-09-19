from tkinter import Image
from art import Artwork
from PIL import ImageDraw
import os
import random
import math


class LineArtwork(Artwork):

    def generate(self):
        drawer = ImageDraw.Draw(self.img)
        for (x, y) in self.get_random_point():
            color = self.get_color_at_point(x, y)

            length = random.randint(2, 10)
            angle = random.uniform(0, 3.141)

            sx = length * math.sin(angle)
            sy = length * math.cos(angle)

            drawer.line([
                (x - sx, y - sy),
                (x + sx, y + sy),
            ], fill=color)
            self.img.putpixel((x, y), color)


#Run Code if only pressed in the file!
if __name__ == "__main__":
    print("Generating Artwork from Line.py")
    os.makedirs('exports', exist_ok=True)
    for i in range(10):
        filepath = os.path.join("exports", f'line-{i + 1}.png')
        art = LineArtwork((500, 500), grain_level=0.3)
        art.save_to_file(filepath)