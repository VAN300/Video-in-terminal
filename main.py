#!/usr/bin/env python
# encoding: utf-8

from handler import MANAGER

# to use: CStrategy1, CStrategy2, ...
from strategies import *


def main():
    path: str = '/home/van/Видео/RickRoll.mp4'

    strategy = CStrategy1()
    MANAGER.setStrategy(strategy)
    MANAGER.executeStrategy(path)


if __name__ == '__main__':
    main()
