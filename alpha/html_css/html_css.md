
----------------------------HTML
WEB
    1. 什么是Web : 网页
        网页是一种基于B/S模式的应用程序
        B/S ： 浏览器与服务器交互模式 (Browser / Server)
        C/S :  客户端与服务器交互模式 (Client / Server)

        多个网页组成网站
    
    2.Web 的组成
        1.浏览器 : 代替用户向服务器发送请求，解析数据并呈现
        2.服务器 : 接收用户请求并响应
        3.通信协议 ： http / https / ftp / file ...
           规范数据在网络中是如何打包和传递的
           http  ： 超文本传输协议
           https ：加密的超文本传输协议
        
    3.Web 服务器
        1.作用：
            1.存储数据
            2.接收请求并响应
            3.具备安全性功能
        2.产品：
            1.Apache 阿帕奇
            2.Tomcat 汤姆猫
            3.IIS    微软  Internet Information Service
            4.Nginx 
            ......
    
        3.技术
            1.JSP - Java Server Pages (Java 服务器页面)
            2.PHP
            3.ASP.net  
            4.Python Web    (Flask Django)
    
    4.浏览器
        1.作用
            1.代替用户向服务器发送请求，也叫用户代理 user agent
            2.作为响应数据的解释引擎，向用户呈现图形化界面
        2.产品
            1.Google chrome - Webkit(内核)
            2.Opera Opera 
            3.Mozilla FireFox
            4.Apple Safari - Webkit(内核)
            5.Microsoft IE 、 Edge
            浏览器内核(引擎):
              1.渲染引擎：解析 HTML CSS,控制页面的渲染效果
              2.JS 引擎 ：解析JS脚本
        3.技术
            1.HTML
            2.CSS
            3.JS
            4.前端框架 (Angular / Vue / Node.js / React...)

HTML 概述
    什么是HTML : HyperText Markup Language   超文本标记语言

        1.超文本 
            网页中一切的内容：文本，图片，音视频等
    
        2.标记
            也叫标签或元素：主要用来标记网络中的内容，结合CSS实现网页的布局和排版
    
    HTML 在计算机中的表现
        所有的网页都是HTML格式的文件
        文件后缀使用 .html / .htm 表示
    
    运行工具
        浏览器, 使用chrome 作为默认浏览器
    
    调试工具
        浏览器自带的调试工具 (开发者工具)，使用F12打开或者右键检查

HTML 语法
    HTML 是标签语法，标签以<> 为标志

       分类 ：1.单标签
                只有开始标签，没有结束标签
                语法：
                    1.<标签名>
                    2.<标签名/>
             2.双标签
                又开始标签，有结束标签，成对出现
                语法：
                    <标签名>标签内容</标签名>
        标签的嵌套
            1.在双标签中嵌套使用其他标签，都是嵌套结构
            2.外层元素称为父元素，内层元素称为子元素
            3.多层嵌套结构中，外层元素称为祖先元素，内层元素为后代元素
    
    HTML 语法规范  非常宽松
        1.HTML 标签不区分大小写的，BODY Body body 标签可以大写，推荐小写
        2.在涉及标签嵌套时保持内部标签适当缩进，增加代码可读性
        3.添加适量注释
    
    HTML 的注释
        语法： <!--  注释内容  -->
    
        1.HTML 的注释不能嵌套
        2.标签名中不能嵌套使用注释

文档基本结构
    1.<html></html>标签，表示文档的开始和结束，
        网页中所有的内容都必须写在html标签中

    2.<head></head>标签，表示网页的头部内容，
            设置网页的标题，字符集，引入外部文件等
            <title>WeiTianHua</title>
            <meta charset="utf-8">
    
    3.<body></body>标签，表示网页的主体内容，所有呈现在网页窗口中的内容，
        都应该写在body标签中
    
    4.标签属性
        标签属性用来修饰或补充当前的标签内容
        语法 :  <标签名 属性名="属性值"></标签名>
            每个标签中都可以添加一个或多个标签属性，多个属性之间使用空格隔开


HTML常用标签
    文档类型声明
        <!doctype html>
        对当前的文档类型及版本做出指定(这种声明方式是HTML5的声明方式)
        关系到页面元素的渲染效果 CSS
        书写到<html>之前，文档开篇


    设置网页的标题，字符集，和选项卡图标
        <meta charset="utf-8" />
        <title>WeiTianHua</title>
        <!-- 头图片链接  rel=大小类型  href=路径 type=进一步说明图片类型-->
        <link rel="shortout icon" href="201_1440x900.jpg" type="image/x-icon">
    
    标题标签
        <h1>一级标题</h1>
        ...
        <h6>六级标题</h6>
      标题标签的内容，与普通文本相比，自带文本加粗效果
      从 h1 ~ h6 字体大小逐渐减小
    
    常用文本标签
        1.段落标签,自占一行
            <p>标签内容</p>
        2.<span>行分区标签</span>
        3.<label>文本标签</label>
        4.<b></b> <strong></strong> 加粗标签
            h5之后推荐使用有语义标签 strong 表示强调
        5.<s></s> 删除线
        6.<i></i> 斜体显示
        7.<u></u> 为文本添加下划线
        8.上下标 标签
            上标: X<sup>2</sup>
            下标: X<sub>1</sub>
    
    字体实体
        1.HTML文档中会忽略多余的空格和换行，只显示为一个空格
        2.针对HTML文档的特殊性，比如对空格，<>的处理，需要采用
            特殊的语法表示空格和<>等其他符号
    
            空格 ：    &nbsp; 表示一个空格
            <  :      &lt;  less than 表示 <
            >  :      &gt;  greater than 表示 >
            版权符号:  &copy;  
            ￥  :     &yen;  表示人民币符号
    
    格式标签
        换行标签 : <br>
        水平线标签 : <hr>

