#encoding" utf-8
import os
import sys
from PIL import Image

SYMS = ' \'.,:^";*!²¤/r(?+¿cLª7t1fJCÝy¢zF3±$S2kñ5AZXG$À0Ãm&Q8%RÔßÊNBåMÆØ@'
SCAL_W, SCAL_H =(6, 11)


class ASCII_Image:

    def __init__(self, file, out=sys.stdout):
        self.image = file
        self.out = out
        self.pixels: list = []
        
        self.width: int = file.size[0] // SCAL_W
        self.height: int = file.size[1] // SCAL_H
        

    def prepare(self):
        self.image = self.image.convert('L')

        self.image = self.image.resize((self.width, self.height))

        self.pixels = list(self.image.getdata())

    def render_image(self):
        os.system('clear')

        for e, i in enumerate(self.pixels):
            self.render_pixel(e, i)

    
    def render_pixel(self, e: int, i: int):
        if e % self.width == 0:
            self.out.write('\n')

        light = SYMS[i // 4]
        self.out.write(light)


image = ASCII_Image(Image.open('/home/van/Изображения/bad_apple.png', 'r'))
image.prepare()
image.render_image()
