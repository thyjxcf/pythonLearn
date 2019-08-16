import re

def gen(n):
    for i in range(n):
        yield i**2

if __name__ == '__main__':
    for i in gen(5):
        print(i,"  ",end="")
