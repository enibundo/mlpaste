import httplib, urllib, sys, os
from optparse import OptionParser
ext = [("c", "c", "C"),
       ("cpp", "cpp", "C++"),
       ("html", "html", "HTML")]
def findLanguage(fn):
    fileName, fileExtension = os.path.splitext(fn)
    
    for e in ext:
        if e[0]==fileExtension[1:]:
            return e[1]
    return "text"


parser = OptionParser()
parser.add_option("-l", "--language", help="language you want")

(options, args) = parser.parse_args()
print options
print args
headers = {"Content-type":"application/x-www-form-urlencoded", "Accept":"text/plain"}
for filename in args:
    try:
        language = options.language
        if language==None:
            raise KeyError
    except KeyError:
        language = findLanguage(filename)
    file = open(filename, 'r')
    str_code = file.read()
    params = urllib.urlencode({'code':str_code,
                               'language':language})
    
    conn = httplib.HTTPConnection("paste.pocoo.org")
    conn.request("POST", "", params, headers)
    response=conn.getresponse()

    if response.status == 302:
        print response.getheader('location')
