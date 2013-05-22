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


