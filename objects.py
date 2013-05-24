#!/usr/bin/env python
#coding=utf-8
"""
描述了在游戏中可能遇到或使用的几个物体
"""
from untils import object_name as name

class Tool(object): pass

class Door(object):
	"""
	密码门
	"""
	def __init__(self, key):
		self.key = key
	
	def open(self, key):
		if key == self.key:
			print "输入密码正确"
			print "成功从密室中逃脱"
			return 'key_right'
		else:
			print "输入密码错误"
			return "none"
	def make_tool(self, tool):
		print "密码门不能和%s组合" % name(tool.__doc__)

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
			print "纸上写着数字%d，已经很模糊了" % self.value
        
    def make_tool(self, tool):
        tool = name(tool.__doc__)
        n = name(self.__doc__)
        print "%s 和 %s 不能组合" % (n, tool)
        return 'no_make'  
        
    def use_tool(self, obj):
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
        if self.flag == False:
            print "由于一些原因，你还不能使用这个长木干"
        else:
            print "%s 和 %s 不能组合" % (name(self.__doc__), name(tool.__doc__))
    
    def use_tool(self, obj):
        if self.flag == True:
            if obj == None:
                print "长木干用来做什么？"
            else:
                obj.flag = True
                print "你拿到了%s" % name(obj.__doc__)    
        else:
            print  "由于一些原因，你还不能使用这个长木干"
            
class Handle(Tool):
    """
    手柄
    """
    def __init__(self, flag = False):
        self.newtool = 'box'
        self.flag = flag 
    
    def examine(self):
        if self.flag == False:
            print "由于一些原因，你还不能使用这个手柄"  
        else:
            print "看起来像是箱子的一部分"
    
    def make_tool(self, tool):
        if self.flag == True and self.newtool == tool.newtool:
            print "%s 和 没有手柄的%s 组成成了 %s" %                          \
                        (name(self.__doc__), name(tool.__doc__), name(tool.__doc__))
            tool.flag = True
        else:
            print "%s 和 %s 不能组合" % (name(self.__doc__), name(tool.__doc__))  
            
    def use_tool(self, obj):
        print "不能是用手柄"
 
class Box(Tool):
    """
    柜子
    """
    def __init__(self, value = None, flag = False):
        self.newtool = 'box'
        self.flag = flag
        self.value = value
        
    def examine(self):
        if self.flag == False:
            print "柜子好像少了手柄，打不开"
        elif self.value == None:
            print "柜子里什么也没有"
        else:
            self.value.flag = True
            print "柜子里发现了一个%s" % name(self.value.__doc__)
            
    def make_tool(self, tool):
        if self.flag == False and self.newtool == tool.newtool:
            print "%s 和 没有手柄的%s 组成成了 %s" %                          \
                        (name(tool.__doc__), name(self.__doc__), name(self.__doc__))
            self.flag = True
        else:
            print "%s 和 %s 不能组合" % (name(self.__doc__), name(tool.__doc__))  
            
    def use_tool(self, obj):
        print "实在是想不出柜子能怎么用"
                
if __name__ == '__main__':
	door = Door(1234)

	print door.open(3456)

	print door.open(1234)
	
	paper = Paper()
	pole = Pole(True)
	
	paper.examine()
	paper.make_tool(pole)
	paper.use_tool()
	
	print "after use pole"
	pole.examine()
#	pole.use_tool(paper)
	paper.examine()
	
	print "handle and box"
	handle = Handle(True)
	handle.examine()
	
	box = Box(paper, False)
#	handle.make_tool(box)
	box.make_tool(handle)
	box.examine()
	paper.examine()
