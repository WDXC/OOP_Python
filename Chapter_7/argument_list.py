"""
def get_pages(*links):
    for link in links:
        print(link)

get_pages()
get_pages('https://www.baidu.com')
get_pages('https://www.baidu.com','https://google.com')
"""

class Options:
    default_options = {
        'port': 21,
        'host': 'localhost',
        'username': None,
        'password': None,
        'debug': False,
    }

    def __init__(self, **kwargs):
        self.options = dict(Options.default_options)
        self.options.update(kwargs)

    def __getitem__(self, key):
        return self.options[key]

options = Options(username='dusty', password='drowssap',
                  debug=True)
print(options['debug'])

print(options['port'])

print(options['username'])