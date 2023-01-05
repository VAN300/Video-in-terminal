# encoding: utf-8

from os import get_terminal_size

from cv2 import resize
from cv2 import INTER_AREA


class ASCIIImage(object):

    def __init__(self, gimage):
        self.max_width,\
        self.max_height = get_terminal_size()
        
        self._image = resize(
                gimage,
                (self.max_width, self.max_height),
                interpolation=INTER_AREA
        )


