import threading
from com.spider.case.dxdbbb.web_reader import web_reader
from com.spider.util.file_utl import file_utl

from bs4 import BeautifulSoup
import time
import re
import sys
import random
rlock = threading.RLock()


def long_to_time(timestamp):
    timefmt = timestamp.replace('-','').replace(' ','').replace(':','')
    # timeLoc = time.localtime(int(timestamp))
    # timefmt = time.strftime("%Y%m%d%H%M%S", timeLoc)
    return timefmt


def detail_seacher(data):
    # url_paths = '../../source/dxdbbb/new_url_list'
    # i =0;
    # read_rows = int(data.__len__()/n)+1
    # lines = data[:read_rows]
    # with open(url_paths,'rt') as f:
        # rlock.acquire()
        # lines = data[:read_rows]
        # f.writelines(data[read_rows:])
        # rlock.release()
    for line in data:
        yield detail_catcher(line)

def detail_catcher(line):
    comm_url = "http://www.dxdbbb.com/"
    req_source = '../../source/dxdbbb/new_detail_reqhead'
    # 锁定共享资源
    # rlock.acquire()
    url = comm_url + str(line)
    i =0
    print(url)
    while True:
        time.sleep(1)
        i+=1
        try:
            html = web_reader(req_source, url).dxdbbb_req().text
            return BeautifulSoup(html),url
        except:
            t, v, tb = sys.exc_info()
            print(t, v)
            if(i>4):
                break
            continue

    # 释放共享资源
    # rlock.acquire()
    # return BeautifulSoup(html),url


def detail_grep(data):

    # print(detail_seacher(n))

    for html,url in detail_seacher(data):
        try:
            html_name = html.select('.postlisttop h1 span a')
            if(html_name.__len__() != 0):
                name = html_name[0].text
            else:
                name = ''
            address = "@@@".join(re.findall(r'href=\"(.*?)\"',str(html.select('ignore_js_op span a'))))
            # print(torn_add)
            spans =  html.select('font')
            index = 0
            # print(name)
            # print(address)
            password = ''
            value= []

            # 捞取密码2
            # print(password.__len__())
            if password.__len__() == 0 :
                if re.match(r'[\s\S]*www.mzxzx.com[\s\S]*?', str(html)):
                    password = 'www.mzxzx.com'

            # 捞取密码3
            if password.__len__() == 0:
                html_password = re.findall(r':(.*@oko.co?)', str(html))
                if (html_password.__len__() != 0):
                    password = html_password[0]
                else:
                    password = ''
                # password = re.findall(r':(.*@oko.co?)',str(html))[0]

            # 捞取密码1
            if password.__len__() == 0:
                for span in spans :
                    # print(password)
                    if re.match(r'[\s\S]*密码[\s\S]*?|[\s\S]*密碼[\s\S]*?',str(span)):
                        # print(spans[index])
                        password =str(spans[index-2:index+2])
                        break
                    index+=1
            # timestamp = re.findall(r'value=\"(.*?)\"', str(html.select('em[id^=authorposton]')[0].text))[0]
            timestamp = str(html.select('em[id^=authorposton]')[0].text)
            time = long_to_time(timestamp)+str(random.randint(10,99))
            # password = password.replace('\'', '').encode('utf-8')
            # password =re.findall(r'b\'(.*?)\'', str(password))[0]
            value.append(time)
            value.append(name)
            value.append(address+"@@@")
            value.append(password.replace('\'', ''))
            value.append(url)
            yield value
        except:
            t, v, tb = sys.exc_info()
            print(t, v)
            continue

def test_one_url():
        req_source = '../../source/dxdbbb/new_detail_reqhead'
        url = 'http://www.dxdbbb.com/thread-358800-1-69.html'
        html = BeautifulSoup(web_reader(req_source, url).dxdbbb_req().text)
        spans = html.select('font')
        index = 0
        # print(str(spans))
        for password in spans:
            # print(password)
            if re.match(r'[\s\S]*密码[\s\S]*?|[\s\S]*密碼[\s\S]*?', str(password)):
                # print(index)
                # print(spans[index])
                password = spans[index - 2:index + 2]
                print(password)
                # print(re.findall(r'href=\"(.*?)\"',password))
                print(','.join(re.findall(r'href=\"(.*?)\"',str(password))))
                break
            index += 1

