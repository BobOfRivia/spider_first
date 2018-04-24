from bs4 import BeautifulSoup
from com.spider.case.util.web_reader import web_reader
import sys
import re
import urllib.request
import os
import socket
from com.spider.case.util.ThreadPool import ThreadPool

#请求 With Retry
def requestWithRetry(url, paramfile, type="gethtml", savepath="", trytime=1):
    import time
    if trytime < 0:
        print("Time is over")
        return "null"
    try:
        time.sleep(2)
        if type == "gethtml":
            return web_reader(paramfile, url).web_req().text
        elif type == "savefile":
            urllib.request.urlretrieve(url, savepath)
    except:
        t, v, tb = sys.exc_info()
        print(t, v)
        print("Timeout=== retry time:" + str(time))
        requestWithRetry(url, paramfile, type=type, savepath=savepath, trytime=trytime - 1)

#读取漫画Pages
def readcharpterPages(href0,thisPath,url1,pool):

    chatperPath = thisPath + "/" + href0.replace("/", "", 1)
    if not os.path.exists(chatperPath):
        os.mkdir(chatperPath)
    else:
        pool.addThread()
        return
    chatperPath = chatperPath + "/%s.jpg"
    url2 = url1 + href0
    html2 = requestWithRetry(url2, "./request-params")
    # html2=web_reader("./request-params", url2).web_req().text
    if (html2 == "404" or html2 == "Not Found"):
        print("ERROR : " + url2)
    else:
        for num in range(0, 9999):
            print(url2 + indexname % num)
            html3 = requestWithRetry(url2 + indexname % num, "./request-params")
            # html3 = web_reader("./request-params", url2+indexname % num).web_req().text
            try:
                picurl = "http://p0.xiaoshidi.net" + "/" + re.findall(r'var mhurl = \"(.*?)\"', str(html3))[0]
            except:
                t, v, tb = sys.exc_info()
                print(t, v)
                break
            print(picurl)
            print(chatperPath % num)
            requestWithRetry(picurl, "./request-params", savepath=str(chatperPath % num), trytime=3, type="savefile")
    pool.addThread()


if __name__ == '__main__':
    threadpool=ThreadPool(4)
    socket.setdefaulttimeout(10)
    homepage = "http://manhua.fzdm.com/"
    indexname = "/index_%s.html"
    path = "D://fzdm-commic"
    filePath = path + "/%s"
    if not os.path.exists(path):
        os.mkdir(path)
    # 首页
    level1 = requestWithRetry("http://manhua.fzdm.com/", "./request-params")
    elements = BeautifulSoup(level1)

    print(elements)

    # 漫画类别列表
    for h in elements.select("li a"):
        commicName = re.findall(r'title=\"(.*?)\"', str(BeautifulSoup(str(h))))
        if commicName.__len__() == 0:
            continue
        commicName = commicName[0]
        print("===" + str(commicName))
        thisPath = filePath % commicName
        if not os.path.exists(thisPath):
            os.mkdir(thisPath)
        else:
            #如果已经创建漫画文件夹，则跳过该漫画
            continue
        url1 = homepage + re.findall(r'href=\"(.*?)\"', str(h))[0]
        html1 = requestWithRetry(url1, "./request-params")
        # html1 = web_reader("./request-params",  url1).web_req().text
        # 遍历章节
        for href0 in re.findall(r'href=\"(.*?)\"', str(html1)):
            if "#" in href0 or "." in href0:
                continue
            else:
                # if "海贼王" in commicName and href0.replace("/","",1).isdigit() and int(href0.replace("/","",1))>580 :
                #     continue
                t=threadpool.getThread()
                a=t(target=readcharpterPages, args=(href0, thisPath, url1,threadpool))
                a.start()
                # readcharpterPages(href0,thisPath,url1)
