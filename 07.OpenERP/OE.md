# Open-ERP笔记

[TOC]

> [官方文档](https://doc.odoo.com/6.1/zh_CN/developer/01_getting_started/)


问题：

> 这里的ORM？使用的是？
>
> `Three-tier_architecture`？
> 
> View是xml文件，这个是什么意思？
> 
> Controller指的是OpenERP对象？不应该是业务逻辑么？视图函数
> 
> JSON-RPC和XML-RPC具体指的什么

## 1. 安装

`OS_X`安装

1. 下载Xcode

    - 安装`xcode-select —install`

2. 下载`openerp7.0`并且安装

    - `http://nightly.odoo.com/7.0/nightly/src/`

3. 根据pip提示安装依赖，安装依赖过程中的问题

    1. `m2crypto`安装问题

    ```sh
    # 如果m2crypto安装不上使用这个命令
    sudo env LDFLAGS="-L$(brew --prefix openssl)/lib" CFLAGS="-I$(brew --prefix openssl)/include" SWIG_FEATURES="-cpperraswarn -includeall -I$(brew --prefix openssl)/include" pip install m2crypto
    ```
    
    2. PIL安装问题

        - 由于PIL已经改名为Pillow，虽然API相同，但是openerp默认还是需要PIL

        - 解决方法：安装`pip install pillow==2.8.1`，将`pillow-2.8.1.dist-info`改为`PIL-2.8.1.dist-info`

        - 或者安装`m3-PIL`但是可能会报clang的错，解决方法`sudo ln -s /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.14.sdk/System/Library/Frameworks/Tk.framework/Versions/8.5/Headers/X11 /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.14.sdk/usr/include`， 根据实际情况来

    3. `Crypto`问题
    
        - `sudo mv /Library/Python/2.7/site-packages/crypto /Library/Python/2.7/site-packages/Crypto`

    4. 如果pip安装不了记得使用`sudo`

    5. 如果pypi上没有的包记得去github上找，这类包安装的方法就是`python setup.py install`

    6. 如果使用了python的虚拟环境的话可能有别的问题..

    7. OE依赖`psotgresql`，别忘了安装

    8. 还有一些包可能版本不对，还是问一下同事他们包的版本，比如`six`

4. 启动OE
    
    1. `openerp-server`，显示`OpenERP server is running, waiting for connections...`就ok

    2. 浏览器访问`0.0.0.0:8069`

    3. 常用运行参数
        
        - `--version` 显示版本信息，然后结束

        - `-c CONFIG`, `--config=CONFIG` 指定配置文件
        
        - `-v, --verbose` 开启调试输出

        - `--logfile=LOGFILE` 存储LOG的文件

        - `-n INTERFACE, --interface=INTERFACE` 监听IP地址

        - `-p PORT, --port=PORT` 监听 TCP 端口

        - `--debug` 开启调试模式

5. 配置文件
    
    - 服务端配置文件 `~/.openerp_serverrc` 用于保存服务启动参数

<table>
<colgroup><col>
<col>
</colgroup><tbody>
<tr><th>interface:</th><td><p id="s838cbd2ab1f947e38cf3b9b5e9138e94">服务器绑定的IP地址</p>
</td>
</tr>
<tr><th>port:</th><td><p id="sf1ab6cb138d649dc9db4aaef1de8d804">监听端口</p>
</td>
</tr>
<tr><th>database:</th><td><p id="sb3fd9a2c0b4c4048a885f26841b2f9fe">数据库名称</p>
</td>
</tr>
<tr><th>user:</th><td><p id="s44f6410edbc942769e68e155fbf944c5">数据库连接帐号用户名</p>
</td>
</tr>
<tr><th>translate_in:</th><td><p id="s394d1402cd1c405297d2803bfe5e7bc1">导入翻译文件</p>
</td>
</tr>
<tr><th>translate_out:</th><td><p id="se08bf6cc6fa140a8bc671af83f991a20">导出翻译文件</p>
</td>
</tr>
<tr><th>language:</th><td><p id="se3a2fd1f890f4faa8b5570823581a1b0">默认载入语言. 必须是符合 W3C 标准的 ISO 国家代码，</p>
</td>
</tr>
<tr><th>verbose:</th><td><p id="s64f328d4f8ed4b4f832dbd56cd3e9dfd">开启调试输出</p>
</td>
</tr>
<tr><th>init:</th><td><p id="sba90ca5e7f314bf1ac2681504d2e1b85">初始化模块 ("all" 参数为初始化所有模块)</p>
</td>
</tr>
<tr><th>update:</th><td><p id="s1f1ad781ab104ae88be08ac68e58ed70">升级模块 ( "all" 参数为升级所有模块)</p>
</td>
</tr>
<tr><th>upgrade:</th><td><p id="s3c474393427045c18bbb9a50dce4834a">升级/安装/卸载 模块</p>
</td>
</tr>
<tr><th>db_name:</th><td><p id="sebf7b4efeef74a5abba0f06b0b80f469">指定数据库名</p>
</td>
</tr>
<tr><th>db_user:</th><td><p id="sa6d7304a0b944553bc5706917021bb92">数据库用户名</p>
</td>
</tr>
<tr><th>db_password:</th><td><p id="s0f4e4b10cc0848ad9f02cb31e5077f93">数据库密码</p>
</td>
</tr>
<tr><th>pg_path:</th><td><p id="s8d9f8d768a6245d692a36a8779d6b019">PostgreSQL可执行文件所在路径</p>
</td>
</tr>
<tr><th>db_host:</th><td><p id="s9ea02d5e58164028b8abd66412fd696e">数据库主机名或IP地址</p>
</td>
</tr>
<tr><th>db_port:</th><td><p id="s84bb587bb6c745a987780f7a378dfe38">数据库端口</p>
</td>
</tr>
<tr><th colspan="2">translate_modules:</th></tr>
<tr><td>&nbsp;</td><td><p id="s278abf823c4046f98a000486832e4e83">指定导出翻译模块，与 --i18n-export 参数一起使用</p>
</td>
</tr>
</tbody>
</table>

<br>
<br>
<br>

## 2. OpenERP的架构 - architecture

B/S架构：基于浏览器

MVC架构

- Model - 数据库 - Postgresql

- Controller - OpenERP对象

- View - OpenERP中定义的XML文件

![image](https://doc.odoo.com/doc_static/6.1/_images/client_server.png)

<br>
<br>
<br>

## 3. Modules

### 3.1 Module Structure

1. 如果创建一个`module`必须遵守这几个规定

    1. 在`server/addons/`目录中创建子目录

    2. 创建模块描述文件`__openerp__.py`

    3. 创建包含`ORM对象`的Python文件

    4. 创建包含数据的`.xml`文件

    5. `reports`， `wizards`， `workflows`文件夹选择性创建
    
    	- `wizards`用于协助用户状态的互动形式，经常用做模块上下文传递

    	- `Reports`xml格式，MAKO或者OpenOffice报表模版，通过数据请求可以生成HTML，ODT或者PDF报表

2. XML文件的用处有：

    1. 初始化并且准备演示数据

    2. [views declaration](#view)

    3. reports declaration

    4. wizards declaration

    5. workflows declaration

    6. 等等

3. `__openerp__.py`文件的用处

    1. 决定了那些`xml`文件要被解析

    2. 决定了改模块的依赖项

4. `__openerp__.py`文件内容

    1. 是一个Python字典，包含了以下键值对

    - name：模块的名称

    - version：模块的版本

    - description：模块的描述

    - author：作者信息

    - website：模块主页

    - license：许可，默认是GPL—2

    - depends：列出了改模块的依赖，一般来说`base module`必须在依赖列表中

    - init： 当使用命令`--init=module`时，加载列表中的.xml文件路径，注意路径必须该模块所在目录的相对路径

    - demo：列出了提供演示数据的.xml文件

    - installable：`True`或者`False`，决定该模块是否可以安装

    - images：截图列表，将在`http://apps.openerp.com`上展示

    - active：`True`或者`False`，默认`False`，决定了该模块是否需要创建数据库
    
    - test：.yml测试文件

    - data：模块安装和升级时需要重新加载的xml文件，基础数据，权限，工作流，视图、报表等的定义文件通常放在此处（权限一般放在最前面，因为其他文件常常引用权限定义数据）。

    - auto_install：是否自动安装，一般为`False`

<br>
<br>
<br>

## 4. ORM

1. 包含ORM模型的文件

    - 在OpenERP中所有的资源都是ORM对象

    ![image](https://doc.odoo.com/doc_static/6.1/_images/pom_3_0_3.png)

2. 默认数据可以通过xml导入，如

    ```xml
    <?xml version="1.0"? encoding="utf-8">
    <openerp>
      <data>
        <record model="model.name_1" id="id_name_1">
          <field name="field1">
            "field1 content"
          </field>
          <field name="field2">
            "field2 content"
          </field>
          (...)
        </record>
        <record model="model.name_2" id="id_name_2">
            (...)
        </record>
        (...)
      </data>
    </openerp>
    ```

### 4.1 ORM对象属性

|||
|---|---|
|_name (required)|业务对象名称，每张实体表都有，方便系统维护，默认使用module.+name的形式|
|_columns (required)|字典{字段名 -> 字段申明}|
|_defaults|提供字段的默认值与可以使用的函数 `_defaults['name'] = lambda self,cr,uid,context:'eggs'`|
|_auto|如果是True（默认）的ORM将创建数据库表 - 设置为Flase需要实现init()方法来创建自己的表/视图|
|_inherit|普通继承，`_inherit="product.product"` 继承产品对象，给产品对象添加字段摸着方法，不需要设置`_name`, `_table`等属性，注意：当继承后的子类不定义`_name`属性，则相当于在父类中增加字段和方法，并不创建对象，当继承后的子类重新定义`_name`属性，则创建一个新的对象，新对象拥有父类中所有的字段和方法，父类不受任何影响|
|_inherits|代理继承，`_inherits = {'product.template':'product_tmpl_id'}` 继承产品模版对象，穿件新的产品对象，产品对象和产品对象之间建立多对一关联关系，产品模版中的字段可以等同产品中的字段一样使用 注意：相同于多重继承，子类通过`_inheits`中定义的字段和各个父类关联，子类不拥有父类的字段，但可以直接操作父类的所有字段和方法 `_inheit=['calendar.event', 'mail.thread', 'ir.needaction_mixin']`|
|_constraints|对象约束，一般用于业务逻辑复杂，服务通过创建数据库约束实现的情况，是一个列表，包含元组：(func_name, message, fields)|
|_sql_constraints|数据库约束，最底层级别的约束，模块安装后对象将在PG对应的表中创建约束，是一个列表，包含元组：(name, sql_def, message)|
|_log_access|默认可以创建四个字段(create_uid, create_date, write_uid,write_date)用于日志记录级别的操作，可通过`perm_read()`函数读取|
|_order|数据库排序，默认使用id|
|_rec_name|其他对象调用时默认使用name_get()方法获取，但是这个地方根据需要可以组合改写显示信息|
|_sql|SQL代码来创建次对象的表/视图（如果_AUTO时False）可以被`init`取代|
|_table|取代SQL表名，默认是`_name`，将`.`换成`_`|
|init|对象初始化数据|

### 4.2 ORM字段类型

定义字段时的通用参数`fields.xxx(para)`

<table>
<colgroup><col>
<col>
</colgroup><tbody valign="top">
<tr><th>change_default:</th><td><p>别的字段的缺省值是否可依赖于本字段。这些缺省值定义在ir.values表格中。</p>
</td>
</tr>
<tr><th>help:</th><td><p用于描述这个字段如何使用：更长的描述文字。当鼠标滑过该字段时将会显示在一个提示框中。</p>
</td>
</tr>
<tr><th>ondelete:</th><td><p>如何处理相关记录的删除。允许的值有：‘restrict’, ‘no action’, ‘cascade’, ‘set null’, and ‘set default’。</p>
</td>
</tr>
<tr><th>priority:</th><td><p>Not used？</p>
</td>
</tr>
<tr><th>readonly:</th><td><p>当值为True时，该字段只读不可修改，缺省值：False</p>
</td>
</tr>
<tr><th>required:</th><td><p>当值为True时，在对象存储前，该字段必须有个值，缺省值：False</p>
</td>
</tr>
<tr><th>size:</th><td><p>数据库中该字段的size：number characters or digits.</p>
</td>
</tr>
<tr><th>states:</th><td><p>让我们为这个对象特定的states重写其他参数，Accepts a dictionary with the state names as keys and a list of name/value tuples as the values. For example: states={‘posted’:[(‘readonly’,True)]}</p>
</td>
</tr>
<tr><th>string:</th><td><p>The field name as it should appear in a label or column header. Strings containing non-ASCII characters must use python unicode objects. For example: ‘tested’: fields.boolean(u’Testé’)</p>
</td>
</tr>
<tr><th>translate:</th><td><p>值为True的话应该翻译这个字段的content，为False的话就不翻。</p>
</td>
</tr>
</tbody>
</table>

还有一些参数：

- password=True 密码星号显示

- nolabel=1 隐藏标签

- attrs 属性 可以定义多添件字段只读，是否显示

- digits 直接格式化浮点字段

- default_focus 新开窗口光标位置

- Widget: 有多种部件显示格式

- select=1 默认搜索，=2高级搜索 -- 建索引？？

- priority 不知道...

- domain：域条件，缺省值[]

- record  不知道...

- incisible: 本字段是否显示

- selection：只用于reference字段类型

ORM字段类型对象包含3种类型的字段：基础类型，复杂类型，关系类型。

1. 基础类型：char,text,boolean,integer,float,date,time,datetime,binary

2. 复杂类型：selection,function,related

3. 关系类型：one2one,one2many,many2one,many2many

#### 4.2.1 基础类型

<table>
<colgroup><col>
<col>
</colgroup><tbody valign="top">
<tr><th>boolean:</th><td><p>布尔型(boolean) (true, false).</p>
<p>语法:</p>
<div><div><pre>fields.boolean('Field Name' [, Optional Parameters]),
</pre></div>
</div>
</td>
</tr>
<tr><th>integer:</th><td><p>整型(integer).</p>
<p>语法:</p>
<div><div><pre>fields.integer('Field Name' [, Optional Parameters]),
</pre></div>
</div>
</td>
</tr>
<tr><th>float:</th><td><p>浮点型(float).</p>
<p>语法:</p>
<div><div><pre>fields.float('Field Name' [, Optional Parameters]),
</pre></div>
</div>
<div>
<p>注解</p>
<p>digits定义整数部分和小数部分的位数。 The scale being the number of digits after the decimal point whereas the precision is the total number of significant digits in the number (before and after the decimal point). If the parameter digits is not present, the number will be a double precision floating point number. Warning: these floating-point numbers are inexact (not any value can be converted to its binary representation) and this can lead to rounding errors. You should always use the digits parameter for monetary amounts.</p>
</div>
<p>Example:</p>
<div><div><pre>'rate': fields.float(
    'Relative Change rate',
    digits=(12,6) [, Optional Parameters]),
</pre></div>
</div>
</td>
</tr>
<tr><th>char:</th><td><p>字符串(char): 限定长度的字符串，size属性定义字符串长度。</p>
<p>语法:</p>
<div><div><pre>fields.char(
        'Field Name',
        size=n [,
        Optional Parameters]), # where ''n'' is an integer.
</pre></div>
</div>
<p>Example:</p>
<div><div><pre>'city' : fields.char('City Name', size=30, required=True),
</pre></div>
</div>
</td>
</tr>
<tr><th>text:</th><td><p>没有长度限制的text field</p>
<p>语法:</p>
<div><div><pre>fields.text('Field Name' [, Optional Parameters]),
</pre></div>
</div>
</td>
</tr>
<tr><th>date:</th><td><p>A date.</p>
<p>语法:</p>
<div><div><pre>fields.date('Field Name' [, Optional Parameters]),
</pre></div>
</div>
</td>
</tr>
<tr><th>datetime:</th><td><p>Allows to store a date and the time of day in the same field.</p>
<p>语法:</p>
<div><div><pre>fields.datetime('Field Name' [, Optional Parameters]),
</pre></div>
</div>
</td>
</tr>
<tr><th>binary:</th><td><p>A binary chain</p>
</td>
</tr>
<tr><th>selection:</th><td><p>这个字段让用户对之前定义的值进行选择</p>
<p>语法:</p>
<div><div><pre>fields.selection((('n','Unconfirmed'), ('c','Confirmed')),
                   'Field Name' [, Optional Parameters]),
</pre></div>
</div>
<div>
<p>注解</p>
<p>Format of the selection parameter: tuple of tuples of strings of the form:</p>
<div><div><pre><span class="p">((</span><span class="s">'key_or_value'</span><span class="p">,</span> <span class="s">'string_to_display'</span><span class="p">),</span> <span class="o">...</span> <span class="p">)</span>
</pre></div>
</div>
</div>
<div>
<p>注解</p>
<p>You can specify a function that will return the tuple. Example</p>
<div><div><pre><span class="k">def</span> <span class="nf">_get_selection</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">cursor</span><span class="p">,</span> <span class="n">user_id</span><span class="p">,</span> <span class="n">context</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span>
    <span class="k">return</span> <span class="p">(</span>
       <span class="p">(</span><span class="s">'choice1'</span><span class="p">,</span> <span class="s">'This is the choice 1'</span><span class="p">),</span>
       <span class="p">(</span><span class="s">'choice2'</span><span class="p">,</span> <span class="s">'This is the choice 2'</span><span class="p">))</span>

<span class="n">_columns</span> <span class="o">=</span> <span class="p">{</span>
   <span class="s">'sel'</span> <span class="p">:</span> <span class="n">fields</span><span class="o">.</span><span class="n">selection</span><span class="p">(</span>
       <span class="n">_get_selection</span><span class="p">,</span>
       <span class="s">'What do you want ?'</span><span class="p">)</span>
<span class="p">}</span>
</pre></div>
</div>
</div>
<p><em>Example</em></p>
<p>Using relation fields <strong>many2one</strong> with <strong>selection</strong>. In fields definitions add:</p>
<div><div><pre>...,
'my_field': fields.many2one(
        'mymodule.relation.model',
        'Title',
        selection=_sel_func),
...,
</pre></div>
</div>
<p>And then define the _sel_func like this (but before the fields definitions):</p>
<div><div><pre><span class="k">def</span> <span class="nf">_sel_func</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">cr</span><span class="p">,</span> <span class="n">uid</span><span class="p">,</span> <span class="n">context</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span>
    <span class="n">obj</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">pool</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s">'mymodule.relation.model'</span><span class="p">)</span>
    <span class="n">ids</span> <span class="o">=</span> <span class="n">obj</span><span class="o">.</span><span class="n">search</span><span class="p">(</span><span class="n">cr</span><span class="p">,</span> <span class="n">uid</span><span class="p">,</span> <span class="p">[])</span>
    <span class="n">res</span> <span class="o">=</span> <span class="n">obj</span><span class="o">.</span><span class="n">read</span><span class="p">(</span><span class="n">cr</span><span class="p">,</span> <span class="n">uid</span><span class="p">,</span> <span class="n">ids</span><span class="p">,</span> <span class="p">[</span><span class="s">'name'</span><span class="p">,</span> <span class="s">'id'</span><span class="p">],</span> <span class="n">context</span><span class="p">)</span>
    <span class="n">res</span> <span class="o">=</span> <span class="p">[(</span><span class="n">r</span><span class="p">[</span><span class="s">'id'</span><span class="p">],</span> <span class="n">r</span><span class="p">[</span><span class="s">'name'</span><span class="p">])</span> <span class="k">for</span> <span class="n">r</span> <span class="ow">in</span> <span class="n">res</span><span class="p">]</span>
    <span class="k">return</span> <span class="n">res</span>
</pre></div>
</div>
</td>
</tr>
</tbody>
</table>

#### 4.2.2 关系类型：

<table>
<colgroup><col>
<col>
</colgroup><tbody>
<tr><th>one2one:</th><td><p>表示有两个对象是一对一的关系。现在用many2one来代替。</p>
<p>语法:</p>
<div><div><pre><span class="n">fields</span><span class="o">.</span><span class="n">one2one</span><span class="p">(</span><span class="s">'other.object.name'</span><span class="p">,</span> <span class="s">'Field Name'</span><span class="p">)</span>
</pre></div>
</div>
</td>
</tr>
<tr><th>many2one:</th><td><p>通过这个字段一个对象与它的父对象关联。例如，员工和部门的关系就是多对一的关系。</p>
<p>语法:</p>
<div><div><pre>fields.many2one(
        'other.object.name',
        'Field Name',
        optional parameters)
</pre></div>
</div>
<p>可选的参数：</p>
<blockquote>
<div><ul>
<li><dl>
<dt>ondelete: 当该字段指示的资源被删除时会发生些什么</dt>
<dd><ul>
<li><p>预先定义的值: "cascade", "set null", "restrict", "no action", "set default"</p>
</li>
<li><p>缺省值: "set null"</p>
</li>
</ul>
</dd>
</dl>
</li>
<li><p>required: True</p>
</li>
<li><p>readonly: True</p>
</li>
<li><p>select: True - (creates an index on the Foreign Key field)</p>
</li>
</ul>
</div></blockquote>
<p><em>Example</em></p>
<div><div><pre>'commercial': fields.many2one(
        'res.users',
        'Commercial',
        ondelete='cascade'),
</pre></div>
</div>
</td>
</tr>
<tr><th>one2many:</th><td><p>TODO</p>
<p>语法:</p>
<div><div><pre>fields.one2many(
        'other.object.name',
        'Field relation id',
        'Fieldname',
        optional parameter)
</pre></div>
</div>
<dl>
<dt>可选的参数：</dt>
<dd><ul>
<li><p>invisible: True/False</p>
</li>
<li><p>states: ?</p>
</li>
<li><p>readonly: True/False</p>
</li>
</ul>
</dd>
</dl>
<p><em>Example</em></p>
<div><div><pre>'address': fields.one2many(
        'res.partner.address',
        'partner_id',
        'Contacts'),
</pre></div>
</div>
</td>
</tr>
<tr><th>many2many:</th><td><p>TODO</p>
<p>语法:</p>
<div><div><pre><span class="n">fields</span><span class="o">.</span><span class="n">many2many</span><span class="p">(</span><span class="s">'other.object.name'</span><span class="p">,</span>
                 <span class="s">'relation object'</span><span class="p">,</span>
                 <span class="s">'actual.object.id'</span><span class="p">,</span>
                 <span class="s">'other.object.id'</span><span class="p">,</span>
                 <span class="s">'Field Name'</span><span class="p">)</span>
</pre></div>
</div>
<dl>
<dt>其中:</dt>
<dd><ul>
<li><p>other.object.name是属于这个关系的其他对象。</p>
</li>
<li><p>relation object做该关系链接的表格</p>
</li>
<li><p>actual.object.id和other.object.id是用于关系表格的字段名称。</p>
</li>
</ul>
</dd>
</dl>
<p>Example:</p>
<div><div><pre>'category_ids':
   fields.many2many(
    'res.partner.category',
    'res_partner_category_rel',
    'partner_id',
    'category_id',
    'Categories'),
</pre></div>
</div>
<p>To make it bidirectional (= create a field in the other object):</p>
<div><div><pre><span class="k">class</span> <span class="nc">other_object_name2</span><span class="p">(</span><span class="n">osv</span><span class="o">.</span><span class="n">osv</span><span class="p">):</span>
    <span class="n">_inherit</span> <span class="o">=</span> <span class="s">'other.object.name'</span>
    <span class="n">_columns</span> <span class="o">=</span> <span class="p">{</span>
        <span class="s">'other_fields'</span><span class="p">:</span> <span class="n">fields</span><span class="o">.</span><span class="n">many2many</span><span class="p">(</span>
            <span class="s">'actual.object.name'</span><span class="p">,</span>
            <span class="s">'relation object'</span><span class="p">,</span>
            <span class="s">'actual.object.id'</span><span class="p">,</span>
            <span class="s">'other.object.id'</span><span class="p">,</span>
            <span class="s">'Other Field Name'</span><span class="p">),</span>
    <span class="p">}</span>
<span class="n">other_object_name2</span><span class="p">()</span>
</pre></div>
</div>
<p>Example:</p>
<div><div><pre><span class="k">class</span> <span class="nc">res_partner_category2</span><span class="p">(</span><span class="n">osv</span><span class="o">.</span><span class="n">osv</span><span class="p">):</span>
    <span class="n">_inherit</span> <span class="o">=</span> <span class="s">'res.partner.category'</span>
    <span class="n">_columns</span> <span class="o">=</span> <span class="p">{</span>
        <span class="s">'partner_ids'</span><span class="p">:</span> <span class="n">fields</span><span class="o">.</span><span class="n">many2many</span><span class="p">(</span>
            <span class="s">'res.partner'</span><span class="p">,</span>
            <span class="s">'res_partner_category_rel'</span><span class="p">,</span>
            <span class="s">'category_id'</span><span class="p">,</span>
            <span class="s">'partner_id'</span><span class="p">,</span>
            <span class="s">'Partners'</span><span class="p">),</span>
    <span class="p">}</span>
<span class="n">res_partner_category2</span><span class="p">()</span>
</pre></div>
</div>
</td>
</tr>
<tr><th>related:</th><td><p>有时候你需要考虑关联中的关联。例如，假设你有这样的对象：City -&gt; State -&gt; Country，你需要从一个城市名得到一个国家名，你可以在City对象中定义:</p>
<div><div><pre>'country_id': fields.related(
    'state_id',
    'country_id',
    type="many2one",
    relation="res.country",
    string="Country",
    store=False)
</pre></div>
</div>
<dl>
<dt>其中:</dt>
<dd><ul>
<li><p>The first set of parameters are the chain of reference fields to
follow, with the desired field at the end.</p>
</li>
<li><p>type是期望字段的类型。</p>
</li>
<li><p>Use <em class="guilabel">relation</em> if the desired field is still some kind of
reference. <em class="guilabel">relation</em> is the table to look up that
reference in.</p>
</li>
</ul>
</dd>
</dl>
</td>
</tr>
<tr>
<td>reference</td>
<td>
<p>引用型，用于selection字段, TODO:搞明白干嘛的</p>
</td>
</tr>
</tbody>
</table>

#### 4.2.3 复杂类型

- function：函数型字段，该类型的字段由函数计算而得，不存储在数据表中(在ORM中可以计算取得)

	```python
	# 格式
	fields.function(fnct, arg=None, fnct_inv=None, fnct_inv_arg=None, type='float', fnct_search=None, obj=None, method=False, store=True)
	```

	- type是函数返回值的类型
	
	- method为True表示本字段的函数是对象的一个方法，False表示全局函数，不是对象的方法

	- fcnt是函数或方法，用于计算字段值。

        ```python
        # 函数应该这么定义
        def fnct(self, cr, uid, ids, field_name, arg, context):
            pass
            # returns a dictionary { ids -> values } with values of type type
        ```

	- fcnt_inv是用于写本字段的函数或者方法

        ```python
        def fnct_inv(obj, cr, uid, id, name, value, fnct_inv_arg, context):
            pass
        ```

	- fcnt_search自定该字段的搜索行为

        ```python
        def fnct_search(obj, cr, uid, obj, name, args):
            pass
            # returns a list of tuples arguments for search(), e.g. [('id','in',[1,3,5])]
        ```

	- store表示是否希望在数据库中存储本字段值，缺省值为False

	> 和`@property`有啥不一样啊

- related: *不小心定义在上面了*

- property：拥有权限的动态属性

    ```python
    fields.property(obj, type='float', view_load=None, group_name=None, ...)
    ```

    - obj: 对象，必须

    - type: 关联字段类型

#### 4.2.4 特殊/默认字段

一些字段会被自动创建，如果被自动创建的字段覆盖时会被忽略

1. id 自动生成id

2. name 字段展示名

3. active 是否活跃，如果为Fasle则默认不显示

4. sequence ：？？？

5. state：该对象的各种状态，用于工作流

6. parent_id：提供了`child_of`的操作

7. parent_left, parnet_right：TODO

8. create_date, create_uid, write_date, write_uid：用于记录日志，如果不需要这个的话设置对象属性`_log_access`为False

### 4.3 ORM基本方法

#### 4.3.1 获取OSV方法

- `self.pool.get('object_name')` 

#### 4.3.2 通用参数

1. cr 数据库游标，数据库链接

2. uid 当前操作用户的id值，这里的id指的是res.user中的id

3. ids 准备执行的记录的id列表

4. context 可选的上下文参数，字典形式

#### 4.3.3 常用方法

1. `search(cr, uid, domain, offset=0, limit=None, order=None, context=None, count=False)` 

    - 返回匹配的id列表

    - domain: 过滤条件

    - offset：可选，忽略某些记录

    - limit：可选，最大的返回数据量

    - order：可选，排序，默认使用`self._order`排序

    > Operators: `=`, `!=`, `>`, `>=`, `<`, `<=`, `like`, `ilike`, `#in`, `not in`, `child_of`, `parent_left`, `parent_right`
    >
    > Prefix operators: `&`, `(default)`, `|`, `!`
    
    ```python
    # Fetch non-spam partner shops + partner 34
    ids = self.search(cr, uid,
                        [ '|', ('partner_id', '!=', 34), '!', ('name', 'ilike', 'spam'),], 
                        order='partner_id' )
    ```

2. `create(cr, uid, values, context=None)`

    - 创建新记录，并返回该新纪录的id

    - values：每一个字段的字典

    ```python
    idea_id = self.create(cr, uid, 
        { 'name': 'Spam recipe',
          'description': 'spam & eggs',
          'inventor_id': 45,
        })
    ```

3. `read(cr, uid, ids, fields=None, context=None)`

    - 返回包含查询字段的字典的列表

    - fields，返回那些字段的数据，默认所有的字段

    ```python
    results = self.read(cr, uid, [1, 2], 
                            ['name', 'inventor_id'])
    print('Inventor:', results[0]['inventor_id'])
    ```

4. `read_group(cr, uid, domain, fields, groupby, offset=0, limit=None, orderby=None, context=None)`

    - 返回包含查询字段的字典的列表，并且做好分类

    - groupby用来分组的字段或者字段的列表

    ```python
    self.read_group(cr, uid, [], ['score'], ['inventor_id'])
    # [{'inventor_id': (1, 'Administrator'), 'score': 23, # aggregated score 'inventor_id_count': 12, # group count
    # },
    # {'inventor_id': (3, 'Demo'),
    # 'score': 13,
    # 'inventor_id_count': 7, }]
    ```

5. `write(cr, uid, ids, values, context=None)`

    - 用给定的id和values来更新记录，返回True

    ```pyrhon
    self.write(cr, uid, [42, 43],
                { 'name' : 'spam' 
                  'parent_id': 24
                })
    ```

6. `copy(cr, uid, id, defaults,context=None)`
    
    - 根据给定的id复制记录并且用defaults来更新它，返回True

7. `unlink(cr, uid, ids, context=None)`

    - 删除给定ids的记录，返回True

8. `browse(cr, uid, ids, context=None)`

    - 将记录当作对象来获取，允许使用点`.`符号来访问对象中的数据，返回的是对象的列表或单个对象

9. `default_get(cr, uid, fields, context=None)`

    - 返回字段的默认值，根据设置的默认值或者context值

10. `perm_read(cr, uid, ids, details=True)`

    - 返回包含每个ids记录的权限字典

    - details：如果是True，`*_uid`字段值会被替换为`(id, name_of_user)`

    - 返回的字典包括：id,`create_uid`,`create_date`,`write_uid`,`weite_date`

11. `fields_get(cr, uid, fields=None, context=None)`

    - 返回字段字典，包含了该字段的一些信息

12. `fields_view_get(cr, uid, view_id=None, view_type='form', context=None, toolbar=False)`

    - 返回描述了view(xml)的字典，包括了继承的视图

    - view_id: 视图的id

    - view_type: 视图的类型

    - toolbar: 如果True, 返回context包含的actions

13. `name_get(cr, uid, ids, context=None)`

    - 返回表示关系（to-many relationships）的元组

14. `name_search(cr, uid, name='', domain=None, operator='ilike', context=None, limit=80)`

    - 返回满足添件的对象名字的列表，用于完善to-many的关系？等同于`search()`on`name`+`name_get()`

    - 不懂

15. `export_data(cr, uid, ids, fields, context=None)`

    - 到处被选择对象的字段，返回一个带有包含`datas`的字典，用于使用客户端导出数据

    - fields：字段名列表

    - context：可能包含`improt_comp`(默认是False)，用于导出兼容`improt_data`的数据

16. `import_data(cr, uid, fields, data, mode='init', current_module='', noupdate=False, context=None, filename=None)`
    
    - 导入数据

> 在内部使用`browse()`在webservice上用`read()`

<br>
<br>
<br>

<span id="view"></span>
## 5. View(xml文件)

**每一个模块元素都是一条数据库记录，比如说menus，views，actions，roles，access rights等**

> 在openerp中，前端代码负责读取数据库中的记录，从而展示出相应的模块，包括权限等等..
>
> 前端代码读取数据库中的模块配置从而显示

### 5.1 xml文件结构

- XML文件的用处有：

    1. 初始化并且准备演示数据

    2. views declaration

    3. reports declaration

    4. wizards declaration

    5. workflows declaration

    6. 等等...

一般来说，xml文件都该这么定义

```xml
<?xml version="1.0" encoding="utf-8"?> <openerp>
    <data>
        <record model="object_model_name" id="object_xml_id">
            <field name="field1">value1</field>
            <field name="field2">value2</field>
        </record>
        <record model="object_model_name2" id="object_xml_id2">
            <field name="field1" ref="module.object_xml_id"/>
            <field name="field2" eval="ref('module.object_xml_id')"/>
        </record>
    </data>
</openerp>
```

每一个record对应着数据库中的一条记录

每一条记录(view, menu, action...)都支持特定的实体和属性，但是所有的都支持以下特殊属性

1. id 这条记录独一无二(每个模块)的外部id

2. ref 不用设置该字段内容，而是使用其他记录的id(也可以跨模块)

3. eval 运行的Python代码作为内容，一般用于True和False的设置

> 注意，外部id和id不一样，外部id用于找到这条记录，而id是这条记录在数据库中的id值

补充：这里的xml结构是通用的xml，不一定是view的xml，view的xml也是相同的结构，modulename_data.xml中可以添加该模块的数据

### 5.2 CVS导入

用于导入数据？TODO，还没用到

还有管理权限的`ir.model.access.csv`

```csv
"id","name","model_id:id","group_id:id","perm_read","perm_write","perm_create","perm_unlink" 
"access_idea_idea","idea.idea","model_idea_idea","base.group_user",1,0,0,0 
"access_idea_vote","idea.vote","model_idea_vote","base.group_user",1,0,0,0
```

### 5.3 菜单和动作

- 一个菜单是一条记录，并且能够被3中方式触发

    - 点击了菜单，它关联了一个动作

    - 点击了视图中的按钮，如果他们关联了动作

    - 作为一个对象的上下文动作(在边栏可见)

#### 5.3.1 定义动作

```xml
<!-- 定义一条记录，一个动作 -->
<record model="ir.actions.act_window" id="action_id"></record>
    <field name="name">action.name</field>
    <field name="view_id" ref="view_id"/>
    <field name="domain">[list of 3-tuples (max 250 characters)]</field> 108 <field name="context">{context dictionary (max 250 characters)}</field> 109 <field name="res_model">object.model.name</field>
    <field name="view_type">form|tree</field>
    <field name="view_mode">form,tree,calendar,graph</field> 
    <field name="target">new</field>
    <field name="search_view_id" ref="search_view_id"/>
</record>
```

说明：

- id：该动作在表格`ir.actions.act_window`中的id，必须是特殊的

- name：该动作的名称

- view_id: 指定某个视图来打开(如果没写的话则使用最高权限的view)

- domain：和`search()`的参数一样，用于过滤view中显示的内容

- context：传递给view的字典

- res_model：该view打开的对象

- view-type：设置view的类型, form用来编辑对象，tree负责展示对象

- view_model: view模式？

- target：设置值为new来创建新的弹窗

- search_view_id：搜索view的id，替换了默认的搜索表格

#### 5.3.2 定义菜单

`<menutiem>`标签是定义`ir.ui.menu`记录的捷径并且将与action通过`ir.model.data`字段中的记录关联

```xml
<menuitem id="menu_id" parent="parent_menu_id" name="label" action="action_id" groups="groupname1,groupname2" sequence="10"/>
```

说明：

- id: 菜单的id，必须特殊

- parent：父外部id

- name：可选的菜单标签，默认为action名

- action: 关联到那个action，action的id

- groups：能看到该菜单的组群列表，如果不填写的话则所有组都能看到

- sequence：排列菜单顺序的优先级（10，20，30...）

<br>
<br>
<br>

## 6 视图和继承

**视图也是一条记录**

可以按照以下的xml来定义一个视图，同一个对象的同样类型的视图也可以形成一定的结构，通过`priority`来确定他们的位置。view也可以继承！

通用视图定义方法

```xml
<record model="ir.ui.view" id="view_id">
    <field name="name">view.name</field>
    <field name="model">object_name</field>
    <!-- types: tree,form,calendar,search,graph,gantt,kanban --> 121 <field name="type">form</field>
    <field name="priority" eval="16"/>
    <field name="arch" type="xml">
    <!-- view content: <form>, <tree>, <graph>, ... --> 125 </field>
</record>
```

说明：

- id：view的id

- name：view的名称

- model：view需要关联的对象，和action中的`res_model`一样

- type：view的类型，有这些类型: `form`, `tree`, `graph`, `calendar`, `search`, `gantt`, `kanban`

- priority：view的优先级，数字越小，优先级越高(默认值为16)

- arch：视图的结构，不同的类型有不同的结构，请看以下类型

### 6.1  Form(用于展示和编辑)

这里又一个定义了form的事例

```xml
<!--放在arch下面-->
<form string="Idea form">
    <group col="6" colspan="4">
        <group colspan="5" col="6">
            <field name="name" colspan="6"/>
            <field name="inventor_id"/>
            <field name="inventor_country_id"/>
            <field name="score"/>
        </group>
        <group colspan="1" col="2">
            <field name="active"/>
            <field name="invent_date"/>
        </group>
    </group>
    <notebook colspan="4">
        <page string="General">
            <separator string="Description"/>
            <field colspan="4" name="description" nolabel="1"/>
        </page>
        <page string="Votes">
            <field colspan="4" name="vote_ids" nolabel="1">
                <tree>
                    <field name="partner_id"/>
                    <field name="vote"/>
                </tree>
            </field>
        </page>
        <page string="Sponsors">
            <field colspan="4" name="sponsor_ids" nolabel="1"/>
        </page>
    </notebook>
    <field name="state"/>
    <button name="do_confirm" string="Confirm" type="object"/>
</form>
```

说明：

- **所有元素**共有的属性：

    1. string：该元素的标签

    2. nolabel：设置为`1`则不现实标签

    3. colspan：该字段占用的列

    4. rowspan：该字段占用的行

    5. col：该元素为其子元素分配的列

    6. invisible：如果设置为`1`则隐藏该元素

    7. eval：执行Python代码作为该元素的内容

    8. attrs：Python map defining dynamic conditions on these attributes: readonly, invisible, required based on search tuples on other field values

一般来说，form中可以写的元素有：

1. field：需要显示的字段

    0. name：确定显示哪个字段 

    1. label：该字段的标签名

    2. nolabel：如果为`1`则隐藏标签

    3. required：view层面的required

    4. readonly：view层面的只读

    5. password：如果为`True`则显示为星号

    6. context：Python代码，一个上下文字典

    7. domain：Python代码，一个包含多个元组的列表，写上限制条件，详见`serach()`方法

    8. on_change：Python代码，定义一个方法，当该字段值改变的时候被调用

    9. groups：能够看到该字段的组，是一个组id的列表

    10. widget：可以选择一个字段的其他小插件(url, email, image, float_time, reference, html, progressbar, statusbar, handle, etc) - 意义不明。。

2. properties：dynamic widget showing all available properties TODO:作用未知

3. button：可点击的控件，能够关联action，他拥有特殊的属性

    1. type: 按钮的类型，`workflow`(默认),`object`,`action`

    2. name：workflow信号，对象的方法名(没有参数)，或者是需要调用的action

    3. confirm：当点击之后显示确认或取消

    4. states：该按钮当前的状态，一个列表

4. separator：水平分割线，有个可选的`string`

5. newline：place-holder for completing the current line of the view

6. label：视图的说明或者图示

7. group：用于给字段分组

8. notebook：notebook是`page`元组的容器

9. page：notebook的内容元组，属性：

    1. name：当前的page的标签

    2. position：在notebook中的位置(inside, top, bottom, left, right)

> 7.0中的新api，如果使用7.0，设置`<form string="Idea form" version="7.0">`这样可以和`xhtml`的一些标签混用，=

### 6.2 动态视图

In addition to what can be done with states and attrs attributes, functions may be called by view elements (via buttons of type object, or on_change triggers on fields) to obtain dynamic behavior. These functions may alter the view interface by returning a Python map with the following entries:

- value：a dictionary of field names and their new values

- domain：a dictionary of field names and their updated domains of value

- warning：a dictionary with a title and message to show a warning dialog

### 6.3  列表和树

```xml
<tree string="Idea Categories" toolbar="1" colors="blue:state==draft">
    <field name="name"/>
    <field name="state"/>
</tree>
```

- tree元素拥有的属性

    1. colors：这样的格式`colors="html颜色: 条件(Python代码)"`

    2. editable：top/bottom 允许在列表中直接修改值

    3. toolbar：set to True to display the top level of object hierarchies as a side toolbar (only for hierarchical lists, i.e. opened with actions that set the view_type to “tree” instead of “mode”)

- tree中允许的元素：field, group, separator, tree, button, filter, newline

### 6.4 看板

TODO

### 6.5 日历

TODO

### 6.6 甘特图

TODO

### 6.7 图表

TODO

### 6.8 搜索视图

TODO

### 6.9 视图继承关系

TODO

<br>
<br>
<br>

## 7. 报表`Reports`

TODO

<br>
<br>
<br>

## 8. 工作流`Workflows`

工作流可能和对象相关联，并且完全的可定制化。

工作流用来搭建和管理业务对象的生命周期以及文档

工作流的`activities`（节点）和`transitions`（转化）一样都是通过xml来定义的，这些都被称为`workitems`。

> 转化就是一个节点到另一个节点，一般来说会有一些条件，详情见transitions

### 8.1 申明一个工作流

应当创建一个`xxxxx_workflow.xml`的文件

**工作流是通过操作对象的`state`字段来实现的**(详见特殊字段的state)

```xml
<record id="wkf_idea" model="workflow"> 
    <field name="name">idea.basic</field> 
    <field name="osv">idea.idea</field> 
    <field name="on_create" eval="1"/>
</record>
```

说明：

1. id：该工作流的id

2. name：工作流名称(必须)

3. osv：工作流所定义的对象（必须）

4. on_create：如果是True，则每一个workitem自动实例化每一条新的osv记录，TODO：怎么个实例化？？

### 8.2 工作流节点

```xml
<record model="workflow.activity" id="''activity_id''">
      <field name="wkf_id" ref="''workflow_id''"/>
      <field name="name">''activity.name''</field>::

      <field name="split_mode">XOR | OR | AND</field>
      <field name="join_mode">XOR | AND</field>
      <field name="kind">dummy | function | subflow | stopall</field>

      <field name="action">''(...)''</field>
      <field name="signal_send">''(...)''</field>
      <field name="flow_start" eval='True | False' />
      <field name="flow_stop" eval='True | False' />
  </record>
```

说明：

1. id：节点id

2. wkf_id：该节点属于哪一个工作流

3. name：节点标签

4. flow_start：如果是True，则该节点为起始节点

5. flow_stop：如果是True，则该节点为结束节点，如果到达了某个结束节点则该工作流完成

6. join_mode：当迁移入该节点后的行为逻辑

    - XOR: 当第一个迁移到来就激活该节点(默认)

    - AND：当所有的迁移完成激活该节点

7. join_split：当迁出该节点时的行为逻辑

    - XOR：由本节点始发的出迁移中，沿着第一个满足迁移条件的迁移跳转，只有一个跳转(默认)

    - OR：由本节点始发的出迁移中，只要满足迁移条件即沿该迁移跳转，有零个或多个跳转

    - AND：表示由本节点始发的出迁移中，只有所有迁移皆满足迁移条件才跳转，而且是同时沿所有迁移跳转，零个或全部跳转

8. kind：当一个节点被激活时进行的操作种类

    - dummy：什么的不做（默认）

    - fucntion：根据action中的指定的动作来执行

    - subflow：表示触发`subflow_id`中指定的工作流

    - stopall：流程到此节点则结束，但结束前仍然会执行action中的代码

9. subflow_id：如果kind是subflow，则使用ref来指定被执行的节点id

10. action：如果kind是`function`或者`subflow`时，指定调用该对象的方法，别忘了更新对象的state字段

    ```python
    def action_confirmed(self, cr, uid, ids): 
        self.write(cr, uid, ids, { 'state' : 'confirmed' }) # ... perform other tasks
        return True
    ```

11. signal_send：执行完action后，往其他的工作流发送信号。

    - 格式为`subflow.*`，subflow_id和siganl_send必须配合使用，subflow_id表示，触发子工作流subflow_id，在该子工作流中，通常必须定义singal_send，signal_send定义父流程中的某个signal，表示子流程处理结束后触发父流程中的信号

### 8.3 工作流迁移

```xml
<record model="workflow.transition" id="transition_id">
  <field name="act_from" ref="activity_id_1"/>
  <field name="act_to" ref="activity_id_2"/>
  <field name="group_id" ref="groupid"/>
  <field name="signal">(...)</field>
  <field name="condition">(...)</field>
  <field name="trigger_model">(...)</field>
  <field name="trigger_expr_id">(...)</field>
</record>
```

说明：

1. act_form/act_to：源节点和目的节点的id

2. signal：触发迁移的信号，如果系统收到信号后，则触发该迁移

    - 最常用的是用户点击的按钮，button中定义的`name=该signal`

    - 调用workflow_service的方法：trg_validate(self, uid, res_type, res_id, signal, cr)，此方法表示，触发对象类型res_type关联的workflow的signal信号，工作流实例关联的对象实例是 res_id

    - 子流程的signal_send发出的信号

3. condition：迁移的条件，是一段Python代码，通常是一个函数调用，当触发信号后会检查此处条件

4. trigger_model/trigger_id：此二字段表示启动一个新工作流实例

    - trigger_model定义对象类型，trigger_expr_id 定义一段Python代码，返回trigger_model类型的对象id

5. role_id：reference to the role that user must have to trigger the transition

6. group_id：表示只有该权限组可以触发本迁移

<br>
<br>
<br>

## 9. 权限

### 9.1 组

创建组相当于在res.groups中创建记录

- 一般在`/security/xxxx_security.xml`中定义新的组

    ```xml
    <record id="ask_for_leave_employee" model="res.groups">
        <field name="name">employee</field>
        <field name="category_id" ref="base.module_category_human_resources"/>
    </record>
    ```

    - category_id表示该组属于哪一个模块，这里的`base.module_category_human_resources`指代的是在`base`模块下某个xml记录
    
    > 实际上是`openerp/addons/base/module/module_data.xml`中可以找到该记录，代表的就是hr模块，data.xml表示这个初始化时创建的数据

- 还可以在该文件中设置规则

    ```xml
    <record model="ir.rule" id="afl_employee_rule">
        <field name="name">rule_employee</field>
        <field name="model_id" ref="model_afl_ask"/>
        <field name="domain_force">[('applier', '=', user.id)]</field>
        <field name="groups" eval="[(4,ref('ask_for_leave_employee'))]"/>
    </record>
    <!--注意这里的groups字段是多对多关系哈！应当在关系表中查看--!>
    ```

> eval说明，因为eval是Python代码，所以id前记得加ref，是不是多对多中才会用到
>
> (4,ID)添加主从关系到id=ID的对象
>
> (3,ID)去除和id=ID的对象主从链接关系,但是不删除这个对象
>
> (2,ID) 去除和id=ID的对象主从链接关系,并且删除这个对象（调用unlink方法）
>
> (5) 去除所有的链接关系,也就是循环所有的从数据且调用(3,ID)
>
> (6,0,[IDs]) 用IDs里面的记录替换原来链接的记录，即先执行(5)再循环IDs执行（4,ID）

有了权限组，就可以执行权限了，权限有

1. 菜单级别权限

    - 在定义菜单`<menuitem>`时可以定义那些组有权看到，当然，这只是不显示而已，输入正确的网址还是可以访问的，因此我们需要**对象级别的权限**

2. 对象级别的权限
    
    - 可以用`/security/ir.model.access.csv`文件来确定

    ```cvs
    "id","name","model_id:id","group_id:id","perm_read","perm_write","perm_create","perm_unlink" 
    "access_idea_idea","idea.idea","model_idea_idea","base.group_user",1,1,1,0 
    "access_idea_vote","idea.vote","model_idea_vote","base.group_user",1,1,1,0
    ```

3. 工作流级别权限

    - 在工作流迁移中指定groups_id

4. 字段级别权限

    - 在定义orm对象时使用group参数来确定

### 9.2 角色(Roles)

角色在res.roles中定义，只用于工作流迁移（设置role_id）


<br>
<br>
<br>

## 10. Wirzard


<br>
<br>
<br>

## 11. WebService - XML-RPC

XML-RPC是第三方和OpenERP交互的借口(应当与restful平级)

```python
import xmlrpclib
# ... define HOST, PORT, DB, USER, PASS
url = 'http://%s:%d/xmlrpc/common' % (HOST,PORT) sock = xmlrpclib.ServerProxy(url)
uid = sock.login(DB,USER,PASS)
print "Logged in as %s (uid:%d)" % (USER,uid)
# Create a new idea
url = 'http://%s:%d/xmlrpc/object' % (HOST,PORT) sock = xmlrpclib.ServerProxy(url)
args = {
'name' : 'Another idea',
'description' : 'This is another idea of mine', 'inventor_id': uid,
}
idea_id = sock.execute(DB,uid,PASS,'idea.idea','create',args)
```

<br>
<br>
<br>

## 12. 优化建议

As Enterprise Management Software typically has to deal with large amounts of records, you may want to pay attention to the following anti-patterns, to obtain consistent performance:

- Do not place browse() calls inside loops, put them before and access only the browsed objects inside the loop. The ORM will optimize the number of database queries based on the browsed attributes.


- Avoid recursion on object hierarchies (objects with a parent_id relationship), by adding parent_left and parent_right integer fields on your object, and setting _parent_store to True in your object class. The ORM will use a modified preorder tree traversal to be able to perform recursive operations (e.g. child_of) with database queries in O(1) instead of O(n)

- Do not use function fields lightly, especially if you include them in tree views. To optimize function fields, two mechanisms are available:
	
	- multi: all fields sharing the same multi attribute value will be computed with one single call to the function, which should then return a dictionary of values in its values map
	
	- store: function fields with a store attribute will be stored in the database, and recomputed on demand when the relevant trigger objects are modified. The format for the trigger specification is as follows: store = {'model': (_ref_fnct, fields, priority)} (see example below)

```python
def _get_idea_from_vote(self,cr,uid,ids,context=None): 
	res = {}
	vote_ids = self.pool.get('idea.vote').browse(cr,uid,ids,context=context) for v in vote_ids:
	res[v.idea_id.id] = True # Store the idea identifiers in a set return res.keys()
def _compute(self,cr,uid,ids,field_name,arg,context=None): 
	res = {}
	for idea in self.browse(cr,uid,ids,context=context): 
		vote_num = len(idea.vote_ids)
		vote_sum = sum([v.vote for v in idea.vote_ids]) res[idea.id] = {
		'vote_sum': vote_sum,
		'vote_avg': (vote_sum/vote_num) if vote_num else 0.0, }
		return res
	_columns = {
	# These fields are recomputed whenever one of the votes changes
	'vote_avg': fields.function(_compute, string='Votes Average',
	store = {'idea.vote': (_get_idea_from_vote,['vote'],10)},multi='votes'),
	'vote_sum': fields.function(_compute, string='Votes Sum',
	store = {'idea.vote': (_get_idea_from_vote,['vote'],10)},multi='votes'),
```