标签的分类
    1.行内元素
        可以与其它元素共行显示 : span  b  strong  label  i  s  u  sub  sup ...
    2.块级元素
        独占一行，不与其它元素共行
            h1~h6  p  div  

列表标签
    列表: 一种结构，将数据按照从上到下进行排列显示
    分类 :
        1.有序列表 (ordered list)
            按照数字或字母依次标记每一条数据
            语法：
                 <ol></ol>
                列表项标签 (list item)
                 <li></li>
                每一个 li 元素都标识一条列表项
            e.g
                <ol>
                    <li></li>
                </ol>

            标签属性：有序列表默认使用数字标识列表项，从1开始
                    也可以在ol标签中添加属性进行设置
                    1.type 属性
                        指定项目符号的类型
                        可取的值 : 1 a A i I
                            希腊数字 : i ii  iii  iv v vi ...
    
                    2.start 属性
                        指定从第几个项目符号开始标识数据
                        取值 : 无单位的数字
    
        2.无序列表 (unordered list)
            语法 :
                <ul>
                    <li></li>
                <ul>
            属性 : 默认情况下，无序列表以实心圆点标识列表项
                    可以通过属性修改
                1.type 属性 : 指定项目符号类型
                  取值 : disc(默认)  square(实心正方形) circle(空心圆) none
    
        3.自定义列表
            语法:
                <dl>
                    <dt>订单跟踪<dt>
                    <dd>物流查询</dd>
                    <dd>联系客服</dd>
                    ...
                    <dt>加入我们<dt>
                    <dd>门店查询<dd>
                    ...
                </dl>
    
        4.列表的嵌套
            列表标签 ol / ul 中除了可以嵌套 li 元素外还可以嵌套其它元素
            下拉菜单
                结构: 我的电脑
                            桌面
                                文件夹1
                                文件夹2

图形与超链接
    1.URL  (Unifrom Resource Locator 统一资源定位符)
        俗称路径 : 有本地路径 ，网络路径

        组成 : 完整的URL: 由 协议 域名 文件目录 文件名组成
    
        分类 :
            1.绝对路径
                从根目录开始逐级查找，直到找到文件名
                通常用于网络资源文件
    
            2.相对路径
                从当前所在的目录文件夹开始查找
                可以使用 ../.. 的形式
    
    2.图片标签
        1.语法：
            <img src='url'>  
            在网页中插入一张图片 ，默认按原始尺寸
        标签属性
            1. width : 取px为单位的像素值，设置图片宽度
            2. height : 取像素值，设置图片的高度
            3. title : 用来设置鼠标悬停与图片上时的显示文本
            4. alt : 当图片加载失败时显示的文本
    
    3.超链接标签
        1.什么是超链接 
            能够实现文件跳转的文本，叫超链接文本
    
        2.使用超链接
            1.语法
                <a href="链接地址">超链接文本</a>
            注意：
                1.href 属性是必填项，省略的话，超链接文本和普通文本一样
                2.网络路径必须加协议
                3.本地文件可用
            2.特殊取值
                ""  :  表示连接至本页面，包含刷新操作
                "#" :  链接至本页的锚点位置，不刷新(做页面目录)
                "javascript:void(0)" : 链接至本页不刷新
    
            3.标签属性
                target : 设置目标文件的打开方式，默认在当前窗口打开，覆盖原文本
                 取值:  _self  默认值
                       _blank  新建页面窗口打开
                
                text-decoration: none; 取消下划线(CSS)
            a标签不能继承外部元素颜色，要单独设置
    
        3.使用锚点链接
            1.通过定义锚点，实现跳转至指定文件的指定位置
            2.使用：
                1.定义超链接，链接到本页的指定位置
                2.在页面相应位置添加锚点
                    <a href="#7">7.条目</a>
                    <a name="7"></a>锚点定位，不显示内容
                在其他文件中，跳转至指定文件指定位置
                    <a href="11.9.3.html#7">跳转至11.9.3.html</a>
                使用name属性定义锚点名称，超链接的链接地址中使用#表示连接至本页，
                跟上锚点名称，表示跳转至锚点位置
            
                图片超链接      
                    <a href=">
                        <img src="">
                    </a>

表格标签
    1.语法 :
        1.<table></table> 表示表格标签
        2.<tr></tr> 表示表格中的一行  table row
        3.<td></td> 表示行中的一个单元格  table data
        4.<th></th> 同单元格，自带文本加粗居中效果
        e.g
            <table>
                <tr></tr>
                    <td></td>
                    <td></td>
                    <td></td>
                <tr></tr>
                    <td></td>
                    <td></td>
                    <td></td>
                <tr></tr>
            </table>
    2.表格的标签属性
        1.table 标签属性 表
            border : 为表格设置边框,取像素值px
            width / height : 设置表格的宽高大小，取像素值，默认内容自适应 
            bgcolor : 表格的背景色设置，取英文颜色单词
            align : 设置表格在父元素中的水平对齐方式
                取值: left(默认左对齐)/ center / right
            cellspacing : 设置单元格与单元格之间的距离 取像素值
            cellpadding : 设置单元格内容与单元格边框之间的距离
        2.tr 标签属性 行
            bgcolor : 行的背景色设置，取英文颜色单词
            align : 设置每一行单元格的内容的水平对齐方式
                取值: left(默认左对齐)/ center / right
            valign : 设置每一行单元格的内容垂直对齐方式
                取值 : top / middle(默认) / bottom

        3.td 标签属性  格
            width / height : 设置单元格的宽高大小，取像素值
            align : 设置单元格的内容的水平对齐方式
                取值: left(默认左对齐)/ center / right
            valign : 设置单元格的内容垂直对齐方式
                取值 : top / middle(默认) / bottom 
            bgcolor : 单元格的背景色设置，取英文颜色单词
    
    3.单元格合并，只作用域td标签
        单元格合并涉及表格结构的调整
        1.跨列合并
            属性 : colspan
            取值 : 无单位的数值，表示跨几列
        2.跨行合并
            属性 : rowspan
            取值 : 无单位的数值，表示跨几行
        注意:
            1.跨行和跨列是单元格的操作，所以属性是单元格td的属性
            2.一旦发生单元格合并，要删除多余的单元格
                跨列合并：
                    影响当前行中单元格的数量，删除当前行中多余单元格
                跨行合并：
                    影响其后行中的单元格数量，需要删除后面行中的单元格
                
    4.表格行分组
        表格在浏览器中渲染时会自动的添加结构标签
        表格可以分为 thead tfoot tbody 三部分
        用于CSS动态添加表格记录时分组操作
        1.thead 
            <thead></thead> 标签用来划分表头
            表头中可以有若干行组成
            <thead>
                <tr>
                    <td></td>
                </tr>
            </thead>
        2.tfoot
            <tfoot></tfoot>用于划分表尾，由若干行组成
        3.tbody
            <tbody></tbody>用于划分表格主体，默认情况下所有的行会自动加入tbody
        注意:
            如果涉及在HTML代码中完整书写分组标签，建议按照此顺序
            <thead></thead>
            <tfoot></tfoot>
            <tbody></tbody>

