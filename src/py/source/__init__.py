from .list.top import index


class Source():
    top = index

    def __init__(self, debug=False):
        self.debug = debug
        self.index = set()
        self.top = set()

        self.__append()

    def __repr__(self):
        for i in Source.top:
            print(f"{i!r}")

    def __append(self):
        for i in Source.top:
            self.top.add(i)
            if self.debug:
                print(type(i))

        if self.debug:
            print(type(Source.top))
            print(type(Source.top[0]))

    def __str__(self):
        return str(self.top)

    def get(self, which_set="default"):
        '''Get a set of vpn sources! by default returns all index'''
        match which_set:
            case "index":
                get_set = self.index
            case "top":
                get_set = self.top
            case _:
                get_set = self.index

        set_pgs = set()
        for p in get_set:
            set_pgs.add(p[0])
        return set_pgs


def _test():
    from browser.Page import Page
    from source import Source
    # Test
    src = Source(debug=False)
    print(src)
    print(src.get("top"))
    pg1 = Page()
    pg1.url = src.get("top").pop()
    pg1.open()


if __name__ == '__main__':
    _test()
