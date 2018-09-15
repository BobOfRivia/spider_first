import re
if __name__ == '__main__':
    dicts = dict();
    with open('/Users/guhongjie/data/branchReport.biz','r') as f :
        for line in f.readlines() :
            # print(line)
            line = line.strip()
            word = re.findall(r'.*refId=\"(.*?)\".*', line)
            if word.__len__()!=0:
                # print(word[0],line)
                # print(re.findall(r'.*refId=\"(.*?)\".*', line))
                dicts[word[0]] = line

    for d in dicts:
        with open('/Users/guhongjie/data/branchReport.reduce','a') as f:
            f.write(dicts[d]+"\n")
