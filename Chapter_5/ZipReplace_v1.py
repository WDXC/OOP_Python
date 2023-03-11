import sys
import os
import shutil
import zipfile
from pathlib import Path

class ZipReplace:
    def __int__(self, filename, search_string,
                replace_string):
        self.filename = filename
        self.search_string = search_string
        self.replace_string = replace_string
        self.tmp_directory = Path("unzipped-{}".format(filename))

    def zip_find_replace(self):
        self.unzip_files()
        self.find_replace()
        self.zip_files()

    def unzip_files(self):
        os.mkdir(self.tmp_directory)
        with zipfile.ZipFile(self.filename) as zip:
            zip.extractall(str(self.tmp_directory))

    def find_replace(self):
        for filename in self.tmp_directory.iterdir():
            with filename.open() as file:
                contents = file.read()
            contents = contents.replace(
                self.search_string, self.replace_string)
            with filename.open("w") as file:
                file.write(contents)

    def zip_files(self):
        with zipfile.ZipFile(self.filename, 'w') as file:
            for filename in self.tmp_directory.iterdir():
                file.write(str(filename), filename.name)
        shutil.rmtree(str(self.tmp_directory))

if __name__ == "__main__":
    ZipReplace(*sys.argv[1:4]).zip_find_replace()