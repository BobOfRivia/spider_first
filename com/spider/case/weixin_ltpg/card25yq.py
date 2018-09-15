from com.spider.case.util.web_reader import web_reader
import json

if __name__ == '__main__':
    listjson = web_reader('./req52yq',
                    'https://card.52yq.cn/v4/rest/namecard/199dec78-691f-42b5-b011-8dec26a42db9') \
        .web_req()
    print(listjson)
    list_json = json.loads(listjson)
    print(list_json)



    # 数据结构：
    # code
    # message
    # data
    #     nameCards[
    #        { "id":112324,
    #         "uuid":"f266e825-2273-4e8a-a583-adb90d0e6fe8",
    #         "userId":266335,
    #         "name":"王永凯",
    #         "aliasThis":"王永凯",
    #         "thumbnail":"https://img.52yq.cn/avatar/266335_1501460463370_smallAvatar.jpg",
    #         "company":"住建部-中国建筑文化中心",
    #         "zhiwu":"项目主管",
    #         "phone":null,
    #         "createDate":1501459358000},
    #             ....
    #         ]
    #     nextNameCardDate






