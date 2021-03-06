[TOC]





## vi/vim 编辑器

vi 编辑器是文字处理软件， 所有的 Unix Like 系统都会内建 vi ；

Vim是从 vi 发展出来的一个文本编辑器， vim 是一个程序开发工具而不是文字处理软件，代码补完、编译及错误跳转等方便编程的功能特别丰富，在程序员中被广泛使用。

 vim 的官方网站 ([http://www.vim.org](http://www.vim.org/))



![img](vi.assets\vi-vim-cheat-sheet-sch.gif)



## 基础操作

### 使用

在Linux shell下 `vi filename` 进入编辑器 

```shell
vi filename
```

文件名可以是相对路径也可以是绝对路径，无此文件会创建此文件



### 模式

基本上 vi/vim 共分为三种模式，分别是**命令模式（Command mode）**，**输入模式（Insert mode）**和**底线命令模式（Last line mode）**。

#### 命令模式：

用户刚刚启动 vi/vim，便进入了命令模式。

此状态下敲击键盘动作会被Vim识别为命令，而非输入字符。比如我们此时按下`i`，并不会输入一个字符，`i`被当作了一个命令。

命令模式只有一些最基本的命令，因此仍要依靠底线命令模式输入更多命令。

**切换到输入模式**

| 按键 | 进入输入模式                                                 |
| :--- | ------------------------------------------------------------ |
| i, I | i 为『从目前光标所在处输入』， I 为『在目前所在行的第一个非空格符处开始输入』 |
| a, A | a 为『从目前光标所在的下一个字符处开始输入』， A 为『从光标所在行的最后一个字符处开始输入』 |
| o, O | 这是英文字母 o 的大小写。o 为『在目前光标所在的下一行处输入新的一行』； O 为在目前光标所在处的上一行输入新的一行 |
| s,S  | s 删除光标处字符，从目前光标所在处输入；S删除光标处行，从目前光标所在处输入 |
| r, R | r 只会取代光标所在的那一个字符一次；R会一直取代光标所在的文字，直到按下 ESC 为止 |



#### 输入模式

在命令模式下按下`i`就进入了输入模式，进行文本输入编辑的模式。

在输入模式中，可以使用以下按键：

- **字符按键以及Shift组合**，输入字符
- **ENTER**，回车键，换行
- **BACK SPACE**，退格键，删除光标前一个字符
- **DEL**，删除键，删除光标后一个字符
- **方向键**，在文本中移动光标
- **HOME**/**END**，移动光标到行首/行尾
- **Page Up**/**Page Down**，上/下翻页
- **Insert**，切换光标为输入/替换模式，光标将变成竖线/下划线
- **ESC**，退出输入模式，切换到命令模式



#### 底线命令模式

在命令模式下按下:（英文冒号）就进入了底线命令模式。

底线命令模式可以输入单个或多个字符的命令，可用的命令非常多。

在底线命令模式中，基本的命令有（已经省略了冒号）：

- **w** 保存文件
- **q** 退出程序
- **wq** 保存并退出
- **ESC**  退出底线命令模式，切换到命令模式



## 复杂操作

### 移动光标

**按方向移动**

| 按键               | 功能                 |
| :----------------- | -------------------- |
| h 或 向左箭头键(←) | 光标向左移动一个字符 |
| j 或 向下箭头键(↓) | 光标向下移动一个字符 |
| k 或 向上箭头键(↑) | 光标向上移动一个字符 |
| l 或 向右箭头键(→) | 光标向右移动一个字符 |

如果想要进行多次移动的话，例如向下移动 30 行，可以使用 `30j` 或 `30↓` 的组合按键， 亦即加上想要进行的次数(数字)后，按下动作即可。

|      按键      |                           功能                            |
| :------------: | :-------------------------------------------------------: |
| **按文档移动** |                                                           |
|       gg       |             移动到这个档案的第一行，相当于 1G             |
|       nG       |             n 为数字。移动到这个档案的第 n 行             |
|       G        |                    移动到文档最后一行                     |
|    **翻页**    |                                                           |
|    Ctrl + f    |       屏幕『向下』移动一页，相当于 [Page Down]按键        |
|    Ctrl + b    |        屏幕『向上』移动一页，相当于 [Page Up] 按键        |
|    Ctrl + d    |                   屏幕『向下』移动半页                    |
|    Ctrl + u    |                   屏幕『向上』移动半页                    |
| **按屏幕移动** |                                                           |
|       H        |     光标移动到这个**屏幕的最上方**那一行的第一个字符      |
|       M        |      光标移动到这个**屏幕的中央**那一行的第一个字符       |
|       L        |     光标移动到这个**屏幕的最下方**那一行的第一个字符      |
| **按段落移动** |                                                           |
|       {        |                           上移                            |
|       }        |                           下移                            |
|  **按行移动**  |                                                           |
|       +        |                     光标移动到下一行                      |
|       -        |                     光标移动到上一行                      |
|    n<Enter>    |             n 为数字，光标向下移动 n 行(常用)             |
| **按字符移动** |                                                           |
|    n<space>    | n 为数字，按下数字后再按空格键，光标会向右移动 n 个字符。 |
|  0 或 [Home]   |          这是数字 0 ，移动到这一行的最前面字符处          |
|   $ 或[End]    |                移动到这一行的最后面字符处                 |
|       e        |                光标向后移动到第一个空格前                 |
|       w        |                光标向后移动到第一个空格后                 |



### 搜索

| 按键  | 功能                                                         |
| :---: | ------------------------------------------------------------ |
| /word | 向光标之下寻找匹配文本（第一个）。例如要在档案内搜寻 vbird 这个字符串，就输入 /vbird 即可 |
| ?word | 向光标之上寻找匹配文本（第一个）                             |
|   n   | n 是英文按键，在查找规则下搜寻下一个匹配文本                 |
|   N   | N 是英文按键，向查找规则相反的方向搜寻下一个匹配文本， 把 / 和 ？ 互换 |

搜索之后按 `Enter`键，再按 `n` 或`N` 

  

### 替换

| 按键                                       | 功能                                                         |
| ------------------------------------------ | ------------------------------------------------------------ |
| :n1,n2s/word1/word2/g                      | n1 与 n2 为数字。在第 n1 与 n2 行之间寻找 word1 这个字符串，并将该字符串取代为 word2 |
| :1,$s/word1/word2/g或 :%s/word1/word2/g    | 从第一行到最后一行寻找 word1 字符串，并将该字符串取代为 word2 |
| :1,$s/word1/word2/gc 或 :%s/word1/word2/gc | 从第一行到最后一行寻找 word1 字符串，并将该字符串取代为 word2 ！且在取代前显示提示字符给用户确认 (confirm) 是否需要取代！ |



### 删除

|     按键     | 功能                                                         |
| :----------: | ------------------------------------------------------------ |
| **删除字符** |                                                              |
|    x， nx    | x 为向后删除一个字符 (相当于 [del] 按键)， n 为一次删除几个字符 |
|    X，nX     | X 为向前删除一个字符(相当于 [backspace] 亦即是退格键)，n 为一次删除几个字符 |
|      d0      | 那个是数字的 0 ，删除光标所在处，到该行的最前面一个字符      |
|      d$      | 删除光标所在处，到该行的最后一个字符                         |
|      D       | 删除光标所在行的所有文本，不换行                             |
|  **删除行**  |                                                              |
|      dd      | 删除光标所在的那一行，换行                                   |
|      dn      | n 为数字，删除光标所在的那一行，和向下n行                    |
|     ndd      | n 为数字，删除光标所在的向下 n 行，例如 20dd 则是删除光标以下 20 行 |
|     d1G      | 删除光标所在到第一行的所有数据                               |
|      dG      | 删除光标所在到最后一行的所有数据                             |
|     ncj      | 按方向键删除n数据，并进入插入模式   `10cj `  ` 5ck ` `2c↑`   |



### 复制与粘贴

|  按键   | 功能                                                   |
| :-----: | ------------------------------------------------------ |
|    y    | 复制光标所在行和下一行的数据                           |
|   yy    | 复制光标所在行数据                                     |
| ny，nyy | n 为数字，复制光标所在行的向下 n 行数据                |
|   y1G   | 复制光标所在行到第一行的所有数据                       |
|   yG    | 复制光标所在行到最后一行的所有数据                     |
|   y0    | 复制光标所在的那个字符到该行行首的所有数据             |
|   y$    | 复制光标所在的那个字符到该行行尾的所有数据             |
|  p, P   | p 为将已复制的数据贴在光标下一行，P 则为贴在光标上一行 |



### 合并行

| 按键 | 功能                                   |
| ---- | -------------------------------------- |
| J    | 将光标所在行与下一行的数据结合成同一行 |



### 撤销

| 按键 | 功能           |
| ---- | -------------- |
| u    | 撤销前一个动作 |



### 恢复撤销

| 按键     | 功能                       |
| -------- | -------------------------- |
| [Ctrl]+r | 恢复撤销的动作, u 的逆操作 |



### 重复前动作

| 按键 | 功能                                                         |
| ---- | ------------------------------------------------------------ |
| .    | 小数点，意思是重复前（非撤销和恢复）一个动作的意思。 如果你想要重复删除、重复贴上等等动作 |



### 移动

|      |             |
| ---- | ----------- |
| >>   | 文本行右移  |
| <<   | 文本行左移  |
| n >> | n行向右移动 |
| n << | n行向左移动 |



### 选中

|      |                     |
| ---- | ------------------- |
| v    | 按字符移动,选中文本 |
| V    | 按行移动,选中文本   |

可以配合 `d`,` y`,` >>`,` << `实现对文本块的删除,复制,左右移动



## 储存、离开

|                     |                                                              |
| ------------------- | ------------------------------------------------------------ |
| :w                  | 将编辑的数据写入硬盘档案中(常用)                             |
| :w!                 | 若文件属性为『只读』时，强制写入该档案。不过，到底能不能写入， 还是跟你对该档案的档案权限有关啊！ |
| :q                  | 离开 vi (常用)                                               |
| :q!                 | 若曾修改过档案，又不想储存，使用 ! 为强制离开不储存档案。    |
| :wq                 | 储存后离开，若为 :wq! 则为强制储存后离开 (常用)              |
| :e!                 | 放弃所有修改，从上次保存文件开始再编辑                       |
| :x                  | 写入文件并退出。仅当文件被修改时才写入，并更新文件修改时间，否则不会更新文件修改时间。 |
| ZZ                  | 这是大写的 Z 喔！若档案没有更动，则不储存离开，若档案已经被更动过，则储存后离开！ |
| :w newfile          | 文件另存为newfile,但是当前文件也在，编辑的时候编辑就是当前文件 |
| :n1,n2 w [filename] | 将 n1 到 n2 的内容储存成 filename 这个档案。                 |
| :sp newfile         | 分出一个窗口编辑newfile文件。                                |



## vim 环境的变更

|           |                                                    |
| :-------- | -------------------------------------------------- |
| :set nu   | 显示行号，设定之后，会在每一行的前缀显示该行的行号 |
| :set nonu | 与 set nu 相反，为取消行号！                       |





## vim里执行 shell 命令

底线命令模式里输入`!`,  后面跟命令

```shell
!ls -la
```

