import sys
import requests
import lxml.etree as et
import lxml.html as html

def parseUrl(url):
    # LOAD XML AND XSL SOURCES
    res = requests.get(url)
    doc = lxml.html.fromstring(res.content)
    xsl = et.parse('xslt/akafist.xsl')

    # TRANSFORM SOURCE
    transform = et.XSLT(xsl)
    result = transform(doc)

    # OUTPUT TO SCREEN
    return result

if len(sys.argv) == 1:
  raise Exception("You should provide URL to parse as the first argument")

obj = parseUrl(sys.argv[1])
print(json.dumps(obj,ensure_ascii=False))
