import requests
from bs4 import BeautifulSoup
from .password import getPassword

source = "https://www.vpnbook.com/freevpn"


class Vpnbook():
    def __init__(self, url=source):
        self.url = url
        self.soup = ''
        self.setSoup()
        self.open_vpn = self.getVpn("open")
        self.pptp_vpn = self.getVpn("pptp")
        self.user = self.__getUser()
        self.password = self.__getPass()

    def setSoup(self):
        response = requests.get(self.url)
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

    def __getPass(self):
        return getPassword()


if __name__ == '__main__':
    def _test():
        '''from get.vpnbook import Vpnbook'''
        v = Vpnbook()

        print(v.pptp_vpn)
        print(v.user)
        print(v.password)
