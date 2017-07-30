from bs4 import BeautifulSoup
with open('../source/1spider.txt','rt') as f :
    t = f.read()

soup = BeautifulSoup(t)

# with open('../source/1bs4.html','wt') as f:
#     f.write(str(soup.contents))
#     f.write(soup.text)
print(soup.select('a')[1])
# print(soup.contents)

alinks = soup.select('a')
for alink in alinks:
    try:
        print(alink['style'])
    except KeyError:
        print('KeyError')
