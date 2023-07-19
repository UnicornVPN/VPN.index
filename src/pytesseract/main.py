import cv2
import pytesseract
from works.paths import *
from works.larger import *

def tesseract(image):
    '''
    from: https://builtin.com/data-science/python-ocr
    '''
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
    img = cv2.imread(extended)
    img = get_greyscale(img)
    img = thresholding(img)
    _write(img)
    enlarge(new)

def _final(img=large):
    img = remove_noise(img)

def readText():
    _process()
    img = cv2.imread(large)
    return tesseract(img).strip()


if __name__ == '__main__':
    out = readText()
    real = "c9c4b4a"
    if out == real:
        print(f"It's a Match! pw = {out}")
