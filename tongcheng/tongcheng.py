from bs4 import BeautifulSoup
import requests
import time
import pymongo

clint = pymongo.MongoClient('Localhost', 27017)
tongcheng = clint['tongcheng']
tongcheng_url_list = tongcheng['url_list']
tongcheng_item_info = tongcheng['item_info']

url = 'http://wh.58.com/tiaozao/'

header1 = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/49.0.2623.108 Chrome/49.0.2623.108 Safari/537.36',
    'Cookie': 'userid360_xml=1CD729C115D874E6F3E541BD567526F4; time_create=1465470715289; f=n; bangbangid=1080863914182732187; id58=c5/nn1cq5uwoe0kzCBIiAg==; mcity=ganzhou; als=0; myfeet_tooltip=end; wh=20165919525; bj58_id58s="V0ZVQktpTk4wSGluNzM0Mg=="; bdshare_firstime=1462881041052; bangbigtip2=1; city=ganzhou; __utma=253535702.1199027134.1462878323.1462878323.1462882132.2; __utmz=253535702.1462882132.2.2.utmcsr=ganzhou.58.com|utmccn=(referral)|utmcmd=referral|utmcct=/fushi/25931719565633x.shtml; 58home=wh; bj58_new_session=1; bj58_init_refer=""; bj58_new_uv=3; f=n; 58tj_uuid=edea702c-ba74-48e3-8628-70f225f57af2; new_session=1; new_uv=3; utm_source=; spm=; init_refer=; final_history=25885353146554%2C25282306671283%2C25877130164534%2C25697991776817%2C25747325290161; ipcity=ganzhou%7C%u8D63%u5DDE',
    'Host': 'wh.58.com'
}


def get_links_from(channel, pages, who_well=0):
    list_view = '{}{}/pn{}/'.format(channel, who_well, pages)

    wd_data = requests.get(list_view)
    wd_data.encoding = 'utf-8'
    suop = BeautifulSoup(wd_data.text, 'lxml')
    for link in suop.select('td.t > a[href^="http://wh.58.com/"]'):
        item_link = link.get('href')
        tongcheng_url_list.insert_one({'url': item_link})

# 获取流量量
def get_views_from(url):
    url_id = url.split('=')[-1].split('_')[0]
    api = 'http://jst1.58.com/counter?infoid={}'.format(url_id)
    header = {
        'Referer': url_id
    }
    js = requests.get(api, headers=header)
    views = js.text.split('=')[-1]
    return int(views)


def get_item_info(url, data=None):
    wd_data = requests.get(url, headers=header1)
    time.sleep(2)
    wd_data.encoding = 'utf-8'
    soup = BeautifulSoup(wd_data.text, 'lxml')

    if soup.select('h1.item'):
        pass
    else:
        try:
            data = {
                'title': soup.title.text,
                'price': soup.select('.price')[0].text.strip(),
                'area': list(soup.select('.c_25d')[0].stripped_strings) if soup.find_all('span', 'c_25d') else None,
                'date': soup.select('.time')[0].text,
                'views': get_views_from(url),
                'url': url.split('?')[0]
            }
            print(data)
            tongcheng_item_info.insert_one(data)
        except AttributeError:
            pass
        except IndexError:
            pass


