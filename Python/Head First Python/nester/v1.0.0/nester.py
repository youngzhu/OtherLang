# -*- coding: utf-8 -*-
""" 递归调用
"""
def print_lol(the_list):
	for each_item in the_list:
		if isinstance(each_item, list):
			print_lol(each_item)
		else:
			print(each_item)

# TEST 
names = ['John', 'Eric', ['Cleese', 'Idle'], 'Michael', ['Palin']]
'''
version 1.0.0
直接打印出来
'''
print_lol(names)
