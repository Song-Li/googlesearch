import urllib.request as urllib2
from datetime import datetime

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}


with open('./result', 'r') as fp:
    for line in fp.readlines():
        line = line.strip()
        wp = urllib2.Request(line, headers=hdr)
        wp = urllib2.urlopen(wp)
        mybytes = wp.read()

        mystr = mybytes.decode('utf-8')
        wp.close()

        idx = mystr.find('<td class="lp">Subject</td>')
        idx = mystr.find('name">', idx)
        subject = mystr[idx + 6: mystr.find("</td>", idx)]

        idx = mystr.find('<td class="lp">Date</td>')
        idx = mystr.find('shed">', idx)
        date = mystr[idx + 6: mystr.find("</td>", idx)]
        date = date.split(',')[1]
        date = date.strip()
        date = '/'.join(date.split(' ')[0:3])
        date = datetime.strptime(date, "%d/%b/%Y")
        date = date.strftime("%m/%d/%Y")


        print('{},"{}",{},{},{}'.format(date, subject, line, "", ""))
