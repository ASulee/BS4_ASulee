import time
from tongcheng import tongcheng_url_list, tongcheng_item_info

while True:
    print(tongcheng_item_info.find().count())
    time.sleep(5)