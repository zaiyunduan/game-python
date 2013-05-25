#!/usr/bin/env python
#coding=utf-8
"""
"""
import objects, untils
from actions import add_a_object, parse_comd, states

def objects_in_part1():
	key = untils.create_door_key()
	
	door = objects.Door(key)
	paper = objects.Paper(key, True)

	add_a_object('paper', paper)
	add_a_object('door',door)
	
	return 'paper'

def objects_in_part2():
	"""
	生成第二关的物体
	"""
	key = untils.create_door_key()

	door = objects.Door(key)
	paper = objects.Paper(key,False)
	pole = objects.Pole(True)

	add_a_object('door', door)
	add_a_object('paper', paper)
	add_a_object('pole', pole)

	return 'paper', 'pole'

def objects_in_part3():
	"""
	生成第三关的物体
	"""
	key = untils.create_door_key()

	door = objects.Door(key)
	paper = objects.Paper(key, False)
	handle = objects.Handle(True)
	box = objects.Box(paper,False)

	add_a_object('door', door)
	add_a_object('paper',paper)
	add_a_object('handle',handle)
	add_a_object('box',box)

	return 'paper', 'handle', 'box'

def print_descriptions():
	"""
	打印开始的描述
	"""
	print "你在一个密室中，面前有一扇密码门[door]，可你没有密"
	print "找到密码，逃出密室"
	print "哈哈~~~~~~~~~~"

def print_paper(flag):
	"""
	"""
	if flag == True:	#
		print "有一张纸[paper]在地板上，上边好像写着点东西"
	elif flag == False:	#
		print "天花板上有一张纸[paper]，可够不到"

def print_pole(flag):
	"""
	打印长木干的描述
	"""
	if flag == True:
		print "在地上有一个长木干[pole]"
	else:
		print "地上有个长木干[pole]，好像已经断了"

def print_handle(flag):
	"""
	打印手柄的描述
	"""
	if flag == True:
		print "在一个角落里有一个被丢弃的手柄[handle]"
	else:
		print "那边角落本有一个手柄[handle]，怎么找不了!"

def print_box(flag):
	"""
	打印柜子的描述
	"""
	if flag == True:
		print "有一个柜子[box]，门很容易就能打开"
	else:
		print "柜子[box]的门有点问题，打不开啦。。。"

if __name__ == "__main__":

	print_descriptions()
	
	objects_in_part3()

	print_handle(True)
	print_box(False)

	print "做你该做的事吧"
	while True:
		comd = raw_input('> ')
		r = parse_comd(comd)
		states[r]()
