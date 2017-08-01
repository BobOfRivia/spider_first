import requests
import fnmatch

class web_reader:
    def __init__(self,req_source,req_url):
        self.req_source = req_source
        self.req_url = req_url

    # 爬取页面信息
    def request_json_fmt(self):
        with open(self.req_source,'rt') as f:
            # return "{"+",".join(["\"" + line.split(':')[0].strip() + "\":" + "\"" + line.split(':')[1].strip() + "\"" for line  in f.readlines()])+"}"
            # return ",".join(["\"" + line.split(':')[0].strip() + "\":" + "\"" + line.split(':')[1].strip() + "\"" for line in f.readlines()])
                for line in f.readlines() :
                    if(fnmatch.fnmatchcase(line,'Cookie')):
                        continue
                    try:
                        # yield "\"" + line.split(': ')[0].strip() + "\":" + "\"" + line.split(': ')[1].strip() + "\""
                        yield line.split(': ')[0],line.split(': ')[1]
                    except IndexError:
                        print('==')
                        # print(line)
               # yield

    def request_json_fmt_Cookie(self):
        with open(self.req_source,'rt') as f:
            # return "{"+",".join(["\"" + line.split(':')[0].strip() + "\":" + "\"" + line.split(':')[1].strip() + "\"" for line  in f.readlines()])+"}"
            # return ",".join(["\"" + line.split(':')[0].strip() + "\":" + "\"" + line.split(':')[1].strip() + "\"" for line in f.readlines()])
                for line in f.readlines() :
                    if(not fnmatch.fnmatchcase(line,'Cookie*')):
                        continue
                    else :
                        return line.split(': ')[1]
               # yield

    def con_cookie(self):
        for cookies in self.request_json_fmt_Cookie().split('; '):
            yield cookies.split('=')[0].strip(),cookies.split('=')[1].strip()

    def dxdbbb_req(self):
        # params = eval("{"+','.join(request_json_fmt())+"}")

        params = dict((key,value) for key,value in self.request_json_fmt())

        cookies =  params = dict((key,value) for key,value in self.con_cookie())

        # print(cookies)
        html = requests.get(self.req_url, headers=params, cookies=dict(cookies),timeout=5).text
        # print(html)
        return html
# print(','.join(request_json_fmt()))
#

# if __name__ == '__main__':
#     req_source = '../../source/dxdbbb/new_list_reqhead'
#     url_path = 'http://www.dxdbbb.com/forum-249-10000.html'
#     dxdbbb_req(url_path,req_source)