FROM ascotbe/medusa:latest
MAINTAINER ascotbe
#安装所需的包
RUN apt clean
RUN apt update
RUN apt install git -y
RUN apt install nodejs -y
RUN apt install npm -y
RUN apt install nginx -y
RUN apt install redis -y
RUN apt install python3 -y
RUN apt install python3-pip -y
RUN apt install mingw-w64 -y
RUN apt install golang-go -y
RUN apt install nim -y
#修改Redis密码
RUN sed -i "s/I_will_always_like_AyanamiRei/redis_passwd123/g" /etc/redis/redis.conf
#copy压缩包后解压到制定路径
ADD ./Medusa.tat.gz /Medusa
#修改你nginx的配置
RUN sed -i "s/medusa.ascotbe.com/this_is_you_domain_name/g" /etc/nginx/sites-enabled/default
RUN sed -i "s/dnslogtest.ascotbe.com/this_is_your_dnslog_name/g" /etc/nginx/sites-enabled/default
#修改邮服配置
RUN echo "\nthis_is_your_mail_server_domain_name\nmail.this_is_your_mail_server_domain_name" >> /etc/mail/local-host-names
#生成流
RUN m4 /etc/mail/sendmail.mc > /etc/mail/sendmail.cf
#启动邮服
RUN service sendmail start
#安装配置vue
WORKDIR /Medusa/Vue/
RUN rm -rf package-lock.json
RUN npm install npm@6.14.15 -g
RUN npm cache clean --force
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
RUN python3 -m pip install -r Medusa.txt
#启动Nginx
RUN nginx
#启动运行脚本
RUN chmod +x run.sh
CMD ./run.sh