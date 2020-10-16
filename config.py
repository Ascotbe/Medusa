###################  DNSLOG配置  ##########################
#ceye配置位置
#没有的可以去ceye中申请，http://ceye.io/
#如果没有改为你的Key会导致有些远程命令执行无法检测
#默认使用的是dnslog.cn
#dnslog目前包括(dnslog.cn,ceye)
dnslog_name="dnslog.cn"#切换使用那个dnslog
ceye_dnslog_url="XXXXX.ceye.io"
ceye_dnslog_key="XXXXXXXXXXXXXXXXXXXXXXXX"

###################  Debug模式切换位置  ####################
debug_mode=False

###################  线程数配置位置  ######################
thread_number=15 #默认线程数
thread_timeout_number=5#防止报错等操作导致的超时
###################  Redis配置  ######################
redis_host="localhost"#连接redis的地址，默认本地
redis_port="6379"#redis连接端口，默认6379
redis_db="6"#连接的数据库，默认为6
redis_password="I_will_always_like_Rei_Ayanami"#连接redis的密码

###################  端口扫描配置  ######################
port_threads_number=20#端口扫描默认线程
port_timeout_period=2#端口扫描默认超时时间
