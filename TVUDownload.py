# -*- coding: utf-8 -*-
'''
Created on 9:24:28 AM , Jan 30, 2016 
@author: @rajasankar
'''
import requests

''' 
downloading from TVU site is like any other site. if you know the link to that file, then
download helpers would take care of the rest. 

So the tricky part is to get the file links. As with the html structure this is organized in
messy way. Steps are listed below. 

1. go to to TVU site and access the book you need. 
2. then use firebug inspect element to get the background link. 
3. That is, address in browser would be same but the page would be servered using 
    AJAX call. So we need to know that url to downlod. 
4. url would be look like this 
    /slet/l3700/l3700son.jsp?subid=1247
    /slet/l3100/l3100pd1.jsp?bookid=56&auth_pub_id=71&pno=1
5. access few pages to get the idea of which part of url is changed to get the pages
    it would be incremental number AFAIK. 
6. get the first page url and last page url you need, take the numbers
7. format the download use like this 
    url = 'http://www.tamilvu.org/slet/l3700/l3700son.jsp?subid=' + str(i) + ''
    notice the http://www.tamilvu.org/ part
8. call the url in a for loop of starting and final page numbers. get the content and 
    write to file. 
9. In requests, you can use proxy if needed. for proxy authentication use urllib3
'''
proxies = {"http": "<proxy ip>:<port>", "https": "<proxy ip>:<port>"}  # use proxy
httplink = '<websitename_link>'  # this would be unchanged part of the url. 
startingpagenumber = 0  # use the numbers from website
finalpagenumber = 0
for i in range(startingpagenumber, finalpagenumber + 1):
    url = httplink + str(i)  # change this
    # reply=requests.get(url, proxies=proxies)
    reply = requests.get(url)
    print url, 'Status is ' + str(reply.status_code)
    filename = str(i).zfill(5) + '.html'
    filetowrite = open(filename, 'w')
    filetowrite.write(reply.content)
    filetowrite.close()
