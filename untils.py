#!/usr/bin/env python
#coding=utf-8
"""
共用且基本的函数
"""

from sys import exit
from random import randint

def create_door_key():
	"""
	随机生成门的四位密码
	"""
	return randint(1000,9999)


def object_name(s):
    """
    去掉 __doc__ 中，刚开始的 '\n' 和 两端的空格 
    """
    s = s.lstrip('\n')
    return s.strip()
    
    
    

if __name__  ==  "__main__":
    print "%r" % object_name("\n    中国欢迎你    ")
