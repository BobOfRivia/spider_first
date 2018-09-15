from com.spider.case.util.web_reader import web_reader
import json
import time

if __name__ == '__main__':

    psz = range(0,1000)

    for i in psz:
        with open('/Users/guhongjie/tmp/list-data-1.txt', 'a') as f:
            resp = web_reader('./request',
                   'https://73270.ixiaochengxu.cc/index.php/addon/DuoguanBcard/Api/top.html?type=click'
                   '&pagesize='+str(i)+'&'
                                           'pagenum=10&'
                                           'utoken=13071a10981aef43ec32fdb1ed48d1b7&'
                                           'token=gh_c3dcc1a82e2b').web_req().text
            print(len(resp))
            if(len(resp) == 0):
                break
            time.sleep(2)
            f.write(resp)
            f.write('\r\n')



