1. 定义

		names = ["zhangsan", "lisi", "wangwu"]
		# 单引号（'），双引号（"）都可以

2. 列表的长度（大小）

		len()
	> 例如：len(names)

3. 访问列表元素

		list[i]，i从0开始
	> 例如，print(name[0])

4. 增加数据
	+ 在列表的末尾增加一个数据项

		
5. 删除元素

	+ 从列表指定位置（index）删除一个元素
	
			pop(index)
		> 例如，names.pop(i)
		> 
		> 注：如果未传参数，则删除最后一个

	+ 查找并删除特定的数据项

			remove(obj)

		> 例如，names.remove('Tom')
		> 
		> 注：如果删除一个不存在的数据，会有异常信息
