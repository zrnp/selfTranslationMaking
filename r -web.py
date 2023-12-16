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

with open(file, "r",encoding='utf-8') as f:
    file_data=f.read()
    if re.findall(r'(p|h2|h3|li|h1)',file_data)!=[]:
        
        file_data=re.sub('\n','',file_data)
        file_data=re.sub(r'<br.*?>','</p><p>',file_data)
        file_data=re.sub(r'<div.*?>','',file_data)
        file_data=re.sub('</div>','',file_data)
        file_data=re.sub(r'<hcfy-result-content.*?>', '',file_data)
        file_data=re.sub(r'<\/hcfy-result-content>', '',file_data)
        file_data=re.sub(r'<hcfy-result-actions.*?>', '',file_data)
        file_data=re.sub(r'<\/hcfy-result-actions>', '',file_data)
        file_data=re.sub(r'<(p|h2|h3|li|h1)',r'\n\n<\1',file_data)
        file_data=re.sub(r'<\/(p|h2|h3|li|h1)>',r'</\1>\n\n',file_data)
        file_data=re.sub(' +',' ',file_data)
        
        file_data=re.sub(r'<p(.*?)>\t*<em>',r'<p\1><em>',file_data)
        file_data=re.sub('</em>\t*</p>','</em></p>',file_data)
        file_data=re.sub(r'<p(.*?)> *<em>',r'<p\1><em>',file_data)
        file_data=re.sub('</em> *</p>','</em></p>',file_data)
        file_data=re.sub('<h3.*?>Work Text\:</h3>>','',file_data)
        file_data=re.sub(r'<div class="byline">(.*?)<\/div>',r'<p class="byline">\1</p>',file_data)
        file_data=re.sub(r'<div class="endnote-link">(.*?)<\/div>',r'<p class="endnote-link">\1</p>',file_data)
        file_data=re.sub(' +<',' <',file_data)
        file_data=re.sub('> +','> ',file_data)
        file_data = re.sub('<span.*?>', '', file_data)
        file_data = re.sub('</span>', '', file_data)
        file_data = re.sub(r'<(p|li)(.*?)><(strong|em|i|b).*?>(.*?)<hcfy-result.*?>(.*?)<.hcfy-result>.*?<.(strong|em|i|b)><.(p|li)>', r'<\1\2 class="t2sO"><\3>\4</\3></\1>\n<\1\2 class="t2sT"><\3>\5</\3></\1>', file_data)
        file_data = re.sub(r'<(p|li).*?>(.*?)<hcfy-result.*?>(.*?)<.hcfy-result>.*?<.(p|li)>', r'<\1 class="t2sO">\2</\1>\n<\1 class="t2sT">\3</\1>', file_data)
        file_data = re.sub(r'<(h1|h2)(.*?)>(.*?)<hcfy-result.*?>(.*?)<.hcfy-result>.*?<.(h1|h2)>', r'<\1\2>\3\n<br/>\4</\1>', file_data)
        file_data = re.sub(r'<div class="byline">(.*?)<.div>', r'<p class="byline">\1</p>', file_data)
        file_data = re.sub(r'<div class="endnote-link">(.*?)<.div>', r'<p class="endnote-link">\1</p>', file_data)

    else:
        file_data=f.read()
    f.close()
if file_data:
    
    fo=open(file,"w+",encoding='utf-8')
    fo.write(file_data)
    fo.close()
    file_data=''
thli = []


