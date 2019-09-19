### 后台运行
    添加解释器路径
    #!/usr/bin/env python3
    改变权限 (rwxrw-rw-)
    chmod 776/774/u+x httpserver.py
    加./ ---- &符号
    ./httpserver.py &
### linux设置全局变量
    在usr/bin目录下创建软链接
    cd /usr/bin
    >> sudo ln -s webframe ~xx/xx.py webframe
    运行
    >> webframe &
    [1] pid
## 阶段总结
    数据结构
        * 逻辑结构
        * 存储结构
        * 链表，栈，队列
        * 树 遍历方法和递归思想（扩展）
        * 算法：排序，查找
    
    IO
        * （open read write）文件描述符fd
        * 网络 socket（TCP，UDP） 
            TCP/IP协议 HTTP协议
        * fork Process threading （通信，并发）
        * IO多路复用
        * 协程
    
    RE
        * findall
        * match
    
    MySQL
        * CURD
        * pymysql
            connect(commit)->cursor(execute, fatchall)
    
    Git
        * 
        * 
        * 
    
    Project
        * ftp
        * dict
        * httpserver