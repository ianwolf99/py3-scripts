import mechanize
from bs4 import BeautifulSoup as bsoup
import sys

def filtersoup(html):
    data = [ ]
    page = bsoup(html)
    for link in page.FindAll('a'):
        data.append('href')
    for link in page.FindAll('form'):
        data.append('action')
    return data        

def browser(link):
    browser = mechanize.browser()
    document = browser.open(link) 
    if document.code <400:
        html = document.read()
        list__ = filtersoup(html)
        return list__
    else:
        print("error code:",document.code)
        sys.exit(1)

def main():
    tgt = sys.argv[1]
    links__ = browser(str(tgt))
    if len(links__) == 0:
        sys.exit('Nothing found in document')
    else:
        for link in links__:
            print ("link")

if __name__ == '__main__':
    main()            