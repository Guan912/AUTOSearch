# AUTOSearch
*A simple search engine for the contents of the college's notice.*
## ✏学习笔记
> 为了搜一个材料，发现找不到站内搜索😅</br>
正好看了数学之美，了解了一些爬虫、建索引、结果排序的内容</br>
学习一波，也方便一下自己</br>

## 📝 需求
对通知动态里的信息的标题（内容）进行检索

## 📝 思路
### 🍳 建spider（python）
> 1、爬所有通知的网页，存到数据库中</br>
2、从数据库中取url，把文章内容爬到数据库中（内容先不做）
### 🍳 建索引(c/c++)
> 1、分词程序：利用friso分词库，将所有文章标题（内容）切分成词语。</br>
2、建立倒排索引程序：处理所有分词程序产生的结果文件，建立倒排索引。
### 🍳 搜索结果(c/c++)
> 1、搜索程序：将输入句子切分成关键词，并根据关键词和倒排索引文件计算出相关文章的TF-IDF(词频-逆文件频率)，最后根据TF-IDF对搜索结果进行排序。
### 🍳 搜索页面(java)
> 搜索引擎的入口，输入搜索的内容，输出搜索的结果。
#### 🍲 快速做的话直接参考大触们的开源代码<br>
#### 🥣 以后可以参考源代码自己理解那些算法<br>
