# AUTOSearch
*A simple search engine for the contents of the college's notice.*
## ✏写在前面
> 为了搜一个材料，发现找不到站内搜索😅<br>
> 正好看了数学之美，了解了一些爬虫、建索引、结果排序的内容<br>
> 学习一波，也方便一下自己<br>

## 📝 需求
对通知动态里的信息的标题进行检索

### 🍳 建spider
> [](http://au.njust.edu.cn/2075/list.htm)
 [](http://au.njust.edu.cn/2076/list.htm)
 [](http://au.njust.edu.cn/2078/list.htm)
 [](http://au.njust.edu.cn/2080/list.htm)
 [](http://au.njust.edu.cn/2082/list.htm)

#### 准备工作

> python环境
>> python环境之前学习的时候搭建过了（其实爬过小虫，没深入了解，就是为了吃的爬了一下大众点评。。）

👉<img width="200" src="https://github.com/Guan912/AUTOSearch/blob/master/image00/1.jpg"/>

> 爬虫库
>> BeautifulSoup：最主要的功能是从网页抓取数据,推荐在现在的项目中使用Beautiful Soup 4，不过它已经被移植到BS4了，也就是说导入时我们需要 import bs4

>> urllib.request:提供了最基本的构造 HTTP 请求的方法，利用它可以模拟浏览器的一个请求发起过程，同时它还带有处理 authenticaton （授权验证）， redirections （重定向)， cookies (浏览器Cookies）以及其它内容

#### 通知页面分析

爬的是教学通知的http://au.njust.edu.cn/2075/list.htm

> 看了一下源，学校网站的都很规整，比较好找到要的flag啥的标签
### 🍲 快速做的话直接利用大触们的开源代码<br>
### 🥣 以后可以参考源代码自己理解那些算法<br>
