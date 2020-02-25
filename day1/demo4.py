#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : demo4.py
# Author: MuNian
# Date  : 2020-01-07

import requests

# 页面链接
urls = 'https://www.lagou.com/jobs/list_Python%E7%88%AC%E8%99%AB%E5%B7%A5%E7%A8%8B%E5%B8%88?labelWords=&fromSearch=true&suginput='
# 数据链接
url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'

data = {
    'first': 'true',
    'pn': '1',
    'kd': 'Python爬虫工程师',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Host': 'www.lagou.com',
    'Referer': 'https://www.lagou.com/jobs/list_Python%E7%88%AC%E8%99%AB%E5%B7%A5%E7%A8%8B%E5%B8%88?labelWords=&fromSearch=true&suginput=',

    # =20200107213816-c7764e95-23f3-4540-9f7e-2d01d9c93087; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1578404299; _ga=GA1.2.1273547907.1578404300; _gat=1; LGSID=20200107213819-f7392b72-3152-11ea-a71a-5254005c3644; PRE_UTM=m_cf_cpt_baidu_pcbt; PRE_HOST=sp0.baidu.com; PRE_SITE=https%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc.php%3Ft%3D06KL00c00fZNKw_0k2Ph0FNkUsjDBwwX00000F2xgNC00000TxppH6.THd_myIEIfK85yF9pywdpAqVuNqsusK15yNWuWcznvDznj01mW9-n1c0IHYvwWbLwHnvrjndPjfzPH7jwjD3nHc1wWPAfW9DnR7aPsK95gTqFhdWpyfqn1n1nWfkn1nYnBusThqbpyfqnHmhIAYqniuB5HD0uHdCIZwsT1CEQLILIz4_myIEIi4WUvYEUA78uA-8uzdsmyI-QLKWQLP-mgFWpa4CIAd_5LNYUNq1ULNzmvRqUNqWu-qWTZwxmh7GuZNxTAPBI0KWThnqPWDsPjm%26tpl%3Dtpl_11534_21264_17382%26l%3D1516085138%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2525E5%252587%252586%2525E5%2525A4%2525B4%2525E9%252583%2525A8-%2525E6%2525A0%252587%2525E9%2525A2%252598-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253D%2525E3%252580%252590%2525E6%25258B%252589%2525E5%25258B%2525BE%2525E3%252580%252591-%252520%2525E4%2525BA%252592%2525E8%252581%252594%2525E7%2525BD%252591%2525E9%2525AB%252598%2525E8%252596%2525AA%2525E5%2525A5%2525BD%2525E5%2525B7%2525A5%2525E4%2525BD%25259C%2525EF%2525BC%25258C%2525E5%2525AE%25259E%2525E6%252597%2525B6%2525E6%25259B%2525B4%2525E6%252596%2525B0%21%2526xp%253Did%28%252522m3332413342_canvas%252522%29%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D232%26wd%3Dlagou%26issp%3D1%26f%3D8%26ie%3Dutf-8%26rqlang%3Dcn%26tn%3Dbaiduhome_pg%26inputT%3D1192; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flanding-page%2Fpc%2Fsearch.html%3Futm_source%3Dm_cf_cpt_baidu_pcbt; LGUID=20200107213819-f7392e1b-3152-11ea-a71a-5254005c3644; JSESSIONID=ABAAABAAAFCAAEGA98EEA17838C5941333AB7F538148A3C; WEBTJ-ID=20200107213822-16f803a4d5c553-0d1bf83113e75f-6701b35-2073600-16f803a4d5d567; _gid=GA1.2.370703971.1578404303; index_location_city=%E5%85%A8%E5%9B%BD; TG-TRACK-CODE=index_search; X_HTTP_TOKEN=77c6cc1dc661c50a8034048751ea30232abc719298; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216f803a6d8cca-0a37d1750adb4c-6701b35-2073600-16f803a6d8d2f3%22%2C%22%24device_id%22%3A%2216f803a6d8cca-0a37d1750adb4c-6701b35-2073600-16f803a6d8d2f3%22%7D; sajssdk_2015_cross_new_user=1; LGRID=20200107213829-fd2c19c7-3152-11ea-a71a-5254005c3644; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1578404311; SEARCH_ID=4b45872df20242269f0b5a41126a40f9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}
# 创建一个session(状态保持)
session = requests.session()
data1 = session.get(url=urls, headers=headers, verify=False, timeout=3)
cookie = data1.cookies

# response = requests.post(url, headers=headers, data=data, verify=False).json()
response = session.post(url=url, headers=headers, data=data, cookies=cookie, verify=False, timeout=3).json()
print(response)
