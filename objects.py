#!/usr/bin/env python
#coding=utf-8
"""
描述了在游戏中可能遇到或使用的几个物体
"""
from sys import exit

class Tool(object): pass

class Door(object):
	def __init__(self, key):
		self.key = key
	
	def open(self, key):
		if key == self.key:
			print "输入密码正确"
			print "成功从密室中逃脱"
			exit(0)
		else:
			print "输入密码错误"
			return "keyerror"

if __name__ == '__main__':
	door = Door(1234)

	r = door.open(3456)
	print r

	door.open(1234)
