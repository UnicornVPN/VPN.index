import shutil
import pathlib
import requests
# https://stackoverflow.com/a/18043472

def saveTo():
    images = f"{pathlib.Path.home()}/Downloads"
    return images
def saveImg(url):
    save_as = f"{saveTo()}/img.jpg"

    response = requests.get(url, stream=True)

    with open(save_as, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response

def __OCR(img):
    return "todo"

def __getImg():
    pass
def getPassword():
    password = __OCR(__getImg())

    return password