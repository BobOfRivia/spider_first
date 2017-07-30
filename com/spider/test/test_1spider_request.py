import requests

res = requests.get('http://blog.csdn.net/u013366098/article/details/50477280')
res.encoding('utf-8')
print(res.headers)

with open('../source/1spider.txt','wt') as f:
    f.write(str(res.headers))

with open('../source/1spider.txt','at') as f:
    f.write(res.encoding)

with open('../source/1spider.txt','at') as f:
    f.write(res.text)
# print(res.text,'../source/1spider.txt')