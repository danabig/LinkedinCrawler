from HTMLParser import HTMLParser

class LinkedHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.handleContent = False
        self.fieldText = ''
        self.openedTag = ''
        self.key = ''
        self.parsedJson = {"name":[], "title":[],"position":[],"summary":[],"skills":[]}

    def getJson(self):
        return self.parsedJson

    def handle_starttag(self, tag, attrs):
        if tag=='p' and len(attrs)>0 and attrs[0]==('class','headline title'):
            self.fieldText = "title: "
            self.handleContent = True
            self.openedTag = tag
            self.key = 'title'
        if tag=='h1' and len(attrs)>0 and attrs[0]==('id','name'):
            self.fieldText = "name: "
            self.handleContent = True
            self.openedTag = tag
            self.key = 'name'
        if tag=='tr' and len(attrs)>0 and attrs[0]==('data-section','currentPositionsDetails'):
            self.fieldText = "current position: "
            self.handleContent = True
            self.openedTag = tag
            self.key = 'position'
        if tag=='section' and len(attrs)>0 and attrs[0]==('id','summary'):
            self.fieldText = "summary: "
            self.handleContent = True
            self.openedTag = tag
            self.key = 'summary'
        if tag=='section' and len(attrs)>0 and attrs[0]==('id','skills'):
            self.fieldText = "skills: "
            self.handleContent = True
            self.openedTag = tag
            self.key = 'skills'

    def handle_endtag(self, tag):
        if tag==self.openedTag:
            self.handleContent = False
            self.fieldText = ''
            self.openedTag = ''

    def handle_data(self, data):
        if data=='':
            return
        if self.handleContent:
            self.parsedJson[self.key].append(data)