表单
    作用:用来接收用户的数据并提交给服务器
    表单二要素
        1.表单元素  <form></form>
        2.表单控件
            提供一系列可视化的组件，能够实现跟用户的交互
            如 : 输入框，按钮，文件上传
    
    表单元素
        1.标签
            <form></form> 用来提交数据到服务器，表单控件都应写在此标签中
        2.标签属性
            method : 用来设置数据提交方式 
                取值: get(默认)  1.数据会以参数的形式拼接在url后面
                                2.是明文提交，安全性较低
                                3.最大提交数据2kb
                      post     1.数据会打包在请求头中                    
                               2.隐式提交，安全性较高
                               3.没有数据大小限制
            action  : 必填，指定数据的提交地址
            enctype : 指定数据的编码方式
                提供的类型有：
                    1.application/x-www-form-urlencoded(默认)
                    将表单中是数据装换成字符串格式(name=ss,&pwd=123)
                    附加在url后面，使用?与url隔开
                    2.multipart/form-data
                        专门用来上传特殊类型的 如: 图片，文件，mp3...
                        数据的提交方式必须是post
                    3.text/plain
                        数据以纯文本形式编码，不含任何控件和格式字符
    
    表单控件
        1.表单控件的数据只有放在表单元素中才可以被提交
        2.分类
        输入框
            文本框和密码框
               文本框 : <input type="text">
               密码框 : <input type="password">
            标签属性
                1.type 指定控件类型
                2.name 指定控件名称，缺少无法提交
                3.value 指定控件的值，可以通过 js 动态获取
                4.maxlength 指定最大输入字符数
                5.placeholder 设置提示文本
                6.autocomplete 设置是否自动补全 on/off  
    
        单选按钮和复选框
              语法: 单选按钮 : <input type="radio">
                   复选框  : <input type="checkbox">
              标签属性
                 name 定义控件名称
                    一组的按钮控件名称必须保持一致
                 value 定义控件的值
                    最终将发送给服务器，按钮的value属性必须指定
                 checked
                    表示默认选择当前按钮
            按钮特殊用法
                label for id   将按钮文本与按钮控件绑定在一起，实现点击等价
                使用: 
                    1.使用<label></label>标签包裹按钮文本
                    2.为按钮控件添加id属性，属性值自定义
                    3.为label标签添加for属性，属性值与控件的id保持一致，实现绑定 
    
        隐藏域和文件选择框
            1.隐藏域
               需要提交给服务器，但是不需要呈现给用户的内容
               例如:用户的 ID
            语法:
                <input type="hidden" name="uid" value"001">
                name 定义控件名称, value 设置控件的值，都是必填项
    
            2.文件选择框
                语法：  <input type="file" name="">
                涉及二进制数据提交，文件，图片，mp3 需要设置form enctype属性，
                指定数据的提交方式为post
    
        下拉选择框
            <select name="address">
                <option value="beijing">北京</option>
                <option value="shanghai">上海</option>
            </select>
            第一个位预选中
                预选择选项  selected
    
        文本域，可以多行输入
            语法: <textarea name="uinfo"></textarea>
            标签属性:
                cols :  指定文本域默认宽度，宽度是通过列数控制的
                        以英文字符为准，中文减半
                rows :  指定文本域行数
            特点 : 文本域的大小可以由用户调整
        
        按钮
            分类:
            1.提交按钮: 点击表单数据发送给服务器
                <input type="submit" value=''>
                value 属性是设置按钮的显示文本
            2.重置按钮: 点击时，会将表单数据还原成默认状态
                <input type="reset" value"">
            3.普通按钮: 绑定自定义事件
                <input type="button" value=""> 
            4.<button>按钮显示文本</button>
                1.按钮标签，可以在HTML中任意地方使用，需要绑定自定义事件
                2.如果按钮标签放在form标签中使用，默认具备提交功能，等于submit

使用JS
    在HTML文档中引入JS代码，有三种方式
        1.通过元素绑定事件的方式引入JS代码
          语法:
            <元素 事件函数名="JS代码语句">
            事件函数:
                鼠标单击事件 onclick
        JS代码：
            弹框显示信息 alert('文本');
            控制台输出信息 console.log('文本');
        2.通过脚本标签<script></script>书写JS代码，标签内容为JS代码，
            可以在任意位置书写任意多次。
          注意: 浏览器遵循从上到下执行代码，书写位置可能会影响效果
        JS代码语句:
            1.prompt('');带有输入框的弹框，可用来接收用户输入
            2.document.write(''); 在网页中写入内容
            使用: 
                1.普通的书写方式，按照从上到下的执行顺序，依次在
                  网页的相应位置插入内容，可以识别标签
                2.如果以元素绑定事件的方式，在页面中写入内容，相当于重写页面

