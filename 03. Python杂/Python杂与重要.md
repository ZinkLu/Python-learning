# Python杂，但是重要！

- 用于测试时候的打印，用`,`逗号分隔打印内容

    ```python
    a = 10
    print("a的值", a)
    
    >>> a的值 10
    ```

<br>

- 区间比较

    ```python
    a = 20
    18 <= a <= 22 -> True # only Python
    ```

<br>

- 三元运算符

    ```python
    # python
    a = 10
    b = 20
    c = a if a>b else b
    # 如果a>b 将a赋值给c，否则，将b赋值给c
    ```
    
    ```swift
    // swift
    let contentHeight = 40;
    let hasHeader = true;
    let rowHeight = contentHeight + (hasHeader ? 50 : 20)
    print("rowHeight = \(rowHeight)");
    //输出 rowHeight =  90
    ```

<br>

- 数字逻辑运算符

    ```python
    # 只有0是False，其他都是True
    a = 0
    b = 1
    c = 3
    
    # 有0 ，and后为0，没有0，得到后面的数字
    a and b -> 0
    a and c -> 0
    b and c -> 3
    c and b -> 1
    
    # 都为0 ，or 才0，否则等于非0数字，或者在or之前的数字
    a or b -> 1
    b or c -> 1
    c or b -> 3
    a or a -> 0
    ```

<br>

- 有关于True和False

  在Python中，`0`、`0.0`、`空字符串""`、`None`被认为是Flase，其他值被认为是True
  
  ```python
  >>> None or ""
  ""
  
  >>> "" or None
  # 得到的是None 所以没有输出 
  ```

<br>

- 多重赋值（拆包）

    用所有列表的值为多个变量赋值，适用于元组
  
    > 注意变量的数目和列表的长度必须严格相等
    
    ```python
    cat = ["fat", "black", "loud"]
    size, color, disposition = cat
    ``` 

<br>

- 将可变类型数据作为参数传入函数

  传入函数的是该数据 **引用**  
  
> `copy`模块的存在

```python
# 什么是可变数据类型，也就是引用类型
a = 10
b = a
a = 20

# b还等于10，整型是不可变类型
a = [1, 2, 3]
b = a
a.append(4)
print(b)
>>> [1, 2, 3, 4]
# 列表是可变数据类型,在传递时实际传递的是引用

def append(aList):
	aList.append(10)
	print(aList)
append(a)
>>> [1, 2, 3, 10]
print(a)
>>> [1, 2, 3，10]
```

<br>

- range() - 和切片差不多

  - 有两个参数，第一个是起始位置，第二是结束位置（结束位置不包含在内）
  - 有一个参数，代表结束位置，起始位置默认是0
  - 有三个参数，第一个是起始位置，第二是结束位置（结束位置不包含在内），第三个是步长
  - 一般用于for循环

> range() - 生成器
> 
> 特点:一次只产生一个数据


<br>

- 原始字符串

    在字符串开始的引号之前加`r`，使它成为一个原始字符串
    
    会将转译字符也打印出来，用于正则表达式

    ```python
    print(r"That is Carol\'s cat.")
    >>> That is Carol\'s cat.
    ```
    
<br>

- `strip()`的使用

    `strip()`可以去除字符串两边的所有空格，如果指定参数的话可以去掉字符串两边所有参数中的字符(无顺序)
    
    ```python
    string = 'SpamSpamBaconSpamEggSpamSpam'
    
    print(string.strip('Spam'))
    >>> BaconSpamEgg
    
    print(string.strip('maSp'))
    >>> BaconSpamEgg
    ```

<br>

- 重名函数(编程中千万不要重名)
    
    - 如果定义了两个同名的函数，在调用函数时，会调用后一个函数。

    - 相当于定义了一个**新的函数**
    
    - 如果又定义了一个变量和函数名相同，则无法再调用之前的函数了。

<br>

- 编程中对文件的处理时：

    - 源文件：source file ：`scr_file`
    
    - 目标文件：destination file：`dst_file`

<br>

- `repr()`方法
    
    可以查看数据的**原始定义格式**，这个和**原始字符串**有什么区别？
    
    ```python
    a = '123'
    b = 123
    
    print(repr(a))
    print(repr(b))
    
    >>> '123'
    >>> 123
    ```

<br>

- 大文件的读取方法(一般用法)

    以字节读取，`f.read(1024*8)`，相对稳妥的方法。
    

<br>

- `.pyw`结尾的`Python`文件在执行时可以不显示终端窗口

<br>

- 对于任意函数，都可以通过类似`func(*args, **kw)`的形式调用它，无论它的参数是如何定义的。 - 很神奇(请看)

> 7月31号看到偏函数的时候不太理解所谓的三个函数什么意思

```python
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


>>> args = (1, 2, 3, 4)
>>> kw = {'d': 99, 'x': '#'}
>>> f1(*args, **kw)  # 在对元组进行解包的时候，居然自动对上了位置参数..
a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}

>>> args = (1, 2, 3)
>>> kw = {'d': 88, 'x': '#'}
>>> f2(*args, **kw)  # 这里在对字典解包的时候如果key和函数名一样还能对上命名函数
a = 1 b = 2 c = 3 d = 88 kw = {'x': '#'}
```

<br>

- `isinstance()`函数可以判断有继承关系的对象和类

    > 可以用来判断输入，例如希望传入参数时数字时，`if isinstance(arg, int):` 就可以了！
    
    ```
    A -> B -> C -> D
    ```
    
    ```python
    >>> a = A()
    >>> b = B()
    >>> c = C()
    >>> d = D()
    >>> isinstance(a, A)
    True
    >>> isinstance(a, (A, B, C, D))  # 同时判断多个
    True
    >>> isinstance(b, A)
    Flase
    ```

<br>

- 格式化字符串 - `str.format()`版本，厉害

    - 基本格式(元组、位置)
    
    ```python
    >>> "{},{}".format("111", "222")
    '111,222'
    
    >>> "{0},{1}".format("111", "222")  # 后面本质是个元组
    '111,222'
    
    >>> "{0},{1},{0}".format("111", "222")
    '111,222,111'
    ```
    
    - 关键字(字典)
    
    ```python
    >>> '{name},{age}'.format(age=18,name='LLL') 
    'LLL,18'
    ```
    
    - 下标(本质上是用过元组取到了列表，再通过下标取到了元素)
    
    ```python
    >>> p=['LLL',18]
    >>> '{0[0]},{0[1]}'.format(p)
    'LLL,18'    
    ```
    
    - 格式限定符
    
        `^`、`<`、`>`分别是居中、左对齐、右对齐，后面带宽度
        
        `:`后面带填充的字符，只能是一个字符，不指定的话默认是用空格填充
    
    ```python
    >>> '{:>8}'.format('189')
    '   189'
    >>> '{:0>8}'.format('189')
    '00000189'
    >>> '{:a>8}'.format('189')
    'aaaaa189'
    ```
    
    - 精度与类型f
    
    ```python
    >>> '{:.2f}'.format(321.33345)
    '321.33'
    ```
    
    - 其他类型
    
        主要就是进制了，b、d、o、x分别是二进制、十进制、八进制、十六进制。
    
    - `,`转化成金额的千位分隔符
    
    ```python
    >>> '{:,}'.format(1234567890)
    '1,234,567,890'
    ```
    
    > [格式化说明符](https://docs.python.org/3/library/string.html#formatspec)
    
<br>

- 工厂函数
    
    闭包？