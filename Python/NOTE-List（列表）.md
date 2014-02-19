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
	
			append(obj)
		>例如，names.append('xiaoming')

	+ 在指定的位置增加一个数据项
	
			insert(i, obj)
		> 例如，names.insert(0, 'xiaohong')
		> 
		> 注：如果，i大于列表的长度，相当于调用append()方法，即在列表的末尾增加一个数据项

	+ 在列表的末尾增加一个数据项集合

			extend()

		> 例如，names.extend(['Lily','Tom'])
		> 
		> **当然，也可以叠加自身**
		>
		> 例如，names.extend(names)


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