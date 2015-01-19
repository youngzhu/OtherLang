> `v`, vertical ，左右分屏


上下分屏
------
使用 `:(v)split` 对同一个文件分屏。
> 好处：
如果文本过大，可以同时查看文件的不同部分。

或，使用 `:split filename`

跳转
----
使用 `CTRL-W` 在各屏之间跳转
也可以使用 `CTRL-W h/j/k/l/t(Top)/b(Buttom)`

-----
`:close`
使用 `:q` 或者 `Shift - ZZ` 也可以关闭窗口。
不同的是，`:close` 不能关闭最后一个窗口，即不能退出VIM。

关闭其他窗口
----
`:only`

新建一个空白文档
----
`:(v)new`

调整窗口大小
----
`[height] CTRL-W +/-/_`

`_` 和 `+/-` 在使用 **height** 时， 不同的地方
前者，将当前窗口设置成 **height** 高度的窗口；
后者，将当前窗口高度增加/减少 **height** 

> 注：
直接使用 `CTRL-W _`，将当前窗口最大化

移动窗口
----
`CTRL-W SHIFT-H/J/K/L`

对所有窗口操作
----
`:_all`
** _ ** 代表所有对窗口的操作，比如 `w` `q` 等

文档比较
----
`:(vertical) diffsplit xx.file`
> 如果没有 **vertical** ，则上下分开 

打开标签页
----
`:tabedit`

标签之间跳转
----
`gt` , Goto Tab

关闭其他标签页
----
`:tabonly`
