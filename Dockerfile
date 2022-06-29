FROM ascotbe/medusa:latest
MAINTAINER ascotbe
#所有启动服务放在run.sh中用RUN结束后会终止该命令
#安装所需的包
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get clean
RUN echo "deb http://mirrors.aliyun.com/ubuntu/ focal main restricted universe multiverse\ndeb-src http://mirrors.aliyun.com/ubuntu/ focal main restricted universe multiverse\ndeb http://mirrors.aliyun.com/ubuntu/ focal-security main restricted universe multiverse\ndeb-src http://mirrors.aliyun.com/ubuntu/ focal-security main restricted universe multiverse\ndeb http://mirrors.aliyun.com/ubuntu/ focal-updates main restricted universe multiverse\ndeb-src http://mirrors.aliyun.com/ubuntu/ focal-updates main restricted universe multiverse\ndeb http://mirrors.aliyun.com/ubuntu/ focal-proposed main restricted universe multiverse\ndeb-src http://mirrors.aliyun.com/ubuntu/ focal-proposed main restricted universe multiverse\ndeb http://mirrors.aliyun.com/ubuntu/ focal-backports main restricted universe multiverse\ndeb-src http://mirrors.aliyun.com/ubuntu/ focal-backports main restricted universe multiverse\n" > /etc/apt/sources.list
RUN dpkg --add-architecture i386
RUN apt-get update
RUN apt-get install wine -y
RUN apt-get install wine32 -y
RUN apt-get install libwine -y
RUN apt-get install git -y
RUN apt-get install nodejs -y
RUN apt-get install npm -y
RUN apt-get install nginx -y
RUN apt-get install redis -y
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN apt-get install mingw-w64 -y
RUN apt-get install golang-go -y
RUN apt-get install nim -y
RUN apt-get install sendmail -y
#修改Redis密码
RUN sed -i "s/# requirepass foobared/requirepass redis_passwd123/g" /etc/redis/redis.conf
#copy压缩包后解压到制定路径
ADD ./Medusa.tat.gz /Medusa
#修改你nginx的配置
RUN echo "server {\n    listen       443 ssl;\n    server_name  medusa.ascotbe.com;\n    ssl_certificate     /etc/nginx/cert/ssl.pem;  \n    ssl_certificate_key  /etc/nginx/cert/ssl.key;\n    client_max_body_size 100m;\n    ssl_session_timeout  5m;    \n    ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:ECDHE:ECDH:AES:HIGH:!NULL:!aNULL:!MD5:!ADH:!RC4;    \n    ssl_protocols TLSv1 TLSv1.1 TLSv1.2;    \n    ssl_prefer_server_ciphers on;\n    gzip on;\n    gzip_min_length 1k;\n    gzip_comp_level 5;\n    gzip_types text/plain application/javascript application/x-javascript text/css application/xml text/javascript image/jpeg image/gif image/png application/vnd.ms-fontobject font/ttf font/opentype font/x-woff image/svg+xml;\n    gzip_vary on;\n    gzip_disable \"MSIE [1-6]\\.\";\n       gzip_buffers 32 4k;\n    location / {\n                \n        root   /var/www/html/dist;\n        index  index.html;\n    }\n    location /api {\n                proxy_pass http://127.0.0.1:9999/api;\n    }\n    location /s {\n                proxy_pass http://127.0.0.1:9999/s;\n    }\n    location /a {\n                proxy_pass http://127.0.0.1:9999/a;\n    }\n    location /b {\n                proxy_pass http://127.0.0.1:9999/b;\n    }\n}\nserver {\n    listen       80;\n    server_name  medusa.ascotbe.com;\n    location / {\n                \n        root   /var/www/html/dist;\n        index  index.html;\n    }\n    location /api {\n                proxy_pass http://127.0.0.1:9999/api;\n    }\n    location /s {\n                proxy_pass http://127.0.0.1:9999/s;\n    }\n    location /a {\n                proxy_pass http://127.0.0.1:9999/a;\n    }\n    location /b {\n                proxy_pass http://127.0.0.1:9999/b;\n    }\n}\nserver {\n    listen       80;\n    client_max_body_size 100m;\n    server_name  dnslogtest.ascotbe.com;\n    gzip on;\n    gzip_min_length 1k;\n    gzip_comp_level 5;\n    gzip_types text/plain application/javascript application/x-javascript text/css application/xml text/javascript image/jpeg image/gif image/png application/vnd.ms-fontobject font/ttf font/opentype font/x-woff image/svg+xml;\n    gzip_vary on;\n    gzip_disable \"MSIE [1-6]\\.\";\n       gzip_buffers 32 4k;\n    location / {\n        proxy_pass  http://127.0.0.1:8888; \n        proxy_set_header Host \$host;\n              proxy_set_header X-Real-IP \$remote_addr; \n        proxy_set_header x-forwarded-for \$proxy_add_x_forwarded_for;       \n    }\n}\nserver {\n    listen       80;\n    client_max_body_size 100m;\n    server_name  *.dnslogtest.ascotbe.com;\n    location / {\n        proxy_pass  http://127.0.0.1:8888;\n        proxy_set_header Host \$host;\n              proxy_set_header X-Real-IP \$remote_addr;\n        proxy_set_header x-forwarded-for \$proxy_add_x_forwarded_for;      \n    }\n}" > /etc/nginx/sites-enabled/default
RUN sed -i "s/medusa.ascotbe.com/this_is_you_domain_name/g" /etc/nginx/sites-enabled/default
RUN sed -i "s/dnslogtest.ascotbe.com/this_is_your_dnslog_name/g" /etc/nginx/sites-enabled/default
#修改邮服配置
RUN sed -i "s/Family=inet,  Name=MTA-v4, Port=smtp, Addr=127.0.0.1/Family=inet,  Name=MTA-v4, Port=smtp, Addr=0.0.0.0/g" /etc/mail/sendmail.mc
RUN sed -i "s/Family=inet,  Name=MSP-v4, Port=submission, M=Ea, Addr=127.0.0.1/Family=inet,  Name=MSP-v4, Port=submission, M=Ea, Addr=0.0.0.0/g" /etc/mail/sendmail.mc
RUN echo "\nthis_is_your_mail_server_domain_name\nmail.this_is_your_mail_server_domain_name" >> /etc/mail/local-host-names
#生成流
RUN m4 /etc/mail/sendmail.mc > /etc/mail/sendmail.cf
#安装配置vue
WORKDIR /Medusa/Vue/
RUN rm -rf package-lock.json
RUN npm install highcharts --save  --registry=http://registry.cnpmjs.org
RUN npm run build
RUN mv dist/ /var/www/html/
WORKDIR /etc/nginx/
RUN mkdir cert/
#配置HTTPS证书
WORKDIR /Medusa
RUN mv ssl.pem /etc/nginx/cert/
RUN mv ssl.key /etc/nginx/cert/
#安装后端所需的包
RUN python3 -m pip install -r Medusa.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
#生成脚本
RUN echo "#!/bin/bash\npython3 -c 'from Web.CVE.NistMonitoring.NistInitialization import NistInitialization;from Web.ActiveScan import InitializationPlugin;InitializationPlugin.Run();NistInitialization();from manage import InitialConfiguration;InitialConfiguration()'\nredis-server /etc/redis/redis.conf &\nservice sendmail start &\npython3 DNSServer.py &\npython3 HTTPServer.py &\ncelery -A Web worker -B --loglevel=info --pool=solo &\nnginx &\ngunicorn Web.wsgi:application --bind 0.0.0.0:9999 --workers 6" > run.sh
#启动运行脚本
RUN chmod +x run.sh
CMD ./run.sh