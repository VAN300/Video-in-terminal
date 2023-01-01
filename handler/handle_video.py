#encoding" utf-8
import sys
import time
from pprint import pprint
from PIL import Image



def handle_video(path: str):


    with Image.open(path, 'r') as image, open('/home/van/Рабочий стол/Текстовый файл.txt', 'w') as out:
        image = image.convert('L')
        width, height = image.size

        image = image.resize((int(width // 9), height // 21))
        width, _ = image.size

        pixels = list(image.getdata())
        
        for e, i in enumerate(pixels):

            if e % (width) == 0:
                sys.stdout.write('\n\t')
            
            if 0 < i < 64:
                sys.stdout.write('.')
                i
            elif 64 < i < 128:
                sys.stdout.write(';')

            elif 128 < i < 196:
                sys.stdout.write('|')

            elif 196 < i < 256:
                sys.stdout.write('#')

            else:
                sys.stdout.write(' ')
            time.sleep(0.00001)
            
        time.sleep(8)



handle_video('/home/van/Изображения/screen/Screenshot_20230101_112822.png')

