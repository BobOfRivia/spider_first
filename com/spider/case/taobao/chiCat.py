from com.spider.case.util.web_reader import web_reader
if __name__ == '__main__':
    # url = "https://list.taobao.com/itemlist/huichi2014.htm?_input_charset=utf-8&json=on&cat=&user_type=0&at=45634&viewIndex=1&as=0&atype=b&style=grid&same_info=1&isnew=2&tid=0&pSize=95&data-key=cat&data-value=50008055&data-action&module=cat&_ksTS=1527647731570_215&callback=jsonp216"
    # print(web_reader('./chicatagory',url).web_req().text)

    # url = "https://detail.tmall.com/item.htm?id=558100724511&ali_refid=a3_430583_1006:1103173608:N:%E9%9B%B6%E9%A3%9F:a3abb6105330d376451239d5d0e78e11&ali_trackid=1_a3abb6105330d376451239d5d0e78e11&spm=a230r.1.14.1";
    # url = "https://item.taobao.com/item.htm?spm=a230r.1.14.66.4c867c75afPp4d&id=556177923828&ns=1&abbucket=6#detail";
    url = "item.taobao.com/item.htm?id=528331923371&amp;ns=1&amp;abbucket=0#detail"
    print(web_reader('./itemDetail',url).web_req().text)
