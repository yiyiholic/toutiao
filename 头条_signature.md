# 头条搜索_signature获取

- 叨叨：爬取今日头条搜索内容的时候发现头条是动态更新网页即Ajax，其URL组成如下：

~~~json
Query String Parameters:
aid: 24
app_name: web_search
offset: 0
format: json
keyword: 街拍
autoload: true
count: 20
en_qc: 1
cur_tab: 1
from: search_tab
pd: synthesis
timestamp: 1594006097370
_signature: .0MBSAAgEBCYzKxEZW5Jgv9CQFAAKBLKqSwQa5QsLIgVuvsezbHEoRAIJakiK.LwoSGCGVYk07eJ1JadHrTLLM3jVeDq5XHyxBTHyTypQnqszymfpqrn81JF5MJyzccfYdS
~~~

其中有个参数\_signature，该参数是头条对URL执行某个算法得到的。接下来就说说如何重新构造这个\_signature。

1. 首先全局查找\_signature，得到如下结果：

   ![p1](C:\Users\YEE\Desktop\GitHub\python_learn\Python3WebCrawlerDevelopmentCombat\4\p1.PNG)

2. 我们打开lib***.js文件，全局查找\_signature，找到相关代码如下：

   ![p2](C:\Users\YEE\Desktop\GitHub\python_learn\Python3WebCrawlerDevelopmentCombat\4\p2.PNG)

   ![p3](C:\Users\YEE\Desktop\GitHub\python_learn\Python3WebCrawlerDevelopmentCombat\4\p3.PNG)

3. 进入window.byted_acrawler可以看到如下代码：

   ![p4](C:\Users\YEE\Desktop\GitHub\python_learn\Python3WebCrawlerDevelopmentCombat\4\p4.PNG)

4. 刷新网页

![image-20200706153053979](C:\Users\YEE\Desktop\GitHub\python_learn\Python3WebCrawlerDevelopmentCombat\4\p5.png)

5. 接下来进入sign函数得到我们需要的js，并把这个js下载到本地，然后在js代码的结尾添加代码如下：

   ![image-20200706153553637](C:\Users\YEE\Desktop\GitHub\python_learn\Python3WebCrawlerDevelopmentCombat\4\p6.png)

6. 获取到新的_signature添加到原始url中得到的结果如下：

   ![image-20200706153825520](C:\Users\YEE\AppData\Roaming\Typora\typora-user-images\image-20200706153825520.png)

* 总结一下：
  * 其实这个过程相当于把自己down今日头条代码，把对url加密的算法执行一次。