

[TOC]



## nodejs 简介

基于谷歌浏览器 v8引擎的解释器,只有一个版本，不存在兼容性问题

网站 : http://www.npmjs.com (npm官网，文档网站，包下载网站)

中文网站    :  nodejs.cn



## 运行模式

### 脚本模式

```shell
node path.js
```

### 交互模式

```javascript
>>node
>
>
退出 ctrl+c  | .exit
```

### 严格模式

​    以严格模式运行JavaScript代码，避免各种潜在陷阱。

1. 文档第一行写上'use strict'

2. 我们可以给Nodejs传递一个参数，让Node直接为所有js文件开启严格模式：

   ```shell
   node --use_strict calc.js
   ```

   

## npm 包管理工具(nodejs)

下载 nodejs解释器自带 npm包管理器
NPM：Node Package Manage
包 ：就是一个目录模块，里边包含有多个文件，其中有一个文件名为 package.json的文件，是包说明文件

### 下载包

切换到要下载的目录  (在文件夹中，可以按Shift 点击鼠标右键打开 powershell , win10？)

```shell
npm install packagename

```

初次下载会在当前目录自动生成 node_modules目录，下载的包就存放其中；
自动生成package_lock.json，包的依赖关系存放其中



## global对象

在 浏览器javascript 中 全局对象是 windows,在文件中定义的变量和函数都是全局的。 nodejs中是 global

在 nodejs 中,在脚本文件中声明的变量和函数都是局部的，在交互下是全局的。

全局变量和函数可以使用 global 访问

```javascript
>var a = 1
>function fn(){}
>global.a;
>global.fn();
```

1. console 对象   

   global对象下的对象

   ```javascript
   global.console.log();    //打印消息
   global.console.info();   //打印消息
   global.console.warn();   //打印警告信息
   global.console.error();  //打印错误信息
   //计时程序运行时间 : 参数字符要一致,代表一个测试
   global.console.time('自定义字符串');    //开始计时
   //程序块;
   global.console.timeEnd('自定义字符串');  //结束计时
   //运行速率:  do-while > for > while
   ```

2. process 对象 进程对象

   ```javascript
   process.arch    // cpu 位数
   process.platform    //操作系统
   process.env     //系统环境变量(对象结构)
   process.version     // 当前nodejs解释器版本号
   process.pid      // 当前进程编号
   process.kill(pid)   //杀死pid进程
   ```

3. buffer 对象  缓冲区对象

    缓冲区： 在内存中存储数据区域，存储网络传输时的资源

   创建buffer

   ```javascript
   var buf = Buffer.alloc(size:number(字节)[,str]);
   //参数:
       //size ： 设置空间大小，字节为单位
       //str : 初始化的数据,缺省为空
   var buf = Buffer.alloc(5,'a');
   console.log(buf);   // <Buffer 61 61 61 61 61>
   var buf = Buffer.alloc(5,'abcde');
   console.log(buf);   // <Buffer 61 62 63 64 65>
   //方法:
   buf.toString()  //  abcde   将Buffer字符转换为字符串
   ```

4. 全局函数

   parseInt/parseFloat/encodeURI/decodeURI/isNaN/eval

   

5. 定时器

   - 一次性定时器,只执行一次

     ```javascript
     //设置
     var timer = setTimeout(function (){
         code;
     },间隔时间ms);
     //清除
     clearTimeout(timer);
     ```

   - 周期性定时器，间隔执行

     ```javascript
     //设置    
     var timer = setInterval(function (){
         code;
     },间隔时间ms);
     //清除
     clearInterval(timer);
     ```

   - 即时执行定时器

     ```javascript
     1.
     process.nextTick(function(){
         code;
     });
     此定时器会在事件队列最后即时执行(程序最后)
     不可清除
             
     2.
     var timer = setImmediate(function(){
          code;
     });
     此定时器会在事件队列最前面即时执行(程序最前)
     清除
     clearImmediate(timer);
     ```

