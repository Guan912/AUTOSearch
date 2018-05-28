# -*- coding: utf-8 -*-

import io  
import os  
import sys  
from bs4 import BeautifulSoup  
import datetime  
import random  
import re  
import chardet


#reload(sys) 
#sys.setdefaultencoding('utf-8')

from requests import Session

headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3357.400 QQBrowser/9.6.11858.400",
	}

#得到某一个分页的所有文章的链接  
articles=set()  
def getArticleLinks(pageUrl):
    s=Session()
    
    #获取网页信息  
    html=s.post(pageUrl,headers) 
    bsObj=BeautifulSoup(html.text,"html.parser")
    global articles  
 
    for articlelist in bsObj.findAll("td",{"class":"list_tr"}):  #正则表达式匹配每一篇文章链接   
        if 'href' in articlelist.a.attrs:  
            if articlelist.a.attrs["href"] not in articles:  
                #遇到了新界面  
                newArticle=articlelist.a.attrs["href"]    
                articles.add(newArticle)    
  
#写入文本  
def data_out(data):
        with open(r'E:\xueyuantongzhi.txt','a+') as out:
                
                out.write('\n')
                out.write(data)
                out.close()

#得到某个主页上所有分页的链接，根据分页链接得到每一篇文章的链接并爬取博客每篇文章的文字
pages=set()  
def getPageLinks(tongzhiye):  

     s=Session()
     html=s.post(tongzhiye,headers) 
     bsObj=BeautifulSoup(html.text,"html.parser")
     
     #获取当前页面(第一页)的所有文章的链接  
     getArticleLinks(tongzhiye)  
     #去除重复的链接  
     global pages  
     for pagelist in bsObj.findAll("a",href=re.compile("^/([A-Za-z0-9]+)(/list)([0-9]+)(.htm)*$")):#正则表达式匹配分页的链接  
         if 'href' in pagelist.attrs:  
             if pagelist.attrs["href"] not in pages:  
                 #遇到了新的界面  
                 newPage=pagelist.attrs["href"]  
                 #print(newPage)  
                 pages.add(newPage)  
                 #获取接下来的每一个页面上的每一篇文章的链接  
                 newPageLink="http://au.njust.edu.cn/"+newPage  
                 getArticleLinks(newPageLink)  
                 #爬取每一篇文章的文字内容  
                 for articlelist in articles:  
                     newarticlelist="http://au.njust.edu.cn/"+articlelist  
                     print(newarticlelist)
                     data_out(newarticlelist)                    
                     getArticleText(newarticlelist)  

getPageLinks("http://au.njust.edu.cn/2075/list.htm")  
#参考：https://blog.csdn.net/HW140701/article/details/55210367
