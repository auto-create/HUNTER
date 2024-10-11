#coding=utf-8
import os, sys, platform
 
os.system('rm -rf test.so')
 
try:
    if sys.argv[1]=='update':
        os.system('rm -rf test.so')
except:
    pass
 
 
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('test.so'):
        os.system('curl -L https://github.com/auto-create/test/blob/main/test.py') 
        import test
    else:
        import test
 
elif bit == '32bit':
    exit()
 