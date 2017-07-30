import requests


def request_json_fmt():
    with open('../../source/request_demo','rt') as f:
        # return "{"+",".join(["\"" + line.split(':')[0].strip() + "\":" + "\"" + line.split(':')[1].strip() + "\"" for line  in f.readlines()])+"}"
        # return ",".join(["\"" + line.split(':')[0].strip() + "\":" + "\"" + line.split(':')[1].strip() + "\"" for line in f.readlines()])
            for line in f.readlines():
                try:
                    # yield "\"" + line.split(': ')[0].strip() + "\":" + "\"" + line.split(': ')[1].strip() + "\""
                    yield line.split(': ')[0],line.split(': ')[1]
                except IndexError:
                    print('==')
                    print(line)
           # yield


def dxdbbb_req():
    entry_url = 'http://www.dxdbbb.com/forum.php'



    # params = eval("{"+','.join(request_json_fmt())+"}")

    params = dict((key,value) for key,value in request_json_fmt())

    params1 = {
        "Host": "www.dxdbbb.com",
        "Connection": "keep-alive",
        "Cache-Control": "max-age=0",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Referer": "http://www.dxdbbb.com/portal.php",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Cookie": "Hm_lvt_a89a192c6cfd9ef05cae2c787a7bcc96=1483544657; boa8_2132_saltkey=bxxo2CTT; boa8_2132_lastvisit=1501314471; boa8_2132_connect_last_report_time=2017-07-29; boa8_2132_visitedfid=249; boa8_2132_forum_lastvisit=D_249_1501319195D_248_1501320075; boa8_2132_ulastactivity=1501324766%7C0; boa8_2132_auth=9b94Bk5Rxr4r2oA8KvM27PTxQSGxFss%2FLcSMr2mQfZrQ13tDaBgvRzDEnsu4vZNxat%2FMTU3JuGszUCR1fv%2B1Rh%2FiCi2T; boa8_2132_lastcheckfeed=1064893%7C1501324766; boa8_2132_lip=58.209.220.206%2C1501324766; flexsns_sky_userinfo=115aq9ivTyC2a1i4ZqL%2Fc0N8nMY6P%2FC6Pa2gC4CJDSOpj7WWTX6bxwRxtpsFHMuJ%2BVUP4cgLFE8KiYQe2xVQsnlNl0nZE4nssuk7f1pFFiPXVRNqmTPpzxTmsQxU; PHPSESSID=b4e36d667d5957029853d972ec0aa6d7; tjpctrl=1501328978531; boa8_2132_reward=e0f0N3BK2TMa30JU%2FsXEb2SoH9SOPOz8cAqrHpxruFp736qSOtU%2FzW9Vg9PRiTiiq5BLxofSp7TnG24; boa8_2132_lastact=1501329477%09home.php%09spacecp; boa8_2132_connect_is_bind=1; boa8_2132_checkpm=1; Hm_lvt_a89a192c6cfd9ef05cae2c787a7bcc96=; Hm_lpvt_a89a192c6cfd9ef05cae2c787a7bcc96=1501327476; boa8_2132_noticeTitle=1"
    }

    print(params)

    print(requests.get(entry_url,params=params).text)


# print(','.join(request_json_fmt()))
#
dxdbbb_req()
