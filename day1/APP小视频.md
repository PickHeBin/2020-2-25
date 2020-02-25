```Python
import requests
from urllib3.exceptions import InsecureRequestWarning
import urllib3

# InsecureRequestWarning
# 禁用安全请求警告
urllib3.disable_warnings(InsecureRequestWarning)

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 OPR/65.0.3467.62'
}


def Video_Dowloads(page):
    url = 'https://v.6.cn/coop/mobile/index.php?act=recommend&padapi=minivideo-getlist.php&page=' + str(page)
    response = requests.get(url, headers=headers, verify=False).json()
    data = response['content']['list']
    for i in data:
        title = i['title']
        data = i['playurl']
        Video_data(data, title)


def Video_data(video_url, title):
    response = requests.get(video_url, headers=headers, verify=False)
    try:
        with open('Video/{}.mp4'.format(title), 'ab') as f:
            f.write(response.content)
            print('正在下载{}....'.format(title))
    except Exception as e:
        pass


if __name__ == '__main__':
    for i in range(1, 10):
        Video_Dowloads(i)
```

```
课题:PythonAPP抓包零基础入门实战 -- 一键抓取抖音全网小视频 围观小姐姐
```

