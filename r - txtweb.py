# -*- coding: UTF-8 -*-
import os
import re
import json
import concurrent.futures
import math

file = 'v.txt'
listn = 'list.json'
lname = 'namet.json'
num = 0
count = 0
file_data = ''
stat = 0
threadnum = 300
count=0
AAA=[]
list=[]
namet=[]
with open('AAA.json','r',encoding='utf-8') as f:
    AAA=json.load(f,encoding='utf-8')
if os.path.isfile(listn):
    with open(listn, 'r', encoding='utf-8') as f:
        list = json.load(f, encoding='utf-8')
if os.path.isfile(lname):
    with open(lname, 'r', encoding='utf-8') as f:
        namet = json.load(f, encoding='utf-8')

with open(file, "r", encoding='utf-8') as f:
    file_data = f.read()
    if "【译文】" in file_data or "t2sT" in file_data:
        stat = 1
    if re.findall(r'<\/p>', file_data):
        if not stat:
            file_data = re.sub('\n', '', file_data)
            file_data = re.sub('<br/>', '</p><p>', file_data)
            file_data = re.sub('<br>', '</p><p>', file_data)
            file_data = re.sub('<p', '\n\n<p', file_data)
            file_data = re.sub('<span.*?>', '', file_data)
            file_data = re.sub('</span>', '', file_data)
            file_data = re.sub('</p>', '</p>\n\n', file_data)
            file_data = re.sub('<h1', '\n\n<h1', file_data)
            file_data = re.sub('</h1>', '</h1>\n\n', file_data)
            file_data = re.sub('<h2', '\n\n<h2', file_data)
            file_data = re.sub('</h2>( |\r|\n)*<h2.*?>', ' <br/>', file_data)
            file_data = re.sub('</h1>( |\r|\n)*<h1.*?>', ' <br/>', file_data)
            file_data = re.sub('</h2>', '</h2>\n\n', file_data)
            file_data = re.sub('<h3', '\n\n<h3', file_data)
            file_data = re.sub('</h3>', '</h3>\n\n', file_data)
            file_data = re.sub('<li', '\n\n<li', file_data)
            file_data = re.sub('</li>', '</li>\n\n', file_data)
            file_data = re.sub(' +', ' ', file_data)
            file_data = re.sub('<p>\t*<em>', '<p><em>', file_data)
            file_data = re.sub('</em>\t*</p>', '</em></p>', file_data)
            file_data = re.sub('<p> *<em>', '<p><em>', file_data)
            file_data = re.sub('</em> *</p>', '</em></p>', file_data)
            file_data = re.sub(r'<h3.*?>(Summary|Notes)\:</h3>', r'<p>\1:</p>', file_data)
            file_data = re.sub('<h3.*?>Work Text\:</h3>>', '', file_data)
            file_data = re.sub(r'<div class="byline">(.*?)</div>', r'<p class="byline">\1</p>', file_data)
            file_data = re.sub(r'<div class="endnote-link">(.*?)</div>', r'<p class="endnote-link">\1</p>', file_data)
        else:
            file_data = re.sub('( |\n)*【译文】( |\n)*', '\n【译文】', file_data)
            file_data = re.sub('</li>( |\n)*【译文】<li.*?><span.*?>', '<br/><span class="t2sT">', file_data)
        file_data = re.sub(' +<', ' <', file_data)
        file_data = re.sub('> +', '> ', file_data)
    else:
        file_data = f.read()
    f.close()
if file_data:
    fo = open(file, "w+", encoding='utf-8')
    fo.write(file_data)
    fo.close()
    file_data = ''
thli = []


