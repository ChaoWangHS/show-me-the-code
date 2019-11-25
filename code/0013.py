import os
import requests
import lxml.html

page = requests.get('http://tieba.baidu.com/p/2166231880').text
doc = lxml.html.document_fromstring(page)

img_path = './data'
if not os.path.exists(img_path):
    os.makedirs(img_path)
for idx, el in enumerate(doc.cssselect('img.BDE_Image')):
    with open(img_path + '/' + '%03d.jpg' % idx, 'wb') as f:
        f.write(requests.get(el.attrib['src']).content)
