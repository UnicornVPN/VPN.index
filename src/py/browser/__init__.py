import subprocess


class Browser:
    @staticmethod
    def __open(browser, url):
        subprocess.run([browser, url])

    @staticmethod
    def chrome(url):
        Browser.__open("google-chrome", url)

    @staticmethod
    def chromium(url):
        Browser.__open("chromium-browser", url)

    @staticmethod
    def firefox(url):
        Browser.__open("firefox", url)

    @staticmethod
    def default(url):
        Browser.__open("xdg-open", url)

    @classmethod
    def open(cls, urls, browser=default):
        for url in urls:
            browser(url)


if __name__ == '__main__':
    # test
    link = "https://youtu.be/TbvWnJh9e-g?t=900"
    Browser.chrome(link)
