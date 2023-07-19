import cv2, os, pathlib, pytesseract
from PIL import Image

class OCR:
    '''
    from: https://builtin.com/data-science/python-ocr
    video: https://youtu.be/9nUNPrvCFAE
    '''

    _dir = f"{pathlib.Path.home()}/Downloads"


    def __init__(self, filename="original", ext=".png"):
        self.file = f"{OCR._dir}/{filename}{ext}"
        self.tmp_file = f"{OCR._dir}/tmp{ext}"
        self.memory = cv2.imread(self.file)
        self.password = ''
        self.actual = "c9c4b4a"

    def __str__(self):
        return self.get_pass()

    def __clean(self):
        old = [self.tmp_file]
        [os.remove(path) for path in old]

    def _initial(self):
        '''Resets everything same as a clean instance!'''
        self.memory = cv2.imread(self.file)

    def to_np(self):
        self.save()
        self.memory = cv2.imread(self.tmp_file)
        self.__clean()

    def to_pil(self):
        self.save()
        self.memory = Image.open(self.tmp_file)
        self.__clean()


    def save(self):
        if str(type(self.memory)) == "<class 'numpy.ndarray'>":
            cv2.imwrite(self.tmp_file, self.memory)

        elif str(type(self.memory)) == "<class 'PIL.Image.Image'>":
            self.memory.save(self.tmp_file, quality=95)


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

    def tesseract(self):
        self.password = pytesseract.image_to_string(self.memory)

    def get_pass(self, strip=True):
        self._initial()
        self.process()
        self.tesseract()
        if strip:
            return self.password.strip()
        else:
            return self.password

    def test_(self):
        if self.actual == self.get_pass():
            print(f"It's a Match! pw = {self.password}")

