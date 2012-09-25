class Source():
    name = 'doi'
    urlbase = 'dx.doi.org'

    def __init__(self, sid=None):
        self.sid = sid

    def parse_url(self, parsedurl):
        sid = None
        loc = parsedurl.netloc
        path = parsedurl.path
        if loc.find(self.urlbase) >= 0:
            self.sid = path.strip('/')

    def get_bibtex(self):
        import urllib2

        if 'file' in dir(self):
            f = open(self.file, 'r')
        else:
            url = 'http://' + self.urlbase + '/' + self.sid
            headers = dict(Accept='text/bibliography; style=bibtex')
            req = urllib2.Request(url, headers=headers)
            f = urllib2.urlopen(req)
        bibtex = f.read()
        f.close

        return bibtex
