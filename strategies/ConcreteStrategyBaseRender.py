from .Strategy import Strategy
import os


class ConcreteStrategyBaseRender(Strategy):

    def __init__(self):
        self.rate = 256 // len(self.SYMS)

    def execute(self, aimage):
        str_image = ''
        for i in aimage._image:
            for j in i:
                str_image += self.SYMS[j // self.rate]
            else:
                str_image += '\n'
        else:
            os.system('clear')
            self.out.write(str_image)
