0. 创建Session

		:mksession [name].vim

0. 使用Session
	
		:source [name].vim

	> 启动VIM时使用Session
	vim -S [name].vim

0. 最完整的备份/恢复

	> 备份

		:mksession! [session_name].vim
		:wviminfo! [viminfo_name].vim

	> 恢复

		:source [session_name].vim
		:rviminfo! [viminfo_name].vim

0. 