def textconv(i):
    thli[i] = re.sub(r'【译文】<p class="byline heading.*', '', thli[i])
    thli[i] = re.sub(r'<h1(.*?)>', r'<h1\1>', thli[i])
    thli[i] = re.sub(r"【译文】<h1(.*?)>", r"<h1\1>", thli[i])
    if not re.findall(r't2sO', thli[i]):
        thli[i] = re.sub(r'<p(.*?)>', r'<p\1 class="t2sO">', thli[i])
    if not re.findall(r't2sO', thli[i]):
        thli[i] = re.sub(r'<li(.*?)>(.*?)</li>', r'<li\1><span class="t2sO">\2</span></li>', thli[i])
    if re.findall(r'【译文】.*?t2sO', thli[i]):
        thli[i] = re.sub(r"【译文】<p(.*?)t2sO(.*?)>", r"【译文】<p\1t2sT\2>", thli[i])
        thli[i] = re.sub(r"【译文】<li(.*?)t2sO(.*?)>", r"【译文】<li\1t2sT\2>", thli[i])
    elif re.findall(r'【译文】', thli[i]):
        thli[i] = re.sub(r'<p(.*?)>', r'<p\1 class="t2sT">', thli[i])
        thli[i] = re.sub(r't2sT t2sT', r't2sT', thli[i])
    if re.findall(r'>Summary\:*<', thli[i]):
        thli[i] = '<p>Summary:</p>\n\n'
    if re.findall(r'>Notes*\:*<', thli[i]):
        thli[i] = '<p>Notes:</p>\n\n'
    thli[i] = re.sub(r'<h2(.*?)>', r'<h2\1>', thli[i])
    thli[i] = re.sub(r"【译文】<h2(.*?)>", r"<h2\1>", thli[i])
    thli[i] = re.sub(r'<h3(.*?)>', r'<h3\1>', thli[i])
    thli[i] = re.sub(r"【译文】<h3(.*?)>", r"<h3\1>", thli[i])
    thli[i] = re.sub(r'【译文】<p class="byline heading.*', '', thli[i])
    thli[i] = re.sub(r'<h3(.*?)>.*?<a rel="author".*>(.*?)</a>.*?</h3>', r'<p\1>\2</p>', thli[i])

    if re.findall('>(总结|注意事项：|Work Text)(：|\:)*<', thli[i]):
        thli[i] = '\n'
    if re.findall(r'<p.*?class=".*?byline', thli[i]):
        thli[i] = re.sub('<p.*?>', '<p class="byline">', thli[i])
    while re.findall(r' class=".*?" class=".*?"', thli[i]):
        thli[i] = re.sub(r' class="(.*?)"(.*?) class="(.*?)"', r' class="\1 \3"\2', thli[i])
    if re.findall('t2sT', thli[i]) and re.findall('t2sO', thli[i]):
        thli[i] = re.sub(' *t2sO', '', thli[i])
    thli[i] = re.sub(r'<li><span.*?>(.*?)</span><br/><span.*?>(.*?)</span></li>',
                     r'<li><span class="t2sO">\1</span><br/><span class="t2sT">\2</span></li>',
                     thli[i])
    if re.findall(r'<h(1|2)', thli[i])!=[]:
        for s, v in list.items():
            if s != v and s.strip() != "":
                thli[i] = re.sub(s, v, thli[i], flags=re.I).lstrip()
    if re.findall(r'((【译文】)|(t2sT))', thli[i]):
        if not re.findall('</*?(p|h2|h1|h3|li).*?>', thli[i], flags=re.I):
            thli[i] = '\n'
        if re.findall('endnote-link', thli[i]):
            thli[i] = '\n'
        for s, v in list.items():
            if s != v and s.strip() != "":
                thli[i] = re.sub(s, v, thli[i], flags=re.I).lstrip()
        for s, v in namet.items():
            if s != v and s.strip() != "":
                s = ' *' + s + ' *'
                thli[i] = re.sub(s, v, thli[i])
    if thli[i] == '':
        thli[i] = '\n'
    for s,v in AAA.items():
        if s !=v and s.strip()!="":
            thli[i]=re.sub(s,v,thli[i])
    thli[i] = re.sub(r'(<\!--)*【译文】(-->)*', '', thli[i])
    thli[i] = re.sub(r'<p.*?>Chapter End Notes</p>', '<p>Chapter End Notes</p>', thli[i])
    thli[i] = re.sub(r'<p class=".*?endnote-link.*?">', '<p class="endnote-link">', thli[i])
    thli[i] = re.sub(r'<p.*?>Chapter Summary</p>', '<p>Chapter Summary</p>', thli[i])
    thli[i] = re.sub(r'< +', '<', thli[i])
    thli[i] = re.sub(r' +>', '>', thli[i])
    thli[i] = re.sub('</李>', '</li>', thli[i])
    thli[i] = re.sub('<p.*?>End Notes</p>', '<p>End Notes</p>', thli[i])
    thli[i] = re.sub(r'< *\/(.*?) *(.*?) *>', r'</\1\2>', thli[i])
    if re.findall('<p class="t2sT">(注意事项|笔记|章节注释|章节总结|概括|章*节*尾注)</p>', thli[i]):
        thli[i] = ''


with open(file, "r", encoding='utf-8') as f:
    thli = f.readlines()
    threadnum=int(math.sqrt(len(thli)))
    if threadnum < 50:
        threadnum=50
if stat:
    with concurrent.futures.ThreadPoolExecutor(max_workers=threadnum) as executor:
        tlist = {executor.submit(textconv, i): i for i in range(len(thli))}
        for future in concurrent.futures.as_completed(tlist):
            count = count + 1
fo = open(file, "w+", encoding='utf-8')
for line in thli:
    fo.write(line)
fo.close()
exit()
