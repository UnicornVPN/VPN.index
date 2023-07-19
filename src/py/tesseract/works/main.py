import cv2
import pytesseract
from .paths import *
from .larger import *
from .margin import add_margin
import os

'''
from: https://builtin.com/data-science/python-ocr
video: https://youtu.be/9nUNPrvCFAE
'''

def clean():
    old = [large, margin, new]
    [os.remove(path) for path in old]

def tesseract(image):
    text = pytesseract.image_to_string(image)
    return text

def get_greyscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def remove_noise(image):
    return cv2.medianBlur(image,5)

def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

def _write(image):
    cv2.imwrite(new, image)

def _process():
    add_margin()
    img = cv2.imread(margin)
    img = get_greyscale(img)
    img = thresholding(img)
    _write(img)
    enlarge(new)

def readText():
    _process()
    img = cv2.imread(large)
    clean()
    return tesseract(img).strip()


def _test():
    out = readText()
    real = "c9c4b4a"
    if out == real:
        print(f"It's a Match! pw = {out}")

if __name__ == '__main__':
    _test()
    clean()