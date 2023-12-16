# -*- coding: UTF-8 -*-
import os
import re
import json

file='v.txt'
listn='list.json'
num=0
count=0
file_data=''
AAA=[]
list=[]
namet=[]
with open('AAA.json','r',encoding='utf-8') as f:
    AAA=json.load(f,encoding='utf-8')
if os.path.isfile(listn):
    with open(listn, 'r', encoding='utf-8') as f:
        list = json.load(f, encoding='utf-8')
with open(file, "r",encoding='utf-8') as f:
    for line in f:
        line=re.sub('Summary:概括：','Summary:',line)
        line=re.sub('Chapter Text章节正文','',line)
        line=re.sub('Notes:笔记：','Notes:',line)
        line=re.sub('Work Text:作品正文：','Work Text:',line)
        for s,v in list.items():
            if s !=v and s.strip()!="":
                line=re.sub(s,v,line,flags=re.I).lstrip()
        for s,v in AAA.items():
            if s !=v and s.strip()!="":
                line=re.sub(s,v,line).lstrip()
        if line=='':
            line='\n'
        file_data += line
    f.close()
fo=open(file,"w+",encoding='utf-8')
fo.write(file_data)
fo.close()
exit()        