外部的JS文件
    1.创建外部的.js文件
    2.在HTML文档中使用<script src="url"></script>引入
    3.如果<script></script>做外部文件的引入操作，标签内部就不能再写JS代码

--------------------------------CSS


                         CSS

CSS :Cascading Style Sheet 层叠样式表
    作用 : 调整页面元素的显示外观，实现网页布局
    使用 : 在HTML文档中使用CSS样式表

使用方式:
    1.内联样式/行内样式
        特点：在标签中通过style属性，为元素设置样式
        语法：
            <标签名 style="属性:值;属性2:值2;..."></标签名>
        CSS中使用属性和值来声明样式

      常用的CSS属性
        font-size 设置元素的字体大小，取像素值
        color 设置元素的字体颜色，取颜色值
        background-color 设置元素的 背景颜色，取颜色值
    
    2.文档内嵌
        特点: 在文档中使用<style></style>标签，为文档中的元素设置样式
        语法:
                <style type="text/css">
                选择器{
                    属性:值
                    属性2:值
                    ...
                }
                </style>
        选择器 : 用来匹配文档中的元素并为其设置样式
        et :
            p{
                color:red;
                font-size:32px
            }
        通过标签名匹配文档中所有的该元素，叫标签选择器
    
    3.外链
        特点 : 在HTML文档中引用外部的样式表文件
        使用 :
            1.定义外部的样式表文件 以.css为后缀
            2.在HTML文档中使用
            <link rel="stylesheet" href="url" type="text/css">

样式表的特征：
    1.层叠性
        可以为一个元素设置多个样式，共同起作用
    2.继承性
        子元素可以继承父元素或祖先元素的某些CSS样式
        例如: 大部分的文本属性都可以被继承
                块元素默认宽度与父元素保持一致 h1 p div
    3.样式表的优先级
        从高到低依次为:
            1.行内样式(最高)
            2.文档内嵌样式/外链文件中的样式(平级):以代码书写顺序为准,后执行起作用
            3.继承样式(子元素继承的父元素样式)
            4.浏览器默认样式
        如果发生样式冲突，参考优先级决定元素最终样式

选择器：
    选择器作用:根据不同的选择器，匹配文档中相应的元素，并为其设置样式

    选择器的分类:
        1.标签选择器
            作用:根据标签名匹配文档中所有的该元素
            语法:
                标签名{
                    属性:值;
                }
    
        2.id 选择器
            根据元素的id属性值匹配元素
            注意: 所有的元素都有id属性，属性值自定义
                  id属性具有唯一性
            语法:
                #id属性值{
                    样式
                }
                e.g:
                    #box{
                        width: 200px;
                        heigth: 200px;
                        background-color:red;                   
                    }
    
                    <div id="box"></div>
        
        3.class 类选择器
            根据元素的class属性值匹配元素，可以复用
            以同名的类为单位统一设置样式
            语法: 
                .class属性值{
                    样式
                }
    
            特殊用法
                1.标签选择器与类选择器结合使用   
                    标签名.类名{
                        样式
                    }
                    标签名必须放在前面
                2.class 属性值可以出现多个，使用空格隔开
                e.g:
                        class="c1 c2 c3"
    
        4.群组选择器
            可以为一组元素设置共同样式,可以组合标签，类，ID选择器
            语法:
                选择器1，选择器2，选择器3{
                    样式
                }
            常见于清除浏览器的默认样式，或设置网页的基本样式
    
        5.后代选择器:
            特点: 匹配满足要求的所有后代元素
            语法: 
                选择器1 选择器2{
                    样式
                }
                选择器1表示父元素
                选择器2表示子元素或后代元素，包含直接间接后代元素
    
        6.子代选择器
            只匹配父元素中的直接子元素
            语法:
                选择器1>选择器2{
                    样式
                }
        
        7.伪类选择器
            作用: 针对元素不同的状态，设置不同的样式,必须和其它选择器一起使用
            分类:
                1.超链接伪类选择器
                    针对超链接不同状态设置样式
                
                2.动态伪类选择器
                    所有元素都可以使用
    
            超链接伪类选择器使用,超链接独有
                1.访问前  :link
                2.访问后  :visitek
                伪类选择器需要与其它选择器结合使用，不能单独使用
                a:link{
                    设置超链接访问之前的样式
                }
    
            动态伪类选择器,所有元素都可用
                1. :hover
                    鼠标滑过元素时的状态
                2. :active
                    鼠标点按元素时的状态,激活
                超链接使用注意:
                    1.超链接可以设置四种状态的样式，
                      书写时必须按以下顺序定义
                            :link
                            :visitek
                            :hover
                            :active
                    2.网络中一般会直接对a标签设置默认样式，
                      配合:hover改变超链接文本色或背景色
                3. :focus
                   表示文本框或密码框在获取焦点时的状态
                   焦点状态: 正接受输入或编辑时的状态
                   input:focus{
                       样式
                   }
                4  :checked  表示表单控件-按钮的选中状态
                
        属性选择器 : 根据属性名和属性值匹配元素
            [type="text"]{
                
            }
    
    选择器的优先级
        选择器的优先级看权重(值),权值越大，优先级越高
    
        基础选择器的权值
          标签选择器   1
          类选择器/伪类选择器  10
          ID选择器       100
          行类样式     1000
        
        组合选择器
          除了群组选择器，其他的选择器权值由各选择器的权值相加得到
            div span{   2
                color:red;
            }
            span{   1
                color:green;
            }
            .d1 .c1{    20
    
            }

