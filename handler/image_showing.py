# encoding: utf-8

import os
import sys
import time

OUT = sys.stdout
SYMS = ' \'.,:^";*!²¤/r(?+¿cLª7t1fJCÝy¢zF3±$S2kñ5AZXG$À0Ãm&Q8%RÔßÊNBåMÆØ@'
SCAL_W, SCAL_H = (6, 9)
SPEED = 0.023


class ASCIIImage:

    def __init__(self, file, out=OUT):
        self.image = file
        self.out = out
        self.pixels: list = []

        self.width: int = self.image.size[0] // SCAL_W
        self.height: int = self.image.size[1] // SCAL_H

    def prepare(self):
        self.image = self.image.convert('L')
        self.image = self.image.resize((self.width, self.height))

        self.pixels = list(self.image.getdata())

    def render_image(self):
        time.sleep(SPEED)
        os.system('clear')

        for e, i in enumerate(self.pixels):
            self.render_pixel(e, i)

    def render_pixel(self, e: int, i: int):
        if e % self.width == 0:
            self.out.write('\n\t\t\t\t\t\t')

        light = SYMS[i // 4]
        self.out.write(light)