###后台运行
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