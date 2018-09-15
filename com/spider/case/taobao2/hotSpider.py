import re
import requests
import json
import time
import pymongo
import random


class mongocon:
    def __init__(self, url, name, pwd, database):
        self.url = url
        self.name = name
        self.pwd = pwd
        self.database = database
        self.db = pymongo.MongoClient(url)[database]

    def insert_many(self, collection, coll_name):
        self.db[coll_name].insert_many(collection)

    def insert_one(self, one, coll_name):
        self.db[coll_name].insert_one(one)


# TODO-shougong 使用浏览器引擎来访问
def openurl(keyword, page):
    params = {'q': keyword, 'sort': 'default', 's': str(page * 44)}
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'}
    url = "https://s.taobao.com/search"
    res = requests.get(url, params=params, headers=headers)
    return res


def get_items(res, time, rank):
    try:
        g_page = re.search(r'g_page_config = (.*?);\n', res.text)
        g_page_json = json.loads(g_page.group(1))

        p_items = g_page_json['mods']['itemlist']['data']['auctions']
    except:
        print('Error')
        return None, rank + 44
    result = []
    for each in p_items:
        rank = rank + 1
        dict_items = dict.fromkeys(
            ('mark', 'title', 'raw_title', 'view_price', 'view_sales', 'comment_count', 'view_fee'
             , 'user_id', 'category', 'nid', 'detail_url', 'item_loc', 'nick', 'comment_url', 'shopLink'))
        dict_items['rank'] = rank
        dict_items['mark'] = time
        dict_items['title'] = each['title']
        dict_items['raw_title'] = each['raw_title']
        dict_items['view_price'] = each['view_price']
        dict_items['view_sales'] = each['view_sales']
        dict_items['comment_count'] = each['comment_count']
        dict_items['view_fee'] = each['view_fee']
        dict_items['user_id'] = each['user_id']
        dict_items['category'] = each['category']
        dict_items['nid'] = each['nid']
        dict_items['detail_url'] = each['detail_url']
        dict_items['item_loc'] = each['item_loc']
        dict_items['nick'] = each['nick']
        dict_items['comment_url'] = each['comment_url']
        dict_items['shopLink'] = each['shopLink']

        result.append(dict_items)

    return result, rank


def sale_num(items):
    count = 0
    for each in items:
        if '关键字' in each['raw_title']:  # 关键字处填写书的作者，或者某种商品特有的关键字
            print(each['raw_title'])
            count += int(re.search(r'\d+', each['view_sales']).group())
    return count


def main():
    conn = mongocon(url='mongodb://192.168.20.204:27017/', database='out-data', name=None, pwd=None)
    spidetime = time.strftime('%Y%m%d%H%M%S', time.localtime())
    keyword = "零食"
    page_num = 100
    rank = 0
    for page in range(page_num):
        res = openurl(keyword, page)
        items, rank = get_items(res, spidetime, rank)
        if None == items:
            continue
        conn.insert_many(items, 'TB_ITEM_HOT_LIST')
        print(items.__len__())
        print('now rank=', rank)
        random.random
        time.sleep(5)


if __name__ == "__main__":
    main()
