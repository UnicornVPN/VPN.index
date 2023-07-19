import shutil, pathlib
import requests
from bs4 import BeautifulSoup
from .password import getPassword, saveImg

class Vpnbook():
    source = "https://www.vpnbook.com"
    url = f"{source}/freevpn"
    def __init__(self):
        self.soup = ''
        self.setSoup()
        self.open_vpn = self.getVpn("open")
        self.pptp_vpn = self.getVpn("pptp")
        self.user = self.__getUser()
        self.password = self.__getPass()

    def setSoup(self):
        response = requests.get(Vpnbook.url)
        self.soup = BeautifulSoup(response.content, 'html.parser')

    def __getList(self, num=0):
        soup = self.soup
        ul = soup.find_all('ul', class_='disc')[num]
        li = ul.find_all('strong')
        return li

    def __getInnerText(self, index):
        return [li.text for li in self.__getList(index)]

    def getVpn(self, which="pptp"):
        vpn = []
        match which:
            case "pptp":
                vpn = self.__getInnerText(0)
            case "open":
                vpn = self.__getInnerText(1)
        return vpn[0:-1]

    def __getUser(self):
        return self.__getInnerText(0)[-1]

    def __getPasswordImg(self):
        num = 0
        ul = self.soup.find_all('ul', class_='disc')[num]
        li = ul.find_all('li')[-1]
        img = li.find('img')
        img_path = img['src'].replace(" ", "%20")
        img_url = f"{Vpnbook.source}/{img_path}"

        return img_url

    def __savePassImg(self):
        '''
        from: https://stackoverflow.com/a/18043472
        '''
        url = self.__getPasswordImg()
        save_as = f"{pathlib.Path.home()}/Downloads/password.png"

        response = requests.get(url, stream=True)
        with open(save_as, 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response

    def __getPass(self):
        self.__savePassImg()



if __name__ == '__main__':
    def _test():
        '''from get.vpnbook import Vpnbook'''
        v = Vpnbook()
        print(v.pptp_vpn)
        print(v.user)
        print(v.password)
