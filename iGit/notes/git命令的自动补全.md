##下载 Git 的源代码##

使用如下命令即可下载：

	git clone https://github.com/git/git

##复制 git-completion.bash##

源代码下有个 **contrib/completion** 目录，有个 **git-completion.bash** 文件

	cd git/contrib/completion/

将该文件复制到主目录(~)下

注意：复制时，文件名前加一个"点"（.），命令如下：

	cp git-completion.bash ~/.git-completion.bash

##修改主目录下的 .bashrc 文件##

	vi ~/.bashrc

在文件的最后一行，加上如下代码：

	source ~/.git-completion.bash

OK，现在可以试一下，在输入 不完整的 git 命令后，再输入两个制表符（Tab）,就会看到与之匹配的相关命令，如输入如下代码：

	git co<tab><tab>

就会得到如下提示

	commit config

如果输入的命令，唯一匹配，键入一个制表符，就会自动补全，例如输入:

	git com<tab>

就会得到

	git commit 


> PS.如果不起作用，就把终端（Terminal）关了，重新打开一个
