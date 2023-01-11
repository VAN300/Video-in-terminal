from .Strategy import Strategy
import os


class ConcreteStrategyTest(Strategy):

    def __init__(self):
        self.SYMS= self.SYMS.replace(' ', ' ')
        self.rate = 256 // len(self.SYMS)
        self.out = open('out.txt', 'w')

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

