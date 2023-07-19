from PIL import Image
from .paths import *

def enlarge(path=new):
    '''
    from https://cloudinary.com/guides/bulk-image-resize/python-image-resize-with-pillow-and-opencv
    '''
    multiple = 3    # works: 3
    image = Image.open(path)
    width, height = image.size
    new_image = image.resize((width * multiple, height * multiple))
    new_image.save(large)
