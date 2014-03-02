**Linux 用户组，用户及文件的访问权限详解**

1. 添加组

		groupadd group_name

2. 查看所有组信息

		cat /etc/group

	> *备注*	

	> 组名: x:groupID:

3. 添加用户

		useradd -g 组名 用户名

4. 查看所有用户信息

		cat /etc/passwd

	> *备注*

	> 用户名:加密信息（密码）:用户ID:用户组ID:注释:用户主目录:shell

5. 设置密码

		pass 用户名

6. 修改用户组

		usermod -g 组名 用户名

7. 将文件改组

		chgrp 组名 文件名

8. 改变文件（夹）所有者

	+ 将该文件夹及其子目录下的所有文件改变所有者
		
			chown -R 用户名 文件夹

	+ 同时改变用户及用户组
			
			chown user_name:group_name file

	+ 也可改变用户组
			
			chown :group_name file



