from tkinter import Image
from art import Artwork
from PIL import ImageDraw
import os
import random


class CircleArtwork(Artwork):

    def generate(self):
        drawer = ImageDraw.Draw(self.img)
        for (x, y) in self.get_random_point():
            color = self.get_color_at_point(x, y)

            radius = random.randint(9, 20)

            drawer.ellipse([
                (x - radius, y - radius),
                (x + radius, y + radius),
            ],
                           fill=color)
            self.img.putpixel((x, y), color)


#Run Code if only pressed in the file!
if __name__ == "__main__":
    print("Generating Artwork from Circle.py")
    os.makedirs('exports', exist_ok=True)
    for i in range(10):
        filepath = os.path.join("exports", f'circle-{i + 1}.png')
        art = CircleArtwork((500, 500), grain_level=0.4, debug=True)
        art.save_to_file(filepath)