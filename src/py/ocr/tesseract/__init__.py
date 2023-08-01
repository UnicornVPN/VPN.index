import cv2, os, pathlib, pytesseract
from PIL import Image

class OCR:
    '''
    Super class for inheritance!
    from: https://builtin.com/data-science/python-ocr
    video: https://youtu.be/9nUNPrvCFAE
    '''

    _dir = f"{pathlib.Path.home()}/Downloads"

    def __init__(self, filename="original", ext=".png"):
        pass


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

    def tesseract(self):
        self.password = pytesseract.image_to_string(self.memory)

    def process(self):
        '''Override in subclass'''
        pass

    def get_pass(self, strip=True):
        self._initial()
        self.process()
        self.tesseract()
        if strip:
            return self.password.strip()
        else:
            return self.password
