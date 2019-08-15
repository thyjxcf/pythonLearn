import re
if __name__ == '__main__':
    match = re.search(r'[1-9]\d{5}','BIT  234234')
    if match:
        print(match.group(0))
    print(type(match))
    print(match.string)
    print(match.re)
    print(match.pos)
    print(match.endpos)
    print(match.start())
    print(match.end())
    print(match.span())
    match = re.search(r'PY.*?N','PYANODUJN')
    if match:
        print(match.group(0))