from browser import Browser
from source import Source

class Search:
    sch_pptp = {"https://www.google.com/search?q=free+pptp+vpn"}
    sch_openvpn = {"https://www.google.com/search?q=free+openvpn"}
    sch = sch_pptp.union(sch_pptp)

    @classmethod
    def open(cls):
        # Browser.open(Search.sch, Browser.chrome)
        Browser.open(Source.top(), Browser.chrome)


if __name__ == '__main__':
    link = ["https://youtu.be/TbvWnJh9e-g?t=902"]
    Browser.open(link)

    # Search.open()
