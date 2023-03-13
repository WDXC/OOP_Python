"""
with open('filename') as file:
    for line in file:
        print(line, end='')
"""

class StringJoiner(list):
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.result = "".join(self)