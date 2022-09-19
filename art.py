from email import message
from turtle import color
from PIL import Image, ImageFont, ImageDraw
import os
import random
import colorsys
from noise import pnoise2


class Artwork:

    def __init__(self,
                 size=(500, 500),
                 grain_level=0.2,
                 noise_level=2.5,
                 noise_shift=2.0,
                 debug=False):
        # color = self.create_random_color()
        self.size = size
        self.img = Image.new("RGBA", size=self.size)
        self.pallate = (self.create_random_color(), self.create_random_color(),
                        self.create_random_color(), self.create_random_color())
        self.grain_level = grain_level
        self.noise_base = random.randint(0, 999)
        self.noise_shift = noise_shift
        self.noise_level = noise_level
        self.debug = debug
        self.generate()
        if self.add_debug:
            self.add_debug()

    def get_random_point(self):
        points = []
        for x in range(self.img.width):
            for y in range(self.img.height):
                points.append((x, y))
        random.shuffle(points)
        return points

    def generate(self):
        for (x, y) in self.get_random_point():
            color = self.get_color_at_point(x, y)
            self.img.putpixel((x, y), color)

    def make_grain(self):
        if self.grain_level > 0:
            return random.uniform(-1 * self.grain_level, self.grain_level)
        else:
            return 0

    def make_noise(self, px, py):
        return self.noise_level * pnoise2(
            px * self.noise_shift, py * self.noise_shift, base=self.noise_base)

    def get_color_at_point(self, x, y):
        (tl, tr, bl, br) = self.pallate

        px = x / self.img.width
        py = y / self.img.height

        #Grain
        grain_x = self.make_grain()
        grain_y = self.make_grain()

        #Noise
        noise_x = self.make_noise(px, py)
        noise_y = self.make_noise(px, py)

        grad1 = self.mix(tl, tr, px + grain_x + noise_x)
        grad2 = self.mix(bl, br, px + grain_x + noise_x)

        grad = self.mix(grad1, grad2, py + grain_y + noise_y)

        return grad

    def mix(self, color1, color2, mixer):
        (r1, g1, b1, a1) = color1
        (r2, g2, b2, a2) = color2

        mixer = max(0, min(mixer, 1))

        return (self.mix_channel(r1, r2,
                                 mixer), self.mix_channel(g1, g2, mixer),
                self.mix_channel(b1, b2,
                                 mixer), self.mix_channel(a1, a2, mixer))

    def save_to_file(self, filepath):
        self.img.save(filepath)

    def mix_channel(self, c1, c2, mixer):
        return int(c1 + (c2 - c1) * mixer)

    def create_random_color(self):
        h = random.uniform(0, 1)
        s = random.uniform(0.5, 1)
        v = random.uniform(0.9, 1)

        #convert hsv color to rgb
        (r, g, b) = colorsys.hsv_to_rgb(h, v, v)

        r = int(r * 255)
        g = int(g * 255)
        b = int(b * 255)

        return (r, g, b, 255)

    def add_debug(self):
        messages = [
            f"Generated Art: By Danny", f"Twitter:       @daniethedev",
            f"Grain Level:  {self.grain_level}",
            f"Noise Level:  {self.noise_level}",
            f"Noise Shift:  {self.noise_shift}"
        ]
        #Load Fonts
        fnt = ImageFont.truetype('ibm-plex-mono.ttf', 6)

        drawer = ImageDraw.Draw(self.img)
        drawer.multiline_text((20, 20),
                              '\n'.join(messages),
                              font=fnt,
                              fill=(0, 0, 0, 255))


#Run Code if only pressed in the file!
if __name__ == "__main__":
    print("Generating Artwork from Art.py")
    os.makedirs('exports', exist_ok=True)
    for i in range(10):
        filepath = os.path.join("exports", f'art-{i + 1}.png')
        art = Artwork((500, 500), grain_level=0.4, debug=True)
        art.save_to_file(filepath)