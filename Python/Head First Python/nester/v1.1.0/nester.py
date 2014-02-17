# -*- coding: gbk -*-
""" 递归调用
v1.1.0
加上缩进
"""
# 给参数提供默认值，使其变为可选参数
def print_lol(the_list, level=0):
	for each_item in the_list:
		if isinstance(each_item, list):
			print_lol(each_item)
		else:
			print(each_item)

# TEST 
names = ['John', 'Eric', ['Cleese', 'Idle'], 'Michael', ['Palin']]
'''
version 1.1.0
直接打印出来
'''
print_lol(names)