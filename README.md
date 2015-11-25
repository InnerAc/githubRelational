# githubRelational
the relational network of github
这是用来获取github上，关系网络的python程序。他使用python来进行爬取和分析，使用d3.js进行可视化展示。


## 仅仅是为了好玩

如果，你现在不想运行，而只是想看看效果，可以直接启动`start.sh`或`start.bat`脚本，然后打开浏览器"localhost:8888/show.html"查看，期间仅仅需要一个`python`的运行环境。

如果你连`python`的环境都没有，那也没关系，你可以打开`show.html`，将其中`json`的路径替换为"https://raw.githubusercontent.com/InnerAc/githubRelational/master/info.json"
然后直接使用浏览器打开该文件即可。

打开浏览器后建议缩放到最小，然后将屏幕拖到中间。

展示图片如下:
![展示]("http://pfile.cn/ddjdw1-l")

## 部署
在部署之前，你首先应该拥有一下环境:
```sh
python
python-bs4
```
拥有环境之后，将项目`clone`下来
- sql.py 首先创建一个数据库和需要的数据表
- start.py 开始进行爬取
- calData.py 给爬取的人物创建边关系
- calValue.py 给边关系增加权重
- calPerson.py 精简人物，只保留需要可视化的部分
- getJson.py `or` getNum.py 得到所需要想json文件
- start.sh `or` start.bat  启动简易服务器进行查看，默认端口8888

然后在浏览器中输入:"localhost:8888/show.html"

如果是`firefox`等支持读取本地json的可以不用启动服务器，但是要修改`show.html`文件中的`json`文件路径。
