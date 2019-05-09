import os
import time
import random


def main():
    content = '北京欢迎你为你开天辟地…………'
    while True:
        # 清理屏幕上的输出
        os.system('cls')  # os.system('clear')
        print(content)
        # 休眠200毫秒
        time.sleep(0.2)
        content = content[1:]+content[0]

def foo(codelen):
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos  = len(all_chars)-1
    code = ''
    for _ in range(codelen):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return code


def main():
    persens = [True] * 30
    sel = 0 
    while(sel < 15):
        index

if __name__ == '__main__':
    main()
