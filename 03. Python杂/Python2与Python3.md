# Python2与Python3

- Python2中Python3中的print()
```python
# Python2
print "hello" # 不用()也能输出
print("hello")

# Python3
print("hello")
```

<br>

- Python2中的input()

    会将输入内容当做代码执行，类似于python3中的eval()函数

```python
# Python2
input() # 对应3中的eval()
raw_input() # 对应python3中的inpu()

# Python3
eval()
input()
```

<br>

- Python2中的`dict.has_key()`方法在3中已经没了

<br>

- Python2中的`cmp()`函数在3中没有了

<br>

- `range()`

    Python2中`range()`生成一个列表，遍历的是列表的每一个元素
    
    Python3中`range()`是一个**生成器**，每次生成器只会产生一个数

<br>

- Python2中的包目录下必须要有`__init__.py`文件

- `@property`在python2中不提供`setter`等其他的功能