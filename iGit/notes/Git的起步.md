配置
===

配置用户信息
---

	git config --global user.name "Young Mac"
	git config --global user.email young.mac@mac.vm.com


下载
===
	git clone [url]

设置 SSH 公钥
===

首先查看用户目录下是否有 **.ssh** 目录。  
如果有，就查看是否有这两个文件 **xxx** 和 **xxx.pub** 。  
如果这两个文件已经存在，就说明已经有 SSH公钥了  

如果没有，则需要生成 SSH公钥。

生成 SSH公钥
---

使用如下命令生成：

	ssh-keygen

将SSH公钥与git库关联
---

将 xxx.pub 的内容复制到git库相关的地方

