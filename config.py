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

###################  Redis配置  ######################
redis_host="localhost"
redis_port="6379"
redis_db="6"
redis_password="I_will_always_like_Rei_Ayanami"