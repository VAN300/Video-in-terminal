# encoding: utf-8

import subprocess
from .image_showing import ASCIIImage
from strategies import Strategy

import cv2



def render_video(path: str):
    video_cap = cv2.VideoCapture(path)
    processing, image = video_cap.read()
    while processing:
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        yield gray_image
            
        processing, image = video_cap.read()



class Manager(object):

    def __init__(self) -> None:
        self.strategy: Strategy

    def setStrategy(self, strategy: Strategy) -> None:
        self.strategy = strategy

    def executeStrategy(self, path: str) -> None:
        subprocess.Popen([f"ffplay", "-nodisp", "-autoexit", path])

        for gray_image in render_video(path):
            aimage = ASCIIImage(gray_image)
            self.strategy.execute(aimage)


MANAGER = Manager()

