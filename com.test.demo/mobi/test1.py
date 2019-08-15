import re

if __name__ == '__main__':
    match = re.search(r'[1-9]\d{5}','BIT  234234')
    if match:
        print(match.group(0))

    match = re.match(r'[1-9]\d{5}','BIT  234234')
    # 一定要加if match: 语句 判断是否为空  不能用 空的match 去调用 match.group(0)
    if match:
        print(match.group(0))
    match = re.match(r'[1-9]\d{5}','234312  BIT')
    if match:
        print(match.group(0))

    ls = re.findall(r'[1-9]\d{5}','234312 234231 32523 BIT')
    print(ls)

    sp = re.split(r'[1-9]\d{5}','ddd 234312 serfe 234231 sfe 32523 BIT' ,maxsplit=1)
    print(sp)
    for m in re.finditer(r'[1-9]\d{5}','ddd 234312 serfe 234231 sfe 32523 BIT'):
        if m:
            print(m.group(0))

    sub = re.sub(r'[1-9]\d{5}','zzz','ddd 234312 serfe 234231 sfe 32523 BIT' )
    print(sub)