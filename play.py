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
	
	return 'paper'


def print_descriptions():
	"""
	打印开始的描述
	"""
	print "你在一个密室中，面前有一扇密码门，可你没有密"
	print "找到密码，逃出密室"
	print "哈哈~~~~~~~~~~"

def print_paper(flag):
	"""
	"""
	if flag == 1:	#
		print "有一张纸在地板上，上边好像写着点东西"
	elif flag == 2:	#
		print "天花板上有一张纸，可够不到"


if __name__ == "__main__":

	print_descriptions()
	
	objects_in_part1()
	print_paper(1)

	print "做你该做的事吧"
	while True:
		comd = raw_input('> ')
		r = parse_comd(comd)
		states[r]()
