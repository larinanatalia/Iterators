import json
from pprint import pprint
from urllib.parse import quote
import hashlib

with open ("C:/Users/79035/Desktop/py-33/ad_py/Iterators. Generators. Yield/countries.json", encoding="utf-8") as f:
    json_file = json.load(f)

class Country_info:
    def __init__(self,file):
        self.file = file
        self.index = 0

    def __iter__(self):
        return self


    def __next__(self):
        new_list = self.file[self.index]
        if self.index <= len(self.file):
            item = new_list['name']['common']
            self.index += 1
            item = item.replace(' ','_')
            wiki = "http://en.wikipedia.org/wiki/{0}".format(quote(item))
            item = f"{item} - {wiki}"
            if self.index == len(self.file):
                raise StopIteration
        return item
#
def hash5(path):
    with open(path, encoding="utf-8") as f:
        json_file = json.load(f)
    for each_country in json_file:
        each_country = hashlib.md5()
        yield each_country.hexdigest()



if __name__ == '__main__':
    for wiki_link in Country_info(json_file):
        print(wiki_link)
    for item in hash5("C:/Users/79035/Desktop/py-33/ad_py/Iterators. Generators. Yield/countries.json"):
        print(item)



