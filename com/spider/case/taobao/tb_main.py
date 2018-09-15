import requests
from com.spider.case.util.web_reader import web_reader

if __name__ == '__main__':
    url = "https://mdskip.taobao.com/core/initItemDetail.htm?isUseInventoryCenter=false&cartEnable=true&service3C=false&isApparel=false&isSecKill=false&tmallBuySupport=true&isAreaSell=true&tryBeforeBuy=false&offlineShop=false&itemId=570826281810&showShopProm=true&cachedTimestamp=1529033735141&isPurchaseMallPage=false&isRegionLevel=true&household=false&sellerPreview=false&queryMemberRight=true&addressLevel=3&isForbidBuyItem=false&callback=setMdskip&timestamp=1529038315131&isg=null&isg2=BICAdzTFz2DzNrNJqL02uoY2UQiSoWUer823N_oRaBsudSCfohk0Y1Ykid21RRyr&ref=https%3A%2F%2Fs.taobao.com%2Fsearch%3Fq%3D%25E9%259B%25B6%25E9%25A3%259F%26commend%3Dall%26ssid%3Ds5-e%26search_type%3Ditem%26sourceId%3Dtb.index%26spm%3Da21bo.2017.201856-taobao-item.1%26ie%3Dutf8%26initiative_id%3Dtbindexz_20170306"
    print(web_reader('./initItemDetail',url).web_req().text)
    # url = "https://dsr-rate.tmall.com/list_dsr_info.htm?itemId=539142412767&spuId=686661027&sellerId=1&_ksTS=1527489430051_213&callback=jsonp214"
    # print(web_reader('./listdsrinfo',url).web_req().text)
    #
    # url1 = "https://s.taobao.com/search?q=%E9%9B%B6%E9%A3%9F&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180528&ie=utf8&bcoffset=13&p4ppushleft=1%2C48&ntoffset=13&s=0&sort=renqi-desc"
    # print(web_reader('./itemList', url1).web_req().text)



