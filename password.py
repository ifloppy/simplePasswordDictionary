import os
import argparse
import itertools
import string
f=open("a.txt", "tw")#密码默认写入一个名为a.txt的文本文件，可以修改为其它的相对路径或绝对路径
print("Wait...")
'''iruanp.com
下面部分代码有借鉴 https://www.smslit.top/2018/10/21/unzip-dict-hacker/ 并进行了一些优化，降低了内存的占用
没有使用多线程，效率较低'''
def getkeyslist(minlength, maxlength, choices):
    for i in range(minlength, maxlength + 1):
        keyiter = itertools.product(choices, repeat=i)
        for c in keyiter:
            keys=''.join(c)+'\n'
            f.write(keys)

klist=getkeyslist(4, 32, '''0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*()_+/*-=[]{};'\:"|,./<>?''')
'''参数1:最短密码长度；参数2:最长密码长度；参数3:用作生成密码的字符'''
