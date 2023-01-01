import io

import cv2

import image_showing

PATH = '/home/van/Видео/bad_apple.mp4'

video_cap = cv2.VideoCapture(PATH)

processing, image = video_cap.read()

while processing:
    
    processing, image = video_cap.read()
    array = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    image_showing.video(array)
    

