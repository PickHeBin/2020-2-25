"""
第一步:
    导入需要用到的包(模块)

"""

import requests    # 用来模拟浏览器发送网络请求
from lxml import etree  # 用来对需要解析提取的数据主体做预处理,让数据更方便我们处理
from urllib import request  # 用request里的urlretrive()方法下载图片
import time   # 让程序延迟几秒再进行(为什么呢?如果请求过快,会让目标网站开启反扒手段,如果把咱们IP封了,那就不好玩了.

"""
函数的封装:稍微讲解下
"""
def huya_spider():
    # 请求数据

    """
    url:什么是url?
    咱们先看一下这个频道的url,也就是咱们所要爬取的页面,写到这里
    """

    url = 'https://www.huya.com/g/4079'

    User_Agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"

    headers = {
        'User_Agent': User_Agent
    }


    response = requests.get(url, headers=headers)
    data_txt = response.text
    print(data_txt)

    data = etree.HTML(data_txt)
    # 数据分析 xpath 进行数据提取 数据清洗
    friends_list = data.xpath('//img[@class="pic"]')

    """
    咱们打印下friends_list 看看具体是什么样的数据
    """
    print(friends_list)

    """
    咱们发现这个friends_list是一个列表,那咱们就可以通过for循环遍历一下这个列表,
    依次把图片的url地址拿出来,再一张一张地下载.
    """
    for friend in friends_list:

        img = friend.xpath('./@data-original')[0]

        """
        这一步的目的呢,是老师发现,删掉img的url的?后面,图片会变得更大更清晰,大家鉴赏一下(演示一下).
        """
        img = img.split("?")[0]

        """
        咱们在这里先设置一个名字name,用来给每张图片命名.
        """
        name = friend.xpath('./@alt')[0]

        """
        下载的时候咱们使用request(没有s的这个)里面的urlretrive()方法
        在这个方法中,需要咱们输入两个参数,这两个参数分别是:图片的url地址,把图片下载到电脑的哪个文件夹,
        文件名是什么,为了方便区分,老师就把小姐姐直播室的名字作为图片的名字进行存储.
        """
        request.urlretrieve(img, 'friends/'+ name + '.jpg')

        """
        显示一下打印进度,爬虫效果更直观
        
        讲解下字符串的替换
        """

        print("<%s>下载完毕!" % name)

        """
        为了防止被网站拉黑封IP,咱们控制一下爬取速度
        """
        time.sleep(3)


"""
调用函数
"""
huya_spider()