尺寸与颜色单位
    尺寸属性：
        1.属性 : width heigth
        2.单位 : 1. px 默认单位，表示像素
                2. % 百分比单位，参照父元素对应属性的值获取尺寸
                -----------
                3.cm 厘米
                4.mm 毫米
                5.pt 磅 1pt = 1/72in
                6.in 英寸 inch 1英寸 = 2.54cm
                -----------
                7. em 默认情况下  1em = 16px
                8. rem 与字体大小相关

    颜色取值:
        1. 英文单词表示颜色
        2. rgb(r,g,b);
            使用红绿蓝三原色表示，每种颜色取值范围0~255
            red    rgb(255,0,0)
            green  rgb(0,255,0)
            blue   rgb(0,255,0)
            black  rgb(0,0,0)
            white  rgb(255,255,255)
    
        3.rgba(r,g,b,a)
            a  表示alpha 透明度 ， 取值0-1
            0  表示透明  1 表示不透明
            使用小数表示半透明 0.5 或 .5
    
        4. 十六进制来表示颜色
           语法:  取值范围  0~9,a~f
                 表示颜色 : 以#开头，每两位为一组，代表一种三元色
                 e.g:
                    rgb(255,0,0) -- #ff0000
                    green           #00ff00
                    blue            #0000ff
            短十六进制:
                由三位组成，每一位表示一种三元色,浏览器会自动重复补充为6位十六进制
                #f00 - #ff0000
    
        font-weight     字体粗细程度
        text-decoration 设置文本装饰线


HTML 元素的分类及特点
    块级元素
        1.独占一行，不与其它元素共行显示
        2.可以手动设置宽高
        3.默认宽度与父元素保持一致(table除外)
    
        常见块级元素:  boyd, h1~h6 , p , div , ul, table td, form
    
    行内元素    
        1.可以与其它元素共行显示
        2.默认尺寸由内容多少决定，不能手动设置宽高】
    
        常见的行类元素: span  label  i  b  strong  sub  sup  a
    
    行内块元素
        1.可以与其它元素共行显示
        2.可以手动设置高宽
    
        常见的行内块元素 : img  表单控件

HTML 标签嵌套
    1.块元素中可以嵌套任何类型元素
        段落标签只能放行内元素和行内块元素(放块元素会两边自动补全)

    2.行内元素只能嵌套行内(块)元素(放块元素高版本浏览器不会报错)

内容溢出
    块元素是可以手动设置高宽的，如果内容超出尺寸范围，如何处理？
    属性 : overflow
    取值 : visible 默认值，表示溢出内容可见
           hidden  溢出内容隐藏
           scroll  为元素添加水平和垂直方向上的滚动条，不管内容有无溢出
           auto    在溢出方向添加可用的滚动条

边框
    CSS中认为所有的元素都是矩形区域
    边框是围绕元素内容出现的线条样式

	1. 边框实现 ：
			属性 ： border
			取值 ：	border-width border-style border-color
				边框宽度，样式，颜色，三个值缺一不可（即使有些值具有默认值）
				border-width : 取像素值，设置四个方向边框宽度
				border-style : 边框样式
					取值 ：
						solid  实线边框
						dashed 虚线边框
						dotted 点线边框
						double 双线边框
				border-color : 设置边框颜色，取颜色值
			注意 ：
				1. 使用border属性为元素设置边框，是同时设置
						上 右 下 左四个方向的边框
				2. 取消默认边框，border : none; (常用于按钮)
	2. 单边边框的设置：
			属性 ：
				1. border-top : 设置顶部边框
				2. border-right : 设置右边边框
				3. border-bottom : 设置底部边框
				4. border-left : 设置左边边框
			取值 ：border-width border-style border-color
	
	3. 网页三角标制作 ：
			1. 设置空的块元素，宽高为0
			2. 为元素设置等宽的边框
			3. 调整边框颜色，显示一个方向的边框，其余边框设置透明边框色 transparent
			注意 ：四个方向的边框缺一不可，缺少的话，边框会
			        恢复成矩形边框，不再是三角形
	
	4. 轮廓线
			属性 ：outline
			取值 ：width style color
			注意 ：轮廓线围绕在元素内容区域四周，与边框类似，
							但有区别 ：轮廓线在网页中不占位，边框
							在网页中是实际占位的
			取消轮廓线 ：outline:none;
	
	5. 圆角边框
			1. 属性 ：border-radius
			2. 取值 ：像素值或者百分比
											上   	右
											左   	下
				1. border-radius:20px;
						一个值表示四个角都以20px做圆角
				2. border-radius:20px 40px;
						取两个值，按照上右下左顺时针方向设置圆角，
						从左上角开始依次取值，在给两个值的情况下，
						上下保持一致，左右保持一致
				3. border-radius:10px 20px 30px;
						取三个值，缺少的第四个值与第二个值保持一致
				4. border-radius:10px 20px 30px 40px;
						分别设置四个角的圆角程度
			3. 百分比取值实现元素形状改变
				border-radius:50%;
				注意 ：使用百分比设置圆角边框时，是参照当前
					元素的尺寸进行计算的
					四个角不能同时超过50%,两个角不能同时超过100%
				如果元素本身的长方形，设置四个50%的圆角会变成椭圆
				如果元素本身是正方形，会变成正圆
	
		6. 盒阴影
			为元素添加阴影效果
			属性 ：box-shadow
			取值 ：offset-x offset-y blur spread color
				1. offset-x : 阴影的水平偏移距离，取像素值
				2. offset-y : 阴影的垂直偏移距离，取像素值
				3. blur : 阴影的模糊程度，取像素值，值越大越模糊
				4. spread : 阴影的延伸距离（可选），取像素值，可以扩大阴影的范围
				5. color : 设置阴影颜色 （默认为黑色）
	
			浏览器的坐标系:
				不管是浏览器窗口中还是元素本身，都存在坐标系，
				默认以左上角为原点(0,0)，向右，向下分别代表X和Y轴的正方向
				正值代表正方向，负值代表负方向

