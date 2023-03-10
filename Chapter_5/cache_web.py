from urllib.request import urlopen
class WebPage:
    def __init__(self, url):
        self.url = url
        self._content = None

    @property
    def content(self):
        if not self._content:
            print("Retrieving New Page...")
            self._content = urlopen(self.url).read()
        return self._content


import time
webpage = WebPage("http://baidu.com")
now = time.time()
contenet1 = webpage.content

print(time.time() - now)

now = time.time()
contenet2 = webpage.content
print(time.time() - now)


print(contenet2 == contenet1)
