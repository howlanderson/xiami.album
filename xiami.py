#!/usr/bin/env python
from pyquery import PyQuery as pq
from lxml import etree
import urllib
import urllib2
import time
import sys
import os

album_name = sys.argv[1]
album_url_name = urllib.quote(album_name.decode(sys.stdin.encoding).encode('utf-8'));
xiami_url = 'http://www.xiami.com/search?key=' + album_url_name + '&pos=1'
print xiami_url
d = pq(url=xiami_url)
try:
    p = d("div.albumBlock_list div.album_item100_block p.cover a.CDcover100")
    album_url = p.attr('href')
    print album_url
    album_url = 'http://www.xiami.com' + album_url
    print album_url
    d = pq(url=album_url)    
    p = d("a#cover_lightbox")
    cover_url = p.attr('href').encode("utf-8","ingnore")
    print cover_url
except Exception, e:
    print e
    sys.exit()

print cover_url
req = urllib2.Request(url=cover_url)
f= urllib2.urlopen(req)

(filepath,filename)=os.path.split(cover_url)
cover_type = os.path.splitext(filename)[1]

fp = open(album_name.decode(sys.stdin.encoding).encode(sys.stdin.encoding) + cover_type.lower(), 'wb')
cover_data = f.read()
fp.write(cover_data)
fp.close()
