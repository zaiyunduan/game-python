#!/usr/bin/env python
#coding=utf-8
"""
描述游戏者的几个动作
"""
from sys import exit

objs = {}

def add_a_object(name, obj):
	"""
	增加一个物体,存储在 obj_list 中
	"""
	if name not in objs:
		objs[name] = obj

def is_exited(name):
	"""
	判断一个物体是否存在
	"""
	return name in objs

def usage_help():
	"""
	命令格式
	"""
	print "只支持 5 个命令"
	print "[1] 查看: exam <object>"
	print "[2] 组合: comb <object1> <object2>"
	print "[3] 使用: use <object1> <object2> 对<object2>使用<object1>"
	print "[4] 帮助: help"
	print "[5] 退出: exit"
	return 'none'

def exam(name):
	"""
	查看一个物体
	"""
	if name == 'door':
		return objs[name].examine()
	elif name in objs:
		objs[name].examine()
		return 'none'
	else:
		return 'no_obj'

def comb(name1, name2):
	"""
	组合两个物体
	"""
	if name1 in objs and name2 in objs:
		objs[name1].make_tool(objs[name2])
		return 'none'
	else:
		return 'no_obj'

def use(name1, name2):
	"""
	使用一个物体
	"""
	if name1 in objs and name2 in objs:
		objs[name1].use_tool(objs[name2])
		return 'none'
	else:
		return 'no_obj'

def none():
	"""
	"""
	print "请输入指令"
	
def no_obj():
	"""
	"""
	print "没有这个物体,请重新输入指令"

states = {'no_obj': no_obj,'none': none}
	
def parse_comd(comd):
	"""
	语法分析命令
	"""
	comd = comd.split()
	c = comd[0]
	l = len(comd) - 1

	if c == 'exam' and l == 1:
		name = comd[1]
		return exam(name)
	elif c == 'comb' and l == 2:
		return comb(comd[1], comd[2])
	elif c == 'use' and l == 2:
		return use(comd[1], comd[2])
	elif c == 'help':
		return usage_help()
	elif c == 'exit':
		print "就这样不玩了！"
		exit(0)
	else:
		print "命令错误，如需帮助，请输入help"
		return 'none'

if __name__ == '__main__':

	import objects
	paper = objects.Paper()
	pole = objects.Pole(True)
	add_a_object('pole',pole)
	add_a_object('paper',paper)

	print objs

	while True:
		comd = raw_input('> ')
		r = parse_comd(comd)
		states[r]()
