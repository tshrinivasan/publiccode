  # -*- coding: utf-8 -*-
'''
Created on 11:36:24 AM , Jan 29, 2016 

@author: @rajasankar

email : errajasankarchem@gmail.com 

'''
from bs4 import BeautifulSoup
import os
import sys

# this part is needed for windows. In Linux, not needed. 
# reload(sys)
# sys.setdefaultencoding('UTF-8')

''' 
Extracting files from TVU site is somewhat difficult because the html files doesnt have
clear formating. So I used a circumvent steps to wriggle out the mess. 

1. Prettify the html so that structure could be easily understandable.
2. check the structure and extract text. 
3. remove the unwanted rows. This could be different steps because if html structured
    in such way, then it would be few steps. Like removing முகப்பு , தொடக்கம் etc. 
4. retain உரை part too. 
5. Then combine the single files into one html. 

For repeated tasks, this code may be combined and simplified. I kept the creating new
files because, it is the easy way to check formatting and other things. It would save
lot time  

Silapathikarm in TVU site http://www.tamilvu.org/slet/l3100/l3100lf1.jsp
'''

for filename1 in os.listdir('D:\\silpa\\silpa\\'):
    print filename1
    filename = open('D:\\silpa\\silpa\\' + filename1)
    E = filename.readlines()
    filename.close()
    soup = BeautifulSoup('\n'.join(E))
    soup.prettify()
    filename = open('D:\\silpa\\silpa1\\' + filename1, 'w')
    filename.write(soup.prettify())
    filename.close()

for filename1 in os.listdir('D:\\silpa\\silpa1\\'):
    print filename1
    filename = open('D:\\silpa\\silpa1\\' + filename1)
    E = filename.readlines()
    filename.close()
    soup = BeautifulSoup('\n'.join(E))
    filename1 = filename1.replace('.htm', '')
    filename = open('D:\\silpa\\silpa2\\' + filename1 + '.txt', 'w')
    filename.write(soup.getText())
    filename.close()   
    
for filename1 in os.listdir('D:\\silpa\\silpa2\\'):
    print filename1
    filename = open('D:\\silpa\\silpa2\\' + filename1)
    E = filename.readlines()
    filename.close()
    lineno = 0
    for i in range(0, len(E)):
        if E[i].find('முகப்பு') != -1:
            lineno = i
            break
    lines = []
    for i in E[lineno:]:
        if i == '\n':
            continue
        lines.append(i.strip())
    filename = open('D:\\silpa\\silpa3\\' + filename1, 'w')
    filename.write('\n'.join(lines))
    filename.close()

for filename1 in os.listdir('D:\\silpa\\silpa3\\'):
    print filename1
    filename = open('D:\\silpa\\silpa3\\' + filename1)
    E = filename.readlines()
    filename.close()
    lines = []
    for i in E:
        if i != '\n':
            lines.append(i)
    E = lines
    lines = []
    notneeded = ['முகப்பு\n', 'பக்கம் எண் :\n', 'தொடக்கம்\n', 'முன் பக்கம்\n', 'மேல்\n', 'அடுத்த பக்கம்\n']
    if E.count('உரை\n') > 0:
        indexofu = E.index('உரை\n')
    else:
        indexofu = 0
    for i in range(0, len(E)):
        if E[i] not in notneeded:
            if indexofu != 0:
                if (i != indexofu) and (i != indexofu - 1):
                    lines.append(E[i])
                else:
                    if i == indexofu - 1:
                        lines.append('\n' + E[i].strip('\n') + ' ')
                    if i == indexofu:
                        lines.append(E[i].strip('\n') + ' ')
            else:
                lines.append(E[i])
    filename = open('D:\\silpa\\silpa4\\' + filename1, 'w')
    filename.write(''.join(lines))
    filename.close()

allthings = []
allthings.append('<head>')
allthings.append('<meta charset="UTF-8">')
allthings.append('</head>')

for i in range(14, 1290):
    print i
    filename = open('D:\\silpa\\silpa4\\' + str(i) + '.txt')
    E = filename.readlines()
    filename.close()
    for j in E:
        allthings.append('<p>')
        if j.find('உரை') != -1:
            allthings.append('<b>')
            allthings.append(j)
            allthings.append('</b>')
        else:
            allthings.append(j)
        allthings.append('</p>')
    allthings.append('*--------*------------*-------------------*')
        
filename = open('D:\\silpa\\silpa5\\2.html', 'w')
filename.write(''.join(allthings))
filename.close()
