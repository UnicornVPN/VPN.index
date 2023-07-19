import requests
from bs4 import BeautifulSoup
from .password import getPassword

source = "https://www.vpnbook.com/freevpn"

class Vpnbook():
    def __init__(self, url=source):
        self.url = url
        self.soup = self.getSoup()

    def getSoup(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')
        self.soup = soup
        return soup



def __getList(num=0):
    soup = __getSoup(source)
    ul = soup.find_all('ul', class_='disc')[num]
    li = ul.find_all('strong')
    return li

def __getInnerText(index):
    return [li.text for li in __getList(index)]

def getVpn(which="pptp"):
    vpn = []
    match which:
        case "pptp":
            vpn = __getInnerText(0)
        case "open":
            vpn = __getInnerText(1)
    return vpn[0:-1]

def getPptpvpn():
    return getVpn("pptp")

def getOpenvpn():
    return getVpn("open")

def getUser():
    return __getInnerText(0)[-1]

def getPass():
    return getPassword()

if __name__ == '__main__':
    print(getVpn("open"))
    print(getVpn("pptp"))
    print(getUser())