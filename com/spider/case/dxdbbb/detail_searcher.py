import threading
from com.spider.case.dxdbbb.web_reader import web_reader
from bs4 import BeautifulSoup
import time
import re
import sys
rlock = threading.RLock()


def long_to_time(timestamp):
    timeLoc = time.localtime(int(timestamp))
    timefmt = time.strftime("%Y-%m-%d %H:%M:%S", timeLoc)
    return timefmt


def detail_seacher(n):
    url_paths = '../../source/dxdbbb/new_url_list'
    i =0;
    with open(url_paths,'rt') as f:
        for line in f.readlines():
            # print('123123')
            # t1 = threading.Thread(target=detail_catcher, args=(i, n,f))
            # t1.start()
            yield detail_catcher(i,n,line)


def detail_catcher(i,n,line):
    comm_url = "http://www.dxdbbb.com/"
    req_source = '../../source/dxdbbb/new_detail_reqhead'
    if (i >= n):
        time.sleep(5)
    i += 1
    # 锁定共享资源
    rlock.acquire()
    url = comm_url + str(line)
    # while True:
    #     c = 0;
    #     if(c>3):
    #         break
    #     try:
    html = web_reader(req_source, url).dxdbbb_req()
        #     break
        # except:
        #     c += 1
        #     print('超时')
        #     continue

    print(url)
    # print(web_reader(req_source, url).dxdbbb_req())
    # 释放共享资源
    rlock.acquire()
    i -= 1
    return BeautifulSoup(html)


def detail_grep(n):
    print('====')
    # print(detail_seacher(n))
    for html in detail_seacher(n):
        try:
            name = html.select('.postlisttop h1 span a')[0].text
            address = "@@@".join(re.findall(r'href=\"(.*?)\"',str(html.select('ignore_js_op span a'))))
            # print(torn_add)
            spans =  html.select('font')
            index = 0
            # print(name)
            # print(address)
            password = ''
            value= []
            # 捞取密码1
            for span in spans :
                # print(password)
                if re.match(r'[\s\S]*密码[\s\S]*?|[\s\S]*密碼[\s\S]*?',str(span)):
                    # print(spans[index])
                    password =str(spans[index-1:index+1])
                    break
                index+=1

            # 捞取密码2
            # print(password.__len__())
            if password.__len__() == 0 :
                if re.match(r'[\s\S]*www.mzxzx.com[\s\S]*?', str(html)):
                    password = 'www.mzxzx.com'

            # 捞取密码3
            if password.__len__() == 0:
                password = str(html)

            timestamp = re.findall(r'value=\"(.*?)\"', str(html.select('#posttime')))[0]

            time = long_to_time(timestamp)
            value.append(time)
            value.append(name)
            value.append(address)
            value.append(password)
            yield value
        except:
            t, v, tb = sys.exc_info()
            print(t, v)
            continue

def test_one_url():
        req_source = '../../source/dxdbbb/new_detail_reqhead'
        url = 'http://www.dxdbbb.com/thread-358800-1-69.html'
        html = BeautifulSoup(web_reader(req_source, url).dxdbbb_req())
        spans = html.select('font')
        index = 0
        # print(str(spans))
        for password in spans:
            # print(password)
            if re.match(r'[\s\S]*密码[\s\S]*?|[\s\S]*密碼[\s\S]*?', str(password)):
                # print(index)
                # print(spans[index])
                password = spans[index - 1:index + 1]
                print(password)
                # print(re.findall(r'href=\"(.*?)\"',password))
                print(','.join(re.findall(r'href=\"(.*?)\"',str(password))))
                break
            index += 1


if __name__ == '__main__':
    # test_one_url()
    # d = dict([(arr[0],arr[1:]) for arr in detail_grep(4)])
       # print(zip(name, address, password))
    for arr in detail_grep(4):
        print(arr[0])
        print(arr[1])
        print(arr[2])
        print(arr[3])

# print('---')