6. module模块

   在NodeJs下模块分为自定义模块、核心模块(官方模块)、第三方模块

   在NodeJs下，任意一个文件都是一个模块，文件中的代码默认被一个构造函数所包含

   模块构造函数:

   ```javascript
   (function (exports,require,module,__dirname,__filename){
          module code;
   })
   ```

   参数:

   - __dirname : 当前模块(文件)所在目录，绝对路径

   - __filename : 当前模块(文件)名，绝对路径

   - require :函数  用于导入其他模块，返回模块对象

     ```javascript
     var obj = require('./*.js')  // 同一级模块要使用 ./路径;
                                  //自定义模块格式为js结尾，.js可以省略
     //由于模块内的变量为局部变量，默认是私有的，所以导入模块诺没有公开变量则 obj为{}
     ```

   - module  : 用于公开当前模块内的变量

     module.exports.var = localvar;
     目标模块 使用 obj.var 访问本模块变量或函数

   - exports : exports === module.exports



## 模块

   1. 以路径开头的

      |                  |                      |                                                              |
      | ---------------- | -------------------- | ------------------------------------------------------------ |
      | 文件模块         | require('./*.js')    | 常用于用户自定义模块，导入时后缀可以省略                     |
      | 目录模块(文件夹) | require('./dirname') | 在此目录下自动导入名字为"index.js"的文件，没有就找 package.json;或者使用"package.json"文件声明main属性，来指定要导入的文件名称{                                                    "main":"test.js",   //属性名必须是双引号括起 } |

      

2. 不以路径开头的

   |                  |                    |                                                              |
   | ---------------- | ------------------ | ------------------------------------------------------------ |
   | 文件模块         | require('*.js')    | 核心模块                                                     |
   | 目录模块(文件夹) | require('dirname') | 自动到当前"node_modules"目录中查找目录为 dirname 的目录                                           (当前目录没有"node_modules"会向上一级目录逐级查找)                                           第三方模块一般使用此方式导入，需要提前下载到node_modules目录 |

   

## 核心模块

是 NODEJS 官方提供的模块，不需要创建，可以直接导入

### querystring  查询字符串模块 

查询字符串  menuId=653493&version=WEBVN201811

`const querystring = require('querystring');`

**方法：**

- parse(obj[, sep[, eq[, options]]])     将查询字符串解析为对象
- stringify(obj[, sep[, eq[, options]]]) 将对象转换为查询字符串

**参数：**

- obj <Object> 要序列化为 URL 查询字符串的对象。

- sep <string> 用于在查询字符串中分隔键值对的子字符串。默认值: '&'。

- eq <string> 用于在查询字符串中分隔键和值的子字符串。默认值: '='。

- options 

  encodeURIComponent <Function> 在查询字符串中将 URL 不安全字符转换为百分比编码时使用的函数。

   默认值: querystring.escape()

```javascript
const querystring = require('querystring');

var str = "menuId=653493&version=WEBVN201811"
var req = querystring.parse(str);

console.log(req);//{ menuId: '653493', version: 'WEBVN201811' }

var obj = {
       name:"wei",
       sex:"man"
}
var req2 = querystring.stringify(obj);
console.log(req2);//name=wei&sex=man
```



### URL 模块     url 解析模块

`const url = require('url');`

**方法：**

- parse(urlstr);  将url解析为 url对象
- format(obj);    将url对象转换为 url

```javascript
const url = require('url');
var u = "http://tts.tmooc.cn/video/showVideo?menuId=653493&version=WEBVN201811"
var req = url.parse(u);
console.log(req);
/*Url {
      protocol: 'http:',  //协议
      slashes: true,
      auth: null,     
      host: 'tts.tmooc.cn',   //主机地址(域名/ip+oirt)
      port: null,             //端口号
      hostname: 'tts.tmooc.cn',
      hash: null,
      search: '?menuId=653493&version=WEBVN201811',
      query: 'menuId=653493&version=WEBVN201811',     // 查询字符串
      pathname: '/video/showVideo',                   // 文件在服务器上的路径
      path: '/video/showVideo?menuId=653493&version=WEBVN201811',
      href:'http://tts.tmooc.cn/video/showVideo?menuId=653493&version=WEBVN201811' }
*/

var obj = {
        protocol: 'http',
        hostname: 'tts.tmooc.cn',
        port: 80,
        pathname: '/video/showVideo',
        query: { menuId: '653493', version: 'WEBVN201811' },    //query要是对象格式
}
var req2 = url.format(obj);
console.log(req2);
//http://tts.tmooc.cn:80/video/showVideo?menuId=653493&version=WEBVN201811
```



### fs 模块  文件系统模块

`const fs = require('fs');`

**fs 方法**：  基本所有方法都有同步和异步两种, 带 Sync 的为同步
              	同步方法直接返回结果，异步用回调函数接收结果

#### 查看文件信息方法：

`fs.stat(path: PathLike, callback: (err: NodeJS.ErrnoException, stats: Stats) => void): void`
异步查看文件信息方法

- path    : 要查看的文件路径
- callback(err,stats) ：回调函数
- err : 查看文件失败的错误信息
- stats : 文件的状态信息

`var res = fs.statSync(path)`  方法：
        同步查看文件信息的方法
res === stats

- stats.isDirectory()     //fs.Stats 对象描述文件系统目录，则返回 true。
- stats.isFile()          //fs.Stats 对象描述常规文件，则返回 true。
- stats.isSocket()        //fs.Stats 对象描述套接字，则返回 true。
- stats.dev           //<number> | <bigint>包含该文件的设备的数字标识符。
- stats.info          //<number> | <bigint>文件系统特定的文件索引节点编号。
- stats.mode          //<number> | <bigint>描述文件类型和模式的位字段。
- stats.nlink         //<number> | <bigint>文件存在的硬链接数。
- stats.uid           //<number> | <bigint>拥有该文件（POSIX）的用户的数字型用户标识符。
- stats.gid           //<number> | <bigint>拥有该文件（POSIX）的群组的数字型群组标识符。
- stats.rdev          //<number> | <bigint>如果文件被视为特殊文件，则此值为数字型设备标识符。
- stats.size          //<number> | <bigint>文件的大小（以字节为单位）。
- stats.blksize       //<number> | <bigint>用于 I/O 操作的文件系统块的大小。
- stats.blocks        //<number> | <bigint>为此文件分配的块数。
- stats.atimeMs       //<number> | <bigint>表明上次访问此文件的时间戳，以 POSIX 纪元以来的毫秒数表示。
- stats.mtimeMs       //<number> | <bigint>表明上次修改此文件的时间戳，以 POSIX 纪元以来的毫秒数表示。
- stats.ctimeMs       //<number> | <bigint>表明上次更改文件状态的时间戳，以 POSIX 纪元以来的毫秒数表示。
- stats.birthtimeMs   //<number> | <bigint>表明此文件的创建时间的时间戳，以 POSIX 纪元以来的毫秒数表示。
- stats.atime         //<Date>表明上次访问此文件的时间戳。
- stats.mtime         //<Date>表明上次修改此文件的时间戳。
- stats.ctime         //<Date>表明上次更改文件状态的时间戳。
- stats.birthtime     //<Date>表示此文件的创建时间的时间戳。

```javascript
const fs = require('fs');
fs.stat('teee.py',(err,stats)=>{
        console.log(err);
        console.log(stats);
});

// null
// Stats {
//   dev: 690497728,
//   mode: 33206,
//   nlink: 1,
//   uid: 0,
//   gid: 0,
//   rdev: 0,
//   blksize: undefined,
//   ino: 5629499534563997,
//   size: 70,
//   blocks: undefined,
//   atimeMs: 1553581455475.0383,
//   mtimeMs: 1553581455475.0383,
//   ctimeMs: 1553581455475.0383,
//   birthtimeMs: 1553581455475.0383,
//   atime: 2019-03-26T06:24:15.475Z,
//   mtime: 2019-03-26T06:24:15.475Z,
//   ctime: 2019-03-26T06:24:15.475Z,
//   birthtime: 2019-03-26T06:24:15.475Z }
```



#### 创建目录方法

`fs.mkdir(path[, options], callback)`

`fs.mkdirSync(path[, options]`

```javascript
fs.mkdir('/tmp/a/apple', { recursive: true }, (err) => {
        if (err) throw err;
});
```



#### 删除目录方法

` fs.rmdir(path[, options], callback)` 

`fs.rmdirSync(path[, options]`

- path <string> | <Buffer> | <URL>
- callback <Function>
- err <Error>



#### 删除文件

`fs.unlink(path, callback)`

`fs.unlinkSync(path)`

- path <string> | <Buffer> | <URL>
- callback <Function>
- err <Error>



#### 读取目录

`fs.readdir(path[, options], callback)`

`fs.readdirSync(path[, options])`

- path <string> | <Buffer> | <URL>

- options <string> | <Object>
  - encoding <string> 默认值: 'utf8'。如果 encoding 设置为 'buffer'，则返回的文件名是 Buffer 对象。
  - withFileTypes <boolean> 默认值: false。
- callback <Function>
  - err <Error>
  - files <string[]> | <Buffer[]> | <fs.Dirent[]> 其中 files 是目录中的文件名的数组（不包括 '.' 和 '..'）。



#### 读取文件内容

`fs.readFile(path[, options], callback)`

`fs.readFileSync(path[, options])`

- path <string> | <Buffer> | <URL> | <integer> 文件名或文件描述符。
- options <Object> | <string>
  - encoding <string> | <null> 默认值: null。
  - flag <string> 参阅支持的文件系统标志。默认值: 'r'。
- callback <Function>
  - err <Error>
  - data <string> | <Buffer>

```javascript
fs.readFile('/etc/passwd', (err, data) => {
      if (err) throw err;
      console.log(data);
});
```

fs.readFile() 函数会缓冲整个文件。 为了最小化内存成本，尽可能通过 fs.createReadStream() 进行流式传输。



#### 创建文件并写入数据

`fs.writeFile(file, data[, options], callback)`

`fs.writeFileSync(file, data[, options])`

- file - 文件名或文件描述符。
- data - 要写入文件的数据，可以是 String(字符串) 或 Buffer(缓冲) 对象。
- options - 该参数是一个对象，包含 {encoding, mode, flag}。默认编码为 utf8, 模式为 0666 ， flag 为 'w'
- callback - 回调函数，回调函数只包含错误信息参数(err)，在写入失败时返回。

writeFile 直接打开文件默认是 w 模式，所以如果文件存在，该方法写入的内容会覆盖旧的文件内容。



#### 打开文件

`fs.open(path, flags[, mode], callback)`

`fs.openSync(path, flags[, mode])`

- path - 文件的路径。
- flags - 文件打开的行为。

>r	以读取模式打开文件。如果文件不存在抛出异常。
>r+	以读写模式打开文件。如果文件不存在抛出异常。
>rs	以同步的方式读取文件。
>rs+  以同步的方式读取和写入文件。
>w	以写入模式打开文件，如果文件不存在则创建。
>wx	类似 'w'，但是如果文件路径存在，则文件写入失败。
>w+	以读写模式打开文件，如果文件不存在则创建。
>wx+	类似 'w+'， 但是如果文件路径存在，则文件读写失败。
>a	以追加模式打开文件，如果文件不存在则创建。
>ax	类似 'a'， 但是如果文件路径存在，则文件追加失败。
>a+	以读取追加模式打开文件，如果文件不存在则创建。
>ax+	类似 'a+'， 但是如果文件路径存在，则文件读取追加失败。

- mode - 设置文件模式(权限)，文件创建默认权限为 0666(可读，可写)。
- callback - 回调函数，带有两个参数如：callback(err, fd)。

```javascript
var fs = require("fs");
// 异步打开文件
console.log("准备打开文件！");
fs.open('input.txt', 'r+', function(err, fd) {
	if (err) {
    	return console.error(err);
	}
	console.log("文件打开成功！");     
});
```



#### 读取文件

`fs.read(fd, buffer, offset, length, position, callback)`

`fs.readSync(fd, buffer, offset, length, position)`

该方法使用了文件描述符来读取文件。

- fd - 通过 fs.open() 方法返回的文件描述符。
- buffer - 数据写入的缓冲区。
- offset - 缓冲区写入的写入偏移量。
- length - 要从文件中读取的字节数.
- position - 文件读取的起始位置，如果 position 的值为 null，则会从当前文件指针的位置读取。
- callback - 回调函数，有三个参数err, bytesRead, buffer，err 为错误信息， bytesRead 表示读取的字节数，buffer 为缓冲区对象。



#### 写入文件

`fs.write(fd, buffer[, offset[, length[, position]]], callback)`

`fs.writeSync(fd, buffer[, offset[, length[, position]]])`

`fs.write(fd, string[, position[, encoding]], callback)`  

`fs.writeSync(fd, string[, position[, encoding]])`

- 将 buffer 写入到 fd 指定的文件。
- offset 决定 buffer 中要被写入的部位， length 是一个整数，指定要写入的字节数。
- 将 string 写入到 fd 指定的文件。 如果 string 不是一个字符串，则该值会被强制转换为字符串。
- position 指定文件开头的偏移量（数据应该被写入的位置）。 如果 typeof position !== 'number'，则数据会被写入当前的位置。 参阅 pwrite(2)。
- 回调有三个参数 (err, bytesWritten, buffer)，其中 bytesWritten 指定 buffer 中被写入的字节数。
- 如果调用此方法的 util.promisify() 版本，则返回的 Promise 会返回具有 bytesWritten 和 buffer 属性的 Object。
- 在同一个文件上多次使用 fs.write() 且不等待回调是不安全的。 对于这种情况，建议使用 fs.createWriteStream()。



#### 将数据追加到文件，如果文件尚不存在则创建该文件

`fs.appendFile(path, data[, options], callback)`

`fs.appendFileSync(path, data[, options])`

- path <string> | <Buffer> | <URL> | <number> 文件名或文件描述符。
- data <string> | <Buffer>
- options <Object> | <string>
  - encoding <string> | <null> 默认值: 'utf8'。
  - mode <integer> 默认值: 0o666
  - flag <string> 参阅支持的文件系统标志。默认值: 'a'。
- callback <Function>
  - err <Error>



#### 关闭文件

`fs.close(fd, callback)` 

 `fs.closeSync(fd)`

- fd <integer>
- callback <Function>
  - err <Error>

异步的 close()。 除了可能的异常，完成回调没有其他参数。



#### 文件重命名

`fs.rename(oldPath, newPath, callback)`

`fs.renameSync(oldPath, newPath)`

- oldPath <string> | <Buffer> | <URL>
- newPath <string> | <Buffer> | <URL>
- callback <Function>
  - err <Error>

异步地将 oldPath 上的文件重命名为 newPath 提供的路径名。 如果 newPath 已存在，则覆盖它。 除了可能的异常，完成回调没有其他参数。



#### 检查文件权限,可用于检查文件是否存在

`fs.access(path[, mode], callback)`

`fs.accessSync(path[, mode])`

- path <string> | <Buffer> | <URL>
- mode <integer> 默认值: fs.constants.F_OK。
- callback <Function>
  - err <Error>

测试用户对 path 指

定的文件或目录的权限。 mode 参数是一个可选的整数，指定要执行的可访问性检查。

mode 可选的值参阅文件可访问性的常量。 可以创建由两个或更多个值按位或组成的掩码（例如 fs.constants.W_OK | fs.constants.R_OK）

不建议在调用 fs.open()、 fs.readFile() 或 fs.writeFile() 之前使用 fs.access() 检查文件的可访问性。 
这样做会引入竞态条件，因为其他进程可能会在两个调用之间更改文件的状态。 
相反，应该直接打开、读取或写入文件，如果文件无法访问则处理引发的错误。



#### 更改文件的权限

`fs.chmod(path, mode, callback)`

`fs.chmodSync(path, mode)`

- path <string> | <Buffer> | <URL>
- mode <integer>
- callback <Function>
  - err <Error>

fs.chmod() 和 fs.chmodSync() 方法中使用的 mode 参数是使用以下常量的逻辑或运算创建的数字型位掩码：

| 常量                 | 八进制值 | 说明               |
| -------------------- | -------- | ------------------ |
| fs.constants.S_IRUSR | 0o400    | 所有者可读         |
| fs.constants.S_IWUSR | 0o200    | 所有者可写         |
| fs.constants.S_IXUSR | 0o100    | 所有者可执行或搜索 |
| fs.constants.S_IRGRP | 0o40     | 群组可读           |
| fs.constants.S_IWGRP | 0o20     | 群组可写           |
| fs.constants.S_IXGRP | 0o10     | 群组可执行或搜索   |
| fs.constants.S_IROTH | 0o4      | 其他人可读         |
| fs.constants.S_IWOTH | 0o2      | 其他人可写         |
| fs.constants.S_IXOTH | 0o1      | 其他人可执行或搜索 |

构造 mode 更简单的方法是使用三个八进制数字的序列（ 例如 765）。 最左边的数字（示例中的 7）指定文件所有者的权限。 
中间的数字（示例中的 6）指定群组的权限。 最右边的数字（示例中的 5）指定其他人的权限。

​		数字			说明
​         7			可读、可写、可执行
​         6			可读、可写
​         5			可读、可执行
​         4			只读
​         3			可写、可执行
​         2			只写
​         1			只可执行
​         0			没有权限

例如，八进制值 0o765 表示：

所有者可以读取、写入和执行该文件。
群组可以读和写入该文件。
其他人可以读取和执行该文件。



### 同步和异步

​    异步 ： 不会影响后续代码会继续执行，会把异步代码放到程序最后执行
​        通过回调函数来获取结果
​    同步 ： 会阻止后续代码执行，只有方法执行完，才能继续执行
​        通过返回值来获取结果

### 文件描述符

​    任何指定的文件描述符都必须支持读取。
​    如果将文件描述符指定为 path，则不会自动关闭它。
​    读数将从当前位置开始。例如，如果文件已经有内容 'Hello World' 并且使用文件描述符读取了六个字节，
​    则使用相同文件描述符调用 fs.readFile() 将返回 'World' 而不是 'Hello World'。



## http 协议

​    是浏览器和web服务器之间的通信协议

### http模块
​       ` const http = require('http');`

### 模拟浏览器发请求

```javascript
http.get(url,(res)=>{
        res //响应内容，对象形式
        res.statusCode  //响应状态码
        res.on('data',(buf)=>{
            buf.toString();
    })  //用事件来获取服务器端响应的数据
});
```



### 创建web服务器

`const http = require('http');

1. 创建web服务器

`var server = http.createServer();` 

2. 监听端口

`server.listen(port?: number, hostname?: string,backlog?: number,listeningListener?: () => void); `

3. 监听请求事件

`server.on('request',(req,res)=>{ });`

req  请求对象 

- req.method      请求方法
- req.url         请求路由
- req.headers     请求头对象

res  响应对象

- res.writeHead(302,{                    设置响应的状态码和头信息
          Location:'https//www.baidu.com'     重定向属性 Location
          });
- res.write('');  创建响应文本,可以多次res.write(''); 添加文本
- res.end();      响应结束

```javascript
const http = require('http');
var server = http.createServer();
server.listen(8888,()=>{console.log('127.0.0.1 8888');});
server.on('request',(req,res)=>{
	if(req.url=='/'){
       res.write('<h1>index<h1/>');
       res.end(); 
	}else if(req.url=='/er'){
       res.write('er');
       res.write('<br>hello');
       res.end(); 
	}else{
       res.writeHead(302,{
           Location:'http://www.baidu.com',
       });
       res.end();
	}
});
```





## express web服务器框架

第三方框架  网站：www.expressjs.com.cn

基于 nodejs, 用于构建web服务器的框架

### 创建web服务器

```javascript
const express = require('express');

var server = express();

server.listen(8888,'192.168.0.10',()=>{
    console.log('listen to 192.168.0.10:8888');
});
server.get('/login',(req,res)=>{
     r = '<h1>login<h1/>';
     res.send(r);        //只允许使用一次 send
});
```

### 请求对象    request

- req.method  请求方法
- req.url     请求url
- req.headers 请求头
- req.query   请求中的查询字符串
- req.body    包含请求正文中提交的键值对数据



### 响应方法    response

- res.send(str | number)  //发送文本,当为数值是表示响应的状态码
- res.sendFile('abspath')  //发送文件 __dirname + filename

- res.redirect('/url')       //重定向



### GET 请求,查询字符串传参

```javascript
app.get('/loginin',(req,res)=>{
        console.log(req.query);
        console.log(listen into ${a++} ,from ${req.hostname});
        res.send(welcome ${qs.uname});
});
```



### POST 请求，请求体传参

```javascript
app.post('/login',(req,res)=>{
      req.on('data',(buf)=>{
            var qs = querystring.parse(buf.toString())
            console.log(listen into ${a++} ,from ${req.hostname});
		}	
      es.send(welcome ${qs.uname});
})
```



### 路由传参

url = 'http://192.168.0.10:8888/user/3/wei'
路由必须带对应的参数

```javascript
app.get('/user/:id/:name', function(req, res) {
    res.send('user ' + req.params.id + req.params.name);
});
```



### 路由器  router

把一组视图函数指定给同一个子路由,便于组织功能模块

#### 架构

路由器文件

```javascript
const express = require('express');
const router = express.Router(); //创建空路由器对象   
router.get('list/:name',(req,res)=>{   //请求方法get URL：/list
      res.send('message');
});
module.exports = router;    //导出路由器
```

服务器文件

```javascript
const express = require('express');
const userRouter = require('./路由器文件')  //导入路由器文件
var server = express();
server.listen(8888,'192.168.0.10',()=>{
console.log('listen to 192.168.0.10:8888');
});
server.use('/user',userRouter); //挂载路由器到服务器
```

访问URL: 192.168.0.10:8888/user/list



### 中间件

中间件  -->  视图函数   --> 中间件

    在 express 中, 中间件和视图函数根据在文件的位置顺序依次执行
    
    创建中间件(在视图函数之前执行)
        server.use((req,res[,next])=>{
            console.log('请求拦截中间件');
            res.send('验证失败');
            next(); //执行下一个函数
        });
    
    路由函数
        server.get('/login',(req,res,next)=>{
            r = '<h1>login<h1/>';
            res.send(r);
            next(); //下一个中间件
        });
    
    创建中间件(在视图函数之后执行)
        server.use((req,res[,next])=>{
            console.log('数据库中间件');
            res.send('保存成功');
            next(); //下一个中间件
        });
    
    1. 在中间件和视图函数中必须有 next(),程序才会执行下一个中间件或视图函数。
    2. 只要有 next() 函数，应用就会继续向下执行，哪怕之前有 send()。
    3. 一次请求只能执行一次 res.send(), 当程序流程执行多次res.send()时，
        只有第一个起作用,并且第二个执行保错。


​    
    创建指定url的中间件(默认全部拦截)
        server.use('/list',(req,res[,next])=>{
            console.log('数据库中间件');
            res.send('保存成功');
            next(); //下一个中间件
        });


​    
    路由中间件
        server.use('/user',userRouter);
        server.use('/list',listRouter);
    
    内置中间件
        静态文件托管中间件,可以托管多个文件夹
        server.use(express.static('static_path1'));
        server.use(express.static('static_path2'));
    
        url = 192.168.0.10:8888[/文件目录]/文件名


    第三方中间件
        1. body-parser  请求体数据解析中间件(解析的数据放入 res.body对象)
            const bodyParser = require('body-parser');
    
            server.use(bodyParser.urlencoded({
                extended:false  //是否使用扩展的qs模块将查询字符串解析为对象,false使用querystring
            }));
    
            server.post('seimt',(req,res)=>{
                req.body;
            });


MYSQL模块   第三方模块
    const mysql = require('mysql'); //导入模块

    1. 普通连接
       1. var connection = mysql.createConnection({    //创建连接对象
            host:'127.0.0.1',
            port:'3306',
            user:'root',
            password:'123456',
            database:'webdb'
         });
       2. connection.connect((err)=>{
            if(err) throw err;
         });   //执行连接
       3. connection.query('select * from wife',(err,result)=>{
            if(err) throw err;
            console.log(result);    //[ RowDataPacket { id: 1, name: 'wei', age: 20, author_id: 2 },
                                    //RowDataPacket { id: 2, name: 'wei1', age: 21, author_id: 3 } ]
         });  //执行sql语句
       4. connection.end();   //执行完所有sql语句后关闭连接
    
    2. 连接池
        一次创建多个连接对象
    
       1. var pool = mysql.createPool({ //创建连接池对象
            host:'127.0.0.1',
            port:'3306',
            user:'root',
            password:'123456',
            database:'tedu',
            connectionLimit:20  //连接池数量
         });
       2.  pool.query('select * from wife',(err,result)=>{
            if(err) throw err;
            console.log(result);    //[ RowDataPacket { id: 1, name: 'wei', age: 20, author_id: 2 },
                                    //RowDataPacket { id: 2, name: 'wei1', age: 21, author_id: 3 } ]
         });     //执行sql语句
    
        连接池不会关闭,执行多次sql语句
    
    在执行删除、修改、插入时,返回OkPacket对象,对象中的affectedRow属性表示执行成功的row数，0表示没一条执行成功
       1. 删除
        pool.query('delete * from wife',(err,result)=>{
            if(err) throw err;
            console.log(result);    //OkPacket { affectedRow：1}
         });
    
       2.  修改 
            pool.query('update wife set name=?,age=? where id=?,['wei',20,2],(err,result)=>{
                if(err) throw err;
                console.log(result);    //OkPacket { affectedRow：1}
            }); 
        
       3. 插入
            基本插入
            pool.query('insert into wife values(?,?,?)',[null,'wei',22],(err,result)=>{
                if(err) throw err;
                console.log(result);    //OkPacket { affectedRow：1}
            }); 
    
         对象插入
            var person = {
                id:null,
                name:'wei',
                age:20
            }
            pool.query('insert into wife set ?',[person],(err,result)=>{
                if(err) throw err;
                console.log(result);    //OkPacket { affectedRow：1}
            }); 


​    
    占位符,防止SQL注入
        在sql语句中的值用?号表示，在第二个参数提供参数数组
        pool.query('delete * from wife where id=? and sex=?',[2,1] ,(err,result)=>{})