def textconv(i):
    while re.findall("<(p|li)(.*?)>.*?<br",thli[i]):
        if '<em' in thli[i]:
            thli[i]=re.sub(r'<(p|li)(.*?)><em.*?>(.*?)<br.*?>(.*?)</em></(p|li)>',r'<\1\2><em>\3</em></\1><\1\2><em>\4</em></\1>',thli[i])
        else:
            thli[i]=re.sub(r'<(p|li)(.*?)>(.*?)<br.*?>(.*?)</(p|li)>',r'<\1\2>\3</\1><\1\2>\4</\1>',thli[i])
    thli[i] = re.sub(r'<h3 class="heading">(Summary|Notes)\:<hcfy-result.*?</h3>', r'<p>\1</p>', thli[i])
    thli[i]= re.sub(r'<h3 class="title">.*?<a.*?>Chpater(.*?)<hcfy-result.*?>(.*?)</hcfy-result.*?</h3>',r'<h2>\1<br/>\2</h2>',thli[i])
    if re.findall(r'>Summary\:*<', thli[i])!=[]:
        thli[i] = '<p>Summary:</p>\n\n'
    if re.findall(r'>Notes*\:*<', thli[i])!=[]:
        thli[i] = '<p>Notes:</p>\n\n'
    if re.findall('>Chapter Text<',thli[i]):
        thli[i]='\n'
    thli[i] = re.sub(r'<h2(.*?)>', r'<h2\1>', thli[i])
    thli[i] = re.sub(r'<h3(.*?)>', r'<h3\1>', thli[i])

    if re.findall('class="jump"', thli[i])!=[]:
        thli[i]=re.sub(' class="jump"',' class="endnote-link"',thli[i])
        if re.findall('t2sO', thli[i])!=[]:
            thli[i]=re.sub(' class="t2sO"','',thli[i])
        elif re.findall('t2sT', thli[i])!=[]:
            thli[i]='\n'
    if re.findall('>(总结|注意事项：|Work Text)(：|\:)*<', thli[i])!=[]:
        thli[i] = '\n'
    if re.findall(r'<p.*?class=".*?byline', thli[i]):
        thli[i] = re.sub('<p.*?>', '<p class="byline">', thli[i])
    while re.findall(r' class=".*?" class=".*?"', thli[i]):
        thli[i] = re.sub(r' class="(.*?)"(.*?) class="(.*?)"', r'\2 class="\1 \3"', thli[i])
    if re.findall('t2sT', thli[i]) and re.findall('t2sO', thli[i]):
        thli[i] = re.sub(' *t2sO', '', thli[i])
    if re.findall(r'<h(1|2)', thli[i])!=[]:
        for s, v in AAA.items():
            if s != v and s.strip() != "":
                thli[i] = re.sub(s, v, thli[i], flags=re.I).lstrip()
    if re.findall('t2sT', thli[i])!=[]:
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
    thli[i] = re.sub(r'<p.*?>Chapter End Notes</p>', '<p>Chapter End Notes</p>', thli[i])
    thli[i] = re.sub(r'<p class=".*?endnote-link.*?">', '<p class="endnote-link">', thli[i])
    thli[i] = re.sub(r'<p.*?>Chapter Summary</p>', '<p>Chapter Summary</p>', thli[i])
    thli[i] = re.sub(r'< +', '<', thli[i])
    thli[i] = re.sub(r' +>', '>', thli[i])
    thli[i] = re.sub('<p.*?>End Notes</p>', '<p>End Notes</p>', thli[i])
    thli[i] = re.sub(r'< *\/(.*?) *(.*?) *>', r'</\1\2>', thli[i])
    if re.findall('<hcfy-result.*(注意事项|笔记|章节注释|章节总结|概括|章*节*尾注)</p>', thli[i])!=[]:
        thli[i] = ''
    thli[i] = re.sub(r'(<hcfy.*?>|</hcfy.*?>)', '', thli[i])
    thli[i] = re.sub(r'<h3> *(.*?)<a.*?>(.*?)</a>(.*?) *</h3>', r'<h2>\1\2\3</h2>', thli[i])


with open(file, "r", encoding='utf-8') as f:
    thli = f.readlines()
    threadnum=int(math.sqrt(len(thli)))
    if threadnum < 10:
        threadnum=10
with concurrent.futures.ThreadPoolExecutor(max_workers=threadnum) as executor:
    tlist = {executor.submit(textconv, i): i for i in range(len(thli))}
    for future in concurrent.futures.as_completed(tlist):
        count = count + 1
fo = open(file, "w+", encoding='utf-8')
for line in thli:
    fo.write(line)
fo.close()