盒模型 （框模型）
	1. 在CSS中，认为一切元素都是框，都是矩形区域
			盒模型 ：计算元素在文档中的实际占位情况
			盒模型组成 ：margin (外边距) border (边框)
						padding(内边距) content(元素的宽高尺寸)
			元素在文档中实际尺寸的计算 ：
			标准盒模型 ：
				最终宽度=左右外边距+左右边框+左右内边距+width
				最终高度=上下外边距+上下边框+上下内边距+height
			其它盒模型元素尺寸计算(表单元素):
				元素设置的宽高表示包含内容内边距和边框在内的总宽度或总高度
				最终宽度 = width + 左右外边框
				最终高度 = height + 上下外边距
		属性
			box-sizing		调整元素最终尺寸的计算方式
			默认 content-box (标准计算方式)
				border-box ： 元素的width/height属性指定的是包含边框在内的区域大小


	2.外边距	
		元素边框与其他元素边框之间的距离
	
		属性 margin
	
		2. 取值 ：像素值
				1. margin : 10px;
						表示设置上右下左四个方向都为10px的外边距
				2. margin: 10px 20px;
						表示上下外边距为10px,左右外边距为20px;
				3. margin: 10px 20px 30px;
						表示上右下左四个方向上的外边距分别为：
						10px 20px 30px 20px;
				4. margin: 10px 20px 30px 40px;
						分别设置四个方向的外边距
	
			特殊取值 
				1. margin : 0; 设置元素外边距为0，常用于初始化页面
					样式，取消一些元素的默认外边距
				2. margin : 0 auto; 设置左右外边距自动，用来实现元素
					的居中效果。auto只对左右外边距起作用
				3. 取负值 ：
						会移动元素的位置，负值表示向上向左移动元素，
						常用于页面元素位置的微调
		
		3. 单方向外边距的设置
			1. 属性 ：
				1. margin-top : 上方外边距
				2. margin-right : 右边的外边距
				3. margin-bottom : 底部外边距
				4. margin-left : 左边外边距
			2. 取值 ：像素值
					只给当前方向设置外边距，给一个值
		4.外边距合并
			1.垂直方向上的外边距(块元素):
				问题:给子元素添加的margin-top，作用于父元素上(浏览器渲染bug)
				解决办法:
					1.可以为父元素添加上边框(一般用透明的)
					2.可以为父元素设置 padding-top 顶部内边距，加0.1px
					3.为父元素添加overflow:hidden;
				margin-bottom
					两个块元素分别设置margin-bottom,margin-top
					最终元素之间的距离取较大的值
			
			2.水平方向上的外边距(块元素):
				默认行内元素水平方向上的外边距会叠加显示
			
		5. 自带默认外边距的元素 ：
				body h1~h6 p ul ol  开发中会用群组选择器全部设置为0
	
	3.内边距
		指元素内容与边框之间的距离
	
		属性 padding
	
		取值 : 像素值
		取值情况 :
			padding:一个值
			 设置上右下左四方向上内容与边框之间的距离
			padding:两个值
			 设置上下内边距为第一个值，左右内边距为第二个值
			padding:三个值
			 设置左右为第二个值
			padding: 四个值
			 上右下左依次取值
	
		单独设置某个方向上的内边距
			属性:padding-top
				 padding-right
				 padding-bottom
				 padding-left
			取值: 给一个值
	
		不同元素类型对盒模型属性的支持情况
			1.块元素完全支持盒模型属性
			2.行内元素不完全支持盒模型属性(margin-top/margin-bottom)
	
		默认带有内边距的元素
			ul ol 表单元素(文本框，按钮)
	
	4.box-sizing
		作用: 指定盒模型的计算方式
		取值:
			1.content-box 默认值
			 	元素的width,height属性只设置内容尺寸，最终在文档中占据的尺寸
				 为 margin border padding width/height 累加得到
			2.border-box
				元素的width,height属性设置包含边框在内的区域大小
				一旦元素设置内边框和边框，会压缩内容的显示区域
				元素最终在文档中占据的尺寸由margin和width/height相加得到
			注意:
				表单按钮默认采用 border-box 计算尺寸
	
	text-align 设置文本居中居。。。。。

背景相关属性
    1.颜色
        属性: background-color
        取值: 颜色值
    2.背景图片
        属性: background-image
        取值: url('')
    3.背景图片相关属性
        1.背景图片重复平铺显示
            属性: background-repeat
            取值: repeat (默认)  当图片尺寸小于元素尺寸，会自动沿水平和垂直方向重复平铺。
                  repeat-x 设置图片沿水平方向上平铺
                  repeat-y 设置图片沿垂直方向上平铺
                  no-repeat 设置图片不重复平铺
        2.背景图片的尺寸
            属性: background-size
            取值: px  取两个值，分别表示背景图片的宽和高
                      取一个值，设置背景图片宽度，高度等比缩放

                  %   取一个值或两个值等同于像素的取值情况
                      百分比参照当前元素的宽高计算
                 cover  覆盖，等比拉伸图片至足够大，完全覆盖元素,超出部分裁剪掉
                 contain  包含，等比拉伸图片至刚好被元素容纳的最大尺寸,有空隙
        3.背景图片的位置
            属性 : background-position
            取值 :
                1. 像素值 x  y
                    x 表示背景图片水平偏移距离，正值表示向右
                    y 表示背景图片垂直偏移距离，正值表示向下
                    默认背景图片从元素左上角显示
                2.百分比 
                    0%  0% 显示在左上角
                    50% 50%  显示在元素的中间位置
                    100% 100%  显示在元素的右下角
                3.方位值
                    水平方向 : left center right
                    垂直方向 : top center bottom
                    设置方位值时，如果缺省一个，默认为居中
            使用场景:
                '精灵图'技术，网页开发过程中为了节省资源，减少网络请求
                通常会将一组小图标以一张图片的形式存储，通过一次网络请
                求加载图片，配合backgrund-position控制图片切换位置
    
    4.背景属性简写
        属性名: background 
        取值 :  color url() repeat position;
        注意: background-size 单独设置
    background: pink url(前端课程资料/img-css/northStar.jpg) no-repeat 10px 10px;

