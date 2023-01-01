# encoding: utf-8

import cv2
from PIL import Image
from .image_showing import ASCIIImage


def collect_video(path: str):
    video_cap = cv2.VideoCapture(path)

    processing, image = video_cap.read()
    try:
        while processing:
            processing, image = video_cap.read()
            array = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            render_video(array)
    finally:
        exit()


def render_video(array):
    image = ASCIIImage(Image.fromarray(array))
    image.prepare()
    image.render_image()
