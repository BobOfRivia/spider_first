from com.spider.case.dxdbbb.web_reader import web_reader
from bs4 import BeautifulSoup
import re

# 第一个参数为线程数量，第二个参数为当前第几个线程
def news_page_iter(c,n):
    print('runing_thread_is_number{}'.format(n))
    # 请求信息
    req_source = '../../source/dxdbbb/new_list_reqhead'
    # url存储 路径
    url_list_source  = '../../source/dxdbbb/new_url_list'
    # 请求路径
    url_path = 'http://www.dxdbbb.com/forum-249-{}.html'

    # < a href = "forum-249-102.html" class ="last"
    page1 = web_reader(req_source,'http://www.dxdbbb.com/forum-249-1.html').dxdbbb_req().text
    soup = BeautifulSoup(page1).select('.last')[0]
    patt = re.compile(r'\d+')
    page_count = int(patt.findall(soup.text)[0])
    # 每个线程处理数量
    per_page_count = int(int(page_count)/c)
    print(per_page_count)
    now_page = per_page_count*(n-1) +1
    end_page = per_page_count * (n)

    while now_page<end_page:
        try:
            # pageurl= 'http://www.dxdbbb.com/forum-249-{}.html'.format(now_page)
            # print(pageurl)
            webreader =  web_reader(req_source, url_path.format(now_page))
            this_list_page =  webreader.dxdbbb_req().text
            sp = str(BeautifulSoup(this_list_page).select('.common em + a'))+str(BeautifulSoup(this_list_page).select('.lock em + a'))

            page_urls = re.findall(r'href=\"(.*?)\"', sp)

            with open(url_list_source,'a') as f:
                for url in page_urls:
                    f.write(url+"\n")

            print(re.findall(r'href=\"(.*?)\"',sp))
            print('over')

            now_page += 1
        except:
            print('Error')
            continue

# def news_list_iter():

def test_one_page():
    req_source = '../../source/dxdbbb/new_list_reqhead'
    pageurl = 'http://www.dxdbbb.com/forum-249-98.html'
    # url存储路径
    url_list_source = '../../source/dxdbbb/new_url_list'
    print(pageurl)
    webreader = web_reader(req_source, pageurl)
    this_list_page = webreader.dxdbbb_req().text
    page  = BeautifulSoup(this_list_page)
    print(page)
    sp = str(page.select('.common em + a'))+str(page.select('.lock em + a'))
    print(sp)
    page_urls = re.findall(r'href=\"(.*?)\"', sp)

    with open(url_list_source, 'a') as f:
        for url in page_urls:
            f.write(url + "\n")

    print(re.findall(r'href=\"(.*?)\"', sp))
    print('over')


# import _thread
import threading

# news_page_iter(1,1)

# n = 3
# i=1
# while i < n:
t1 = threading.Thread(target=news_page_iter,args=(5,1))
t2 = threading.Thread(target=news_page_iter,args=(5,2))
t3 = threading.Thread(target=news_page_iter,args=(5,3))
t4 = threading.Thread(target=news_page_iter,args=(5,4))
t5 = threading.Thread(target=news_page_iter,args=(5,5))
    # i += 1

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

# test_one_page()


