# githubRelational
the relational network of github
这是用来获取github上，关系网络的python程序。他使用python来进行爬取和分析，使用d3.js进行可视化展示。

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