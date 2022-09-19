from tkinter import Image
from art import Artwork
from PIL import ImageDraw
import os
import random


class BlockArtwork(Artwork):

    def generate(self):
        drawer = ImageDraw.Draw(self.img)
        for (x, y) in self.get_random_point():
            color = self.get_color_at_point(x, y)

            height = random.randint(2, 10)
            width = random.randint(2, 10)

            drawer.rectangle([
                (x - width, y - height),
                (x + width, y + height),
            ],
                             fill=color)
            self.img.putpixel((x, y), color)


#Run Code if only pressed in the file!
if __name__ == "__main__":
    print("Generating Artwork from Block.py")
    os.makedirs('exports', exist_ok=True)
    for i in range(10):
        filepath = os.path.join("exports", f'block-{i + 1}.png')
        art = BlockArtwork((500, 500), grain_level=0.3)
        art.save_to_file(filepath)