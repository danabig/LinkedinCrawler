import unicodedata
from bs4 import BeautifulSoup


class MyHTMLParser:
    def __init__(self, html_doc):
        self.soup = BeautifulSoup(html_doc, 'html.parser')
        self.parsedJson = {"name":[], "title":[],"position":[],"summary":[],"skills":[]}
        self.getskills()
        self.getsummary()
        self.getposition()
        self.gettitle()
        self.getname()

    def gettitle(self):
        titleTag = self.soup.find(class_="headline title")
        self.parsedJson['title'] = self.convertToString(titleTag.get_text())

    def getname(self):
        nametag = self.soup.find(id="name")
        self.parsedJson['name'] = self.convertToString(nametag.get_text())

    def getposition(self):
        for tr in self.soup.find_all('tr'):
            if tr['data-section'] == "currentPositionsDetails":
                self.parsedJson['position'] = self.convertToString(tr.get_text())
                return

    def getsummary(self):
        nametag = self.soup.find(id="summary")
        self.parsedJson['summary'] = self.convertToString(nametag.get_text())

    def getskills(self):
        nametag = self.soup.find(id="skills")
        self.parsedJson['skills'] = self.convertToString(nametag.get_text())

    def convertToString(self, text):
       return unicodedata.normalize('NFKD', text).encode('ascii','ignore')

    def getJson(self):
        return self.parsedJson