import cv2
from PIL import Image

from ocr.tesseract import OCR


class OCRVpnBook(OCR):
    '''
    This class Works! But this "processing" stack & order is Highly tuned for the image from VPNbook. Other sites may require their own custom subclass!

    Precondition:
    - Works only if a image file is in Downloads! make this using the Vpnbook class

    for: https://www.vpnbook.com/
    '''

    def __init__(self, filename="original", ext=".png"):
        super().__init__(filename, ext)
        self.file = f"{OCRVpnBook._dir}/{filename}{ext}"
        self.tmp_file = f"{OCRVpnBook._dir}/tmp{ext}"
        self.memory = cv2.imread(self.file)
        self.password = ''
        self.actual = "c9c4b4a"

    def margin(self, top=20, right=20, bottom=20, left=20, color=(255, 255, 255)):
        '''
        Adds a margin around the image, using Pillow!
        # Python
        sch: https://www.google.com/search?q=python+add+extra+space+around+image
        from: https://note.nkmk.me/en/python-pillow-add-margin-expand-canvas

        # Gimp
        solution: Gimp https://superuser.com/questions/115018/gimp-adding-new-content-to-the-bottom-of-an-image
        '''
        # im = Image.open(self.file)
        self.to_pil()
        im = self.memory

        width, height = im.size
        new_width = width + right + left
        new_height = height + top + bottom
        result = Image.new(im.mode, (new_width, new_height), color)
        result.paste(im, (left, top))
        # Save to memory
        self.memory = result

    def greyscale(self):
        self.memory = cv2.cvtColor(self.memory, cv2.COLOR_BGR2GRAY)

    def thresholding(self):
        self.memory = cv2.threshold(self.memory, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    def remove_noise(self):
        return cv2.medianBlur(self.memory, 5)

    def enlarge(self):
        '''
        from https://cloudinary.com/guides/bulk-image-resize/python-image-resize-with-pillow-and-opencv
        '''
        self.to_pil()

        multiple = 3  # works: 3
        width, height = self.memory.size
        new_image = self.memory.resize((width * multiple, height * multiple))
        self.memory = new_image

    def process(self):
        self.margin()
        self.to_np()
        self.greyscale()
        self.thresholding()
        self.enlarge()

    def test_(self):
        '''Compares a retrieved image, with one read by hand! If it matches: then OCR is working & accurate.'''
        if self.actual == self.get_pass():
            print(f"It's a Match! pw = {self.password}")


def ocrPass():
    '''Test'''
    img = OCRVpnBook()
    return img.get_pass()


if __name__ == '__main__':
    ocrPass()
    # Or
    img = OCRVpnBook()
    print(img.test_())
