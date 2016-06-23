from multiprocessing import Pool
from tongcheng_url_list import url_list
from tongcheng import get_links_from, get_item_info, get_views_from
import pymongo

clint = pymongo.MongoClient('localhost', 27017)
tongcheng = clint['tongcheng']
tongchengurl_list = tongcheng['url_list']


# def get_58_links_from(chanel):
#     for i in range(1, 20):
#         get_links_from(chanel, i)
#
#
# def get_tongcheng_item(url):
#     pass

if __name__ == '__main__':
    pool = Pool(4)
    urlss = [item['url'] for item in tongchengurl_list.find()]
    pool.map(get_item_info, urlss)

