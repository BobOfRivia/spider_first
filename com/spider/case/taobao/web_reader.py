import requests
import fnmatch


class web_reader:
    def __init__(self,req_source,req_url):
        self.req_source = req_source
        self.req_url = req_url

    # 爬取页面信息
    def _request_json_fmt(self):
        with open(self.req_source,'rt') as f:
                for line in f.readlines():
                    if(fnmatch.fnmatchcase(line,'Cookie')):
                        continue
                    try:
                        yield line.split(': ')[0],line.split(': ')[1].replace('\n','')
                    except IndexError:
                        print('==')

    def _request_json_fmt_Cookie(self):
        with open(self.req_source,'rt') as f:
                for line in f.readlines() :
                    if(not fnmatch.fnmatchcase(line,'Cookie*')):
                        continue
                    else :
                        return line.split(': ')[1]

    def _con_cookie(self):
        for cookies in self._request_json_fmt_Cookie().split('; '):
            yield cookies.split('=')[0].strip(),cookies.split('=')[1].strip()

    def web_req(self,timeout=10):

        params1 = dict((key,value) for key,value in self._request_json_fmt())

        return requests.get(self.req_url, headers=params1, cookies=dict(cookies),timeout=timeout)