def data_save_db(c:int,n:int) ->int:
    from com.spider.database.mysqlcon import mysql_bean
    mysql_bean = mysql_bean(1)
    mysql_bean.open_db()
    sql = 'insert into animation_source values (\'{}\',\'{}\',\'{}\',\'{}\',\'{}\')'
    url_paths = '../../source/dxdbbb/new_url_list'
    data = open(url_paths, 'rt').readlines()

    read_rows = int(data.__len__() / c) + 1
    start =read_rows*(n-1)
    end = read_rows * (n)-1
    lines = data[start:end]
    for arr in detail_grep(lines):
        try:
            mysql_bean.sql_act(sql.format(arr[0], arr[1], arr[2], arr[3], arr[4]))
        except:
            t, v, tb = sys.exc_info()
            print(t, v)
            continue
    mysql_bean.close_db()

import os
def data_save_localfile(n:int,c:int):
    req_source = '../../source/dxdbbb/tor_downer_req'
    comm_url = 'http://www.dxdbbb.com/'
    url_paths = '../../source/dxdbbb/new_url_list'
    data = open(url_paths, 'rt').readlines()
    file = file_utl()
    root = 'G:\py-space\spider_first\com\spider\source\dxdbbb\\torrents1'
    file.new_dir(root)
    read_rows = int(data.__len__() / c) + 1
    start = read_rows * (n - 1)
    end = read_rows * (n) -1
    lines = data[start:end]
    for arr in detail_grep(lines):
        # 新建本地目录
        mod = re.compile(r'\【.*\】|\[.*\]')
        name = mod.sub('', arr[1])
        name = name if name else arr[1]
        tor_root_base = root + '\\{}'.format(name.replace('/','-').replace('\\','-').replace(' ','').replace('...',''))
        file.new_dir(tor_root_base)
        # 下载种子
        tor_count = 0;
        tor_root =  tor_root_base+"\种子列表"
        print(tor_root)
        file.new_dir(tor_root)
        for tor_arr in  arr[2].split('@@@') :
            try:
                if(tor_arr == ''):
                    continue
                tor_count += 1
                print(comm_url+tor_arr)
                tor_url = 'http://www.dxdbbb.com/forum.php?mod=attachment&aid=NjU0Mzg4fDhiM2FlZDM0fDE1MDIzMzM1NjN8MTA2NDg5M3w0NDgyMjU%3D'
                print(tor_url)
                torb = web_reader(req_source,(comm_url+tor_arr).replace('&amp;','&')).dxdbbb_req()
                file.file_downer(torb,tor_root + '\\{}.zip'.format('种子'+str(tor_count)))
            except:
                t, v, tb = sys.exc_info()
                print(t, v)
                continue
        # 说明文件
        with open(tor_root_base+'\pass.txt','wt') as f:
            try:
                f.write(arr[3])
            except:
                print("wt-error ==>")
                print(arr[3])

def test_down_tor():
    req_source = '../../source/dxdbbb/tor_downer_req'
    tor_url = 'http://www.dxdbbb.com/forum.php?mod=attachment&aid=NjU0Mzg4fDhiM2FlZDM0fDE1MDIzMzM1NjN8MTA2NDg5M3w0NDgyMjU%3D'
    torb = web_reader(req_source,tor_url).dxdbbb_req()
    file = file_utl()
    file.file_downer(torb, "d:/test.tor")

# 数据库
if __name__ == '__main1__':
    t1 = threading.Thread(target=data_save_db,args=(1,1))
    # t2 = threading.Thread(target=data_save_db,args=(3,2))
    # t3 = threading.Thread(target=data_save_db,args=(3,3))

    t1.start()
    # t2.start()
    # t3.start()

# 本地文件存储
if __name__ == '__main__':
    t1 = threading.Thread(target=data_save_localfile, args=(3, 1))
    t2 = threading.Thread(target=data_save_localfile, args=(3, 2))
    t3 = threading.Thread(target=data_save_localfile, args=(3, 3))

    t1.start()
    t2.start()
    t3.start()
# root= 'G:\py-space\spider_first\com\spider\source\dxdbbb\\torrents1\もんむす_くえすと！＃1「外伝_サキュバス'
# os.mkdir(root)
# path = root +'种子列表'
# os.mkdir(path)

# test_down_tor()
path = 'G:\\py-space\\spider_first\\com\\spider\\source\\dxdbbb\\torrents1\\:姬辱触手龙恶魔Vol.1-3\\pass.txt'