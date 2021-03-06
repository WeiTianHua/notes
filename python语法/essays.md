

[TOC]



## 源码文件的编码

如果一条注释位于 Python 脚本的第一或第二行，并且匹配正则表达式 `coding[=:]\s*([-\w.]+)`，这条注释会被作为编码声明来处理；上述表达式的第一组指定了源码文件的编码。编码声明必须独占一行。如果它是在第二行，则第一行也必须是注释。推荐的编码声明形式如下

```
# -*- coding: <encoding-name> -*-
```

这也是 GNU Emacs 认可的形式，以及

```
# vim:fileencoding=<encoding-name>
```

如果没有编码声明，则默认编码为 UTF-8。此外，如果文件的首字节为 UTF-8 字节顺序标志 (`b'\xef\xbb\xbf'`)，文件编码也声明为 UTF-8 



## 显式的行拼接

两个或更多个物理行可使用反斜杠字符 (`\`) 拼接为一个逻辑行，规则如下: 当一个物理行以一个不在字符串或注释内的反斜杠结尾时，它将与下一行拼接构成一个单独的逻辑行，反斜框及其后的换行符会被删除。

以反斜杠结束的行不能带有注释。反斜杠不能用来拼接注释。反斜杠不能用来拼接形符，字符串除外 (即原文字符串以外的形符不能用反斜杠分隔到两个物理行)。不允许有原文字符串以外的反斜杠存在于物理行的其他位置。

隐式的行拼接可以带有注释。后续行的缩进不影响程序结构。后续行也允许为空白行。隐式拼接的行之间不会有 NEWLINE 形符。隐式拼接的行也可以出现于三引号字符串中 (见下)；此情况下这些行不允许带有注释。



## 对象、值与类型

每个对象都有各自的编号、类型和值。一个对象被创建后，它的 *编号* 就绝不会改变；你可以将其理解为该对象在内存中的地址。 '[`is`](https://docs.python.org/zh-cn/3/reference/expressions.html#is)' 运算符可以比较两个对象的编号是否相同；[`id()`](https://docs.python.org/zh-cn/3/library/functions.html#id) 函数能返回一个代表其编号的整型数。

对象的类型决定该对象所支持的操作 (例如 "对象是否有长度属性？") 并且定义了该类型的对象可能的取值。[`type()`](https://docs.python.org/zh-cn/3/library/functions.html#type) 函数能返回一个对象的类型 (类型本身也是对象)。与编号一样，一个对象的 *类型* 也是不可改变的。

有些对象的 *值* 可以改变。值可以改变的对象被称为 *可变的*；值不可以改变的对象就被称为 *不可变的*。(一个不可变容器对象如果包含对可变对象的引用，当后者的值改变时，前者的值也会改变；但是该容器仍属于不可变对象，因为它所包含的对象集是不会改变的。因此，不可变并不严格等同于值不能改变，实际含义要更微妙。) 一个对象的可变性是由其类型决定的；例如，数字、字符串和元组是不可变的，而字典和列表是可变的。

有些对象包含对其他对象的引用；它们被称为 *容器*。容器的例子有元组、列表和字典等。这些引用是容器对象值的组成部分。在多数情况下，当谈论一个容器的值时，我们是指所包含对象的值而不是其编号；但是，当我们谈论一个容器的可变性时，则仅指其直接包含的对象的编号。因此，如果一个不可变容器 (例如元组) 包含对一个可变对象的引用，则当该可变对象被改变时容器的值也会改变。

类型会影响对象行为的几乎所有方面。甚至对象编号的重要性也在某种程度上受到影响: 对于不可变类型，会得出新值的运算实际上会返回对相同类型和取值的任一现有对象的引用，而对于可变类型来说这是不允许的。例如在 `a= 1; b = 1` 之后，`a` 和 `b` 可能会也可能不会指向同一个值为一的对象，这取决于具体实现，但是在 `c = []; d =[]` 之后，`c` 和 `d` 保证会指向两个不同、单独的新建空列表。(请注意 `c = d = []` 则是将同一个对象赋值给 `c` 和 `d`。)



## 实例方法

实例方法用于结合类、类实例和任何可调用对象 (通常为用户定义函数)。

特殊的只读属性: `__self__` 为类实例对象本身，`__func__` 为函数对象；`__doc__` 为方法的文档 (与 `__func__.__doc__` 作用相同)；[`__name__`](https://docs.python.org/zh-cn/3/library/stdtypes.html#definition.__name__) 为方法名称 (与 `__func__.__name__` 作用相同)；`__module__` 为方法所属模块的名称，没有则为 `None`。

```python
class AA:
    def aaa(self):
        print(dir(self.aaa))

a = AA()
#a.aaa.__func__==AA.aaa!=a.aaa
#AA.aaa(a)==a.aaa()
#a.aaa.__self__==a
#AA.aaa==a.aaa.__func__

['__call__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__func__', '__ge__', '__get__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__self__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']

```





