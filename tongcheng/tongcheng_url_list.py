from bs4 import BeautifulSoup
import requests

urlhost = 'http://wh.58.com/'
url = 'http://wh.58.com/sale.shtml?PGTID=0d100000-0009-e3f7-bb14-9a74d1e0aee7&ClickID=3'
header = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/49.0.2623.108 Chrome/49.0.2623.108 Safari/537.36',
    'Cookie': 'ganji_uuid=1605030515337855910737; ganji_xuuid=b6089d07-f775-437a-a2e4-6fbf69c689b5.1462429425531; GANJISESSID=1a42b69a75db34b54cd18195f2c8e05d; lg=1; citydomain=gz; __utmt=1; __utma=32156897.160040043.1462429425.1462881135.1462888401.4; __utmb=32156897.3.10.1462888401; __utmc=32156897; __utmz=32156897.1462878247.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _gl_tracker=%7B%22ca_source%22%3A%22www.baidu.com%22%2C%22ca_name%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_id%22%3A%22-%22%2C%22ca_s%22%3A%22seo_baidu%22%2C%22ca_n%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22sid%22%3A68646753735%7D',
    'Host': 'Host:gz.ganji.com'
}


def ganji_index_url(url):
    wd_data = requests.get(url, headers=header)
    wd_data.encoding = 'utf-8'
    suop = BeautifulSoup(wd_data.text, 'lxml')
    link = suop.select('li  b a')
    for links in link:
        page_url = urlhost + links.get('href')
        print(page_url)





url_list = '''
    http://wh.58.com//shouji/
    http://wh.58.com//tongxunyw/
    http://wh.58.com//danche/
    http://wh.58.com//fzixingche/
    http://wh.58.com//diandongche/
    http://wh.58.com//sanlunche/
    http://wh.58.com//peijianzhuangbei/
    http://wh.58.com//diannao/
    http://wh.58.com//bijiben/
    http://wh.58.com//pbdn/
    http://wh.58.com//diannaopeijian/
    http://wh.58.com//zhoubianshebei/
    http://wh.58.com//shuma/
    http://wh.58.com//shumaxiangji/
    http://wh.58.com//mpsanmpsi/
    http://wh.58.com//youxiji/
    http://wh.58.com//jiadian/
    http://wh.58.com//dianshiji/
    http://wh.58.com//ershoukongtiao/
    http://wh.58.com//xiyiji/
    http://wh.58.com//bingxiang/
    http://wh.58.com//binggui/
    http://wh.58.com//chuang/
    http://wh.58.com//ershoujiaju/
    http://wh.58.com//bangongshebei/
    http://wh.58.com//diannaohaocai/
    http://wh.58.com//bangongjiaju/
    http://wh.58.com//ershoushebei/
    http://wh.58.com//yingyou/
    http://wh.58.com//yingeryongpin/
    http://wh.58.com//muyingweiyang/
    http://wh.58.com//muyingtongchuang/
    http://wh.58.com//yunfuyongpin/
    http://wh.58.com//fushi/
    http://wh.58.com//nanzhuang/
    http://wh.58.com//fsxiemao/
    http://wh.58.com//xiangbao/
    http://wh.58.com//meirong/
    http://wh.58.com//yishu/
    http://wh.58.com//shufahuihua/
    http://wh.58.com//zhubaoshipin/
    http://wh.58.com//yuqi/
    http://wh.58.com//tushu/
    http://wh.58.com//tushubook/
    http://wh.58.com//wenti/
    http://wh.58.com//yundongfushi/
    http://wh.58.com//jianshenqixie/
    http://wh.58.com//huju/
    http://wh.58.com//qiulei/
    http://wh.58.com//yueqi/
    http://wh.58.com//tiaozao/


'''