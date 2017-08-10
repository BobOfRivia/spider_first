import os
class file_utl:
    def __init__(self,*args):
        self.args = args

    def new_dir(self,path):
        try:
            os.mkdir(path)
        except:
            # t, v, tb = sys.exc_info()
            print('文件已存在')

    def file_downer(self,response,filename):
        chunk_size = 1024  # 单次请求最大值
        content_size = int(response.headers['content-length'])  # 内容体总大小
        with open(filename, "wb") as file:
            for data in response.iter_content(chunk_size=chunk_size):
                file.write(data)