文本与字体相关属性
    1.字体相关属性
        1.字体大小
            属性 : font-size
            取值 : 像素值
        2.指定字体名称
            属性 : font-family
            取值 : 字体名称
            语法注意: 1.字体名称如果是中文，或者由多个英文单词组成必须加引号
                     2.可以设置多个字体名称作备用字体，名称之间用逗号隔开
        e.g:
            font-family: Arial,'宋体','Microsoft TaHei';

        3.字体加粗
            属性 : font-weight
            取值 :
                1.可以去关键字
                    bold(加粗显示)/normal(默认，正常显示)
                2.取无单位的整百数
                    范围 100~900
                    400 : 同 normal
                    700 : 同 bold
        4.设置字体样式(斜体)
            属性 : font-style
            取值 : 1.normal (默认正常显示)
                  2.italic  (斜体显示)
                  3.oblique (文本倾斜显示)
                    一般作为italic的替换样式，可以实现斜体效果
                    在某些情况下可以指定倾斜角度
    
        字体属性简写
            属性 : font
            取值 : style weight size family; (顺序强制)
        语法注意:size,family为必填项

2.文本相关
        1.文本颜色
            属性: color
            取值: 颜色值
        2.本本水平对齐方式
            属性 : text-align
            取值 : left(默认) / center / right
        3.文本装饰线
            属性 : text-decoration
            取值 : 
                  1.underline  下划线
                  2.overline  上划线
                  3.line-through 删除线
                  4.none  取消装饰线
        4.行高
            属性 : line-height
            取值 : 像素值
            注意: 所有文本在其所属行中都是垂直居中的
            使用场景: 
                1.行高可以用来设置一行文本的垂直居中
                    行高与元素的高度保持一致
                2.行高可以实现文本在元素中上下位置的微调
                    eg:
                        1.{
                            height : 100px;
                            line-height : 120px;
                        }
                        2.{
                            height : 100px;
                            line-height : 70px;
                        }
表格相关的属性
    1.表格的尺寸
        表格在设置宽高时可以选择
            1.为table设置宽高，单元格自动大小
            2.为单元格设置宽高，由内容决定表格整体大小
            注意: 只能二选一，表格优先级高于单元格
    2.table 标签完全支持盒模型，默认采用border-box计算尺寸
      tr,td标签，不完全支持盒模型
      td 不支持margin属性
      tr 不支持margin ,padding属性
    
    3.表格边框和并
        将单元格边框和表格边框合并在一起
        属性: border-collapse
        取值: separate (默认 边框分离)
             collapse  设置合并
            
    4.调整单元格之间的距离
        属性 : border-spacing
        取值 : h-value v-value 像素值
        语法注意 : 
            h-value 表示水平方向上的边距
            v-value 表示垂直方向上的边距
            该属性必须添加给table标签，要求必须是边框分离状态才起作用

过渡效果    transition过渡
    元素在两种状态切换时的平滑过渡效果(默认瞬时)
    过渡相关的属性
        指定过渡时长
            属性: transition-duration
            取值: 以秒s/ms为单位

        指定执行过渡效果的属性
            属性 : transition-property
            取值 : 大部分的CSS属性名
            语法 : 
                1.width (指定单个属性名)
                2.width,height (指定多个属性名使用逗号隔开)
                3.all (指定所有发生值改变的属性,默认)
        
        指定过渡发生的时间变化曲率
            属性: transition-timing-function
            取值:   
                1.linear 匀速变化
                2.ease  默认值 慢速开始中间加速慢速结束
                3.ease-in 慢速开始，加速结束
                4.ease-out 快速开始，慢速结束
                5.ease-in-out 慢速开始和结束,中间过程先加速后减速
    
        指定延迟时间    
            属性: transition-delay
            取值: 以秒s/ms为单位的数值，设置过渡效果的延迟执行
    
        简写属性
            属性: transition
            取值: property duration timing-function delay;
            语法注意: 1.duration是必填项，其它可省
                     2.可以分别为属性设置过渡时长
                        eg:
                            transition: width 2s,height 3s,background 5s;

CSS常用的布局方式
    1.布局
        设置元素的排列和显示
    2.分类:
        1.标准流布局(文档流布局，静态布局)
            默认的布局方式
            特点: 元素按照类型和书写顺序，从左到右，从上到下
        2.浮动布局
            元素设置浮动之后，可以停靠在其他元素的边缘
            属性: float
            取值: left / right / none(默认)
            left 元素左浮动直到紧靠其他元素的边缘
            right 元素右浮动，直到紧靠其他元素的边缘
        特点:
            1.元素浮动之后，会脱离文档流，在文档中不再占位，
                表现为悬浮在文档上方，后面正常的元素会向前占位
            2.多个元素浮动时，会依次停靠在前一个浮动元素边缘，
                如果当前父元素中宽度无法容纳，会自动换行显示
            3.任何元素只要设置浮动都可以设置宽高(针对行内元素)
            4.文字环绕效果，浮动元素不占位会遮挡正常元素的显示，
                只遮挡元素位置，不会影响正常内容显示，内容会围绕
                浮动元素显示
            5.浮动元素水平方向没有缝隙，浮动可以解决行内元素或
                行内块元素，水平方向上由于换行导致的空隙问题
    浮动问题:
        由于子元素全部浮动，在文档中不占位，造成父元素高度为0，
        影响页面布局
    解决方法:
        1.给父元素固定高度
        2.给父元素设置overflow:hidden
        3.标准做法: 清除浮动元素带来的影响
            属性: clear
            取值: left / right / both
            用法:
                为元素设置clear属性
                left : 当前元素不受左浮动元素的影响
                right : 当前元素不受右浮动元素的影响
                both ： 不受左浮动或右浮动的影响
            解决父元素高度为0：
                步骤:
                    1.在父元素的末尾添加空的子元素(块元素)
                    2.为空元素设置clear:both;
                
定位布局
    可以设置元素在网页中的显示位置
    属性: position
    取值:
        1.static (静态布局，默认值)
        2.relative(相对定位)
        3.absolute(绝对定位)
        4.fixed (固定定位)
    注意:
        只有元素设置position为relative/absolute/fixed，
        才能称元素为已定位元素

定位详解
    1.相对定位
        position : relative;
        特点: 元素一旦相对定位，可以参照它在文档中的原始位置进行偏移
               仍然在元素文档中占位(保留它原始位置)
        偏移属性: top /right / bottom / left
        取值: 取像素值，设置元素的偏移距离
            top : 设置元素距离顶部的偏移量，正值下移
            left : 设置元素距离左侧的偏移量，正值右移
            bottom : 设置元素距离底部的偏移量，正值上移
            right : 设置元素距离右部的偏移量，正值左移

    2.绝对定位
        position : absolute;
        特点:
            1.元素设置绝对定位，会参照一个离它最近的已经定位
              (position属性不为static就为已定位)的祖先元素进行偏移,
              如果没有已定位的祖先元素，则参照浏览器窗口的原点进行偏移。
            2.元素设置绝对定位会脱离文档流，父元素高度为0
        使用注意：
            1.一般采用父元素相对定位，子元素绝对定位，实现元素偏移
            2.偏移属性是根据元素的参照物进行偏移
    
    3.元素的堆叠次序
        元素出现相互重叠时的显示顺序
        属性 : z-index
        取值 : 给无单位的数值，默认为0，数值越大越靠上显示
        注意 : 只有当前元素设置定位布局，z-index才有效
        用法 : 与 :hover 事件配合改变z-index值显示动效。
    
    4.固定定位
        position : fixed;
        特点 : 元素设置固定定位，会参照浏览器窗口进行偏移

元素显示效果
    1.设置元素显示与隐藏
        属性: visibility
        取值: 
              visible (默认可见)
              hidden  (元素隐藏,仍然占位)
    2.转换元素类型
        属性 : display
        取值 : 
            1.inline 行内元素
            2.block  块元素
            3.inline-block 行内块元素
            4.none  元素隐藏,在文档中不占位

    3.元素透明度设置
        1.rgba(r,g,b,a)  a 取值0~1
        2.属性 : opacity
          取值 : 0-1  (0位透明，1为不透明)
          使用: 
                1.opacity会使包含元素自身和其后代元素在内的所有
                    显示效果半透明
                  rgba() 只针对当前元素的指定属性实现半透明，文本的
                     半透明效果会被子元素继承
                3.子元素与父元素同时设置opacity半透明，子元素中的半透明
                  效果是两个值相乘(在父元素半透明的基础上再次半透明)
    
    4.鼠标形状改变
        默认: 鼠标悬停普通文本上显示为 "I",超链接上为"手指",其它为"箭头"
    
        属性 : cursor 
        取值 :  1.default  箭头
                2.pointer  手指
                3. text    I
                4.progress  箭头带圈
                ...
    
    5.行内块元素的垂直对齐方式
        行内块元素默认按照文本的基线对齐，会出现元素排列不齐的情况
        属性 : vertical-align
        取值 : top/middle/bottom
        使用 : 为行内块元素设置vertical-align,调整左右元素跟它的对齐方式
    
    6.列表相关的属性
        1.list-style-type
            设置项目符号的类型
            取值: square / circle / disc / none
        2.list-style-image
            使用图片自定义项目符号
            取值 : url()
        3.list-style-position
            设置项目符号的位置
            默认显示在内容框的左侧
            取值 :  1.outside 在内容框外部
                    2.inside  显示在内容框内部
        4.简写属性
            list-style : type/url() position
            取消项目符号:
                list-style:none;

元素的转换效果
    元素的转换效果主要指元素可以发生平移，缩放，旋转变换
    属性 : transform
        取值 : 转换函数
        注意: 多个转换函数之间使用空格隔开
    1.元素的转换基准点
        默认情况下，元素以中心点作为转换的基准点
        调整基准点:
            属性 : transform-origin
            取值 : 以左上角为(0,0)  取 x  y 
                可以使用像素值，百分比或方位值表示基准点的位置
                eg:
                    左上角 0px   0px
                    右下角 100%  100%
                    右上角 100%  0 / right top
                方位值:
                    left center right
                    top  center bottom

    2.平移变换
        1.作用：可以改变元素在文档中的位置
        2.使用：
            属性 : transform
            取值:
                1. translate(x,y)
                  x,y分别表示元素在X轴上和Y轴上的平移距离，
                  取像素值，可正可负，区分平移方向
                2. translate(x)
                  一个值表示沿X轴平移
                3. translateX(value)
                    指定沿X轴平移
                4.translateY(value)
                    指定沿Y轴平移
    
    3.缩放变换
        改变元素的显示尺寸(放大或缩小)
        属性 : transform
        取值 : scale(value)
            value 为无单位的数值，表示为缩放比例
            1. value > 1  元素放大
            2. 0 < value < 1 元素缩小
            3. value <0  数值仍然元素缩放比，负号表示元素会被翻转
        其它取值:
            scaleX(v) 沿X轴缩放
            scaleY(v) 沿Y轴缩放
    
    4.旋转变换
        可以设置元素旋转一定的角度显示
        属性 : transform
        取值 : rotate(deg)
            取角度值，以deg为单位
        使用:
            1. rotate() 表示平面旋转
            正值表示顺时针旋转，负值表示逆时针旋转
            2. 三D旋转
                rotateX(deg) 沿X轴旋转
                rotateY(deg) 沿Y轴旋转
    
    5.转换函数的组合使用
        transform : translate() scale() rotate();


​        