'''
# Gimp
sch: https://www.google.com/search?q=gimp+add+extra+space+to+image
Solution: Gimp https://superuser.com/questions/115018/gimp-adding-new-content-to-the-bottom-of-an-image

# Python
sch: https://www.google.com/search?q=python+add+extra+space+around+image
Solution: https://note.nkmk.me/en/python-pillow-add-margin-expand-canvas
'''

from PIL import Image
from .paths import *

def __add_margin(pil_img, top=20, right=20, bottom=20, left=20, color=(255, 255, 255)):
    '''
    from: https://note.nkmk.me/en/python-pillow-add-margin-expand-canvas/
    '''
    width, height = pil_img.size
    new_width = width + right + left
    new_height = height + top + bottom
    result = Image.new(pil_img.mode, (new_width, new_height), color)
    result.paste(pil_img, (left, top))
    return result


def add_margin():
    im = Image.open(original)
    im_new = __add_margin(im)
    im_new.save(margin, quality=95)