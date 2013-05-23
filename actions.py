#!/usr/bin/env python
#coding=utf-8
"""
描述游戏者的几个动作
"""

obj = {}

def add_a_object(name, obj):
	"""
	增加一个物体,存储在 obj_list 中
	"""
	if name not in obj:
		obj[name] = obj

def is_exited(name):
	"""
	判断一个物体是否存在
	"""
	return name in obj

def usge_help():
	"""
	命令格式
	"""
	print "只支持 4 个命令"
	print "[1] 查看: exam <object>"
	print "[2] 组合: comb <object1> <object2>"
	print "[3] 使用: use <object>"
	print "[4] 帮助: help"

def exam(name):
	"""
	查看一个物体
	"""
	if name in obj:
		obj[name].examine()
		return 'none'
	else:
		return 'no_obj'

def comb(name1, name2):
	"""
	"""
	if name1 in obj and name2 in obj:
		obj[name1].make_tool(obj[name2])
		return 'none'
	else:
		return 'no_obj'

def use(name):
	"""
	"""
	if name in obj:
		obj[name].use_tool()
		return 'none'
	else:
		return 'no_obj'

def none():
	"""
	"""

states = {'no_obj': no_obj,'none': none}
	
def parse_comd(comd):
	"""
	语法分析命令
	"""
	comd = comd.split()

	

if __name__ == '__main__':
	
	add_a_object('car')
	add_a_object('door')
	add_a_object('pole')

	print obj_list

	print is_exited('car')
	print is_exited('bus')

	comd = raw_input('> ')
	parse_comd(comd)
