## 使用说明
我来丢人了，做的比较菜，能跑就行，大家看着办吧

该项目是对英文文本（主要是AO3），基于[划词翻译](https://hcfy.app)插件网页全文翻译，制作中英对照机翻的脚本

如果程序跑不起来，先把所有文件的编码换成utf-8格式，再看json文件有没有格式错误

使用时下载这个项目，并配置python 3.x环境

最好有个高级点的文本编辑器，如VSCode


### txt文本

1.把网页全文翻译的结果粘贴到v.txt

2.双击r.py，重新打开v.txt

### 网页文本1

1.保存原文的HTML，粘贴到v.txt中

2.双击r - txtweb.py

3.在浏览器中打开v.txt，使用划词翻译插件网页翻译（设置插件允许访问本地文件）

4.翻译完毕后，把内容粘贴到v.txt中

5.双击r - txtweb.py，重新打开v.txt

### 网页文本2（暂时只使用AO3）

1.对网页使用划词翻译插件网页翻译

2.把翻译后的HTML粘贴到v.txt中

3.双击r -web.py，重新打开v.txt

## 文件说明

三个json文件都是用来文本替换的，不需要替换的话也别删，AAA替换标点，list替换中文译文错误（比如翻译人物名时译文跟约定的译文不同），namet将译文中的英文换成中文。

json文件每一行代表一项，冒号左边引号里是目标文本，右边引号是替换文本，可以使用正则表达式

如果要增加几个替换项目，把预设在文件里有逗号的空项目多复制粘贴一点。

s.css是HTML格式说明，t2sO类是原文，t2sT是译文，如果要隐藏原文或英文，只需把对应类里的`display:block;`改成`display:none;`

建议使用epub编辑器，将其保存为epub格式（比较好用的软件为[calibre](https://calibre-ebook.com/zh_HK)和[sigil](https://github.com/Sigil-Ebook/Sigil)）
