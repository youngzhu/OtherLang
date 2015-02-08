0. `'0-9`

	恢复到退出VIM时编辑的文档

	> 可使用 `:marks` 查看详细的标记

0. `:oldfiles`
列出编辑过的历史文档

	> 使用 `{file-comand} #<{number}` 操作对应的文档
{file-comand}，代表所有可操作文档的命令，如 edit , split 等
{number}，列表对应的数字

0. `:browse oldfiles`
`:oldfiles` 的升级版
展示的内容是相同的，
不同的是，该命令输入 `q` 后直接输入数字，即可编辑该文档

0. 
