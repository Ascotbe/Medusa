# celery -A Web.Workbench.Tasks worker --loglevel=info --pool=solo
# python3 manage.py runserver 0.0.0.0:9999 --insecure --noreload
# 测试启用HTTPS：python3 manage.py runserver_plus --cert server.crt 0.0.0.0:9999 --insecure --noreload
# mitmdump -s ProxyServer.py --proxyauth any --listen-host "0.0.0.0" --listen-port 9747
# mac redis-server /usr/local/etc/redis.conf
# linux redis-server /etc/redis/redis.conf
# git commit -m  "v1.0.0:palm_tree:"
# pip install python-magic-bin==0.4.14

Language2Command={
    "linux":
        {
            "c":
            {
                "x86":
                {
                    "exe":"i586-mingw32msvc-gcc -mwindows -o ",
                    "dll":"i686-w64-mingw32-gcc -fPIC -shared -o "
                },
                "x64":
                {
                    "exe": "x86_64-w64-mingw32-gcc -o ",
                    "dll": "x86_64-w64-mingw32-gcc -fPIC -shared -o "
                }
            },
            "c++":
            {
                "x86":
                {
                    "exe": "i586-mingw32msvc-g++ -mwindows -o ",
                    "dll": "i686-w64-mingw32-g++ -fPIC -shared -o "#编译c++dll的时候需要在每个函数前面添加extern "C"，不然导出函数是C++编译器编译之后的函数名
                },
                "x64":
                {
                    "exe": "x86_64-w64-mingw32-g++ -o ",
                    "dll": "x86_64-w64-mingw32-g++ -fPIC -shared -o "
                }
            },
            #不支持交叉编译dll程序
            "go":
            {
                "x86":
                {
                    "dll": None,
                    "exe": "GOOS=windows GOARCH=386 go build -o ",
                },
                "x64":
                {
                    "dll": None,
                    "exe": "GOOS=windows GOARCH=amd64 go build -o ",
                }

            },
            "nim":
            {
                    "x86":
                        {
                            "exe": "nim c -d:mingw --app:console  --cpu:i386  --out:",
                            "dll": None#"nim c -d:mingw --app:lib --nomain --cpu:i386 --out:"
                        },
                    "x64":
                        {
                            "exe": "nim c -d:mingw --app:console --cpu:amd64 --out:",
                            "dll": "nim c -d:mingw --app:lib --nomain  --cpu:amd64 --out:"
                        }

                }
        },
    "windows":
        {}
}
Command = Language2Command["linux"]["go"]["x86"]["dll"]  # 通过文件中的语言类型和生成文件进行提取命令

print(Command)