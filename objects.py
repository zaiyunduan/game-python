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
			return 'key_right'
		else:
			print "输入密码错误"
			return "key_error"

class Paper(Tool):
    """
    纸
    """
    def __init__(self,  value = 1111, flag = False):
        self.value = value
        self.newtool = None
        self.flag = flag               #默认物体不能被使用
        
    def examine(self):
        if self.flag == False:
            print "由于一些原因，你还不能使用这张纸"
        else:
            print self.value
        
    def make_tool(self, tool):
        tool = tool.__doc__
        print "%s 和 %s 不能组合" % (self.__doc__, tool)
        return 'no_make'  
        
    def use_tool(self):
        print "你不能以任何方式使用纸张"
        return 'no_use'
        
class Pole(Tool):
    """
    长木干
    """
    def __init__(self, flag = False):
        self.newtool = None
        self.flag = flag
        
    def examine(self):
        if self.flag == False:
            print "由于一些原因，你还不能使用这个长木干"
        else:
            print "长木干，可以用来够到高处的东西"
    
    def make_tool(self, tool):
        print "%s 和 %s 不能组合" % (self.__doc__, tool.__doc__)
    
    def use_tool(self, obj):
        if obj == None:
            print "长木干用来做什么？"
        else:
            obj.flag = True
            print "你拿到了%s" % obj.__doc__    
           
if __name__ == '__main__':
	door = Door(1234)

	print door.open(3456)

	print door.open(1234)
	
	paper = Paper()
	pole = Pole(True)
	
	print "paper is %r" % paper.__doc__
	paper.examine()
	paper.make_tool(pole)
	paper.use_tool()
	
	print "after use pole"
	pole.examine()
	pole.use_tool(paper)
	paper.examine()
