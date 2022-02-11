#!/bin/bash
if [ $# != 11 ] ; then
    echo "Please enter 10 parameters, use the default value, use 'none' instead of the input"
    exit 1;
fi
redis_password=$1
secret_key_required_for_account_registration=$2
forget_password_key=$3
cross_site_script_uses_domain_names=$4
domain_name_system_address=$5
third_party_mail_host=$6
third_party_mail_user=$7
third_party_mail_pass=$8
local_mail_host=$9
local_mail_user=${10}
server_ip=${11}
if [[ `uname` == 'Linux' ]]; then
    sudo apt update
    sudo apt install git -y
    sudo apt install docker.io -y
    sudo systemctl start docker
    if [ "$redis_password" = "none" ]  ;then
        echo -e "\033[32m redis password no change ~ \033[0m"
    else
        #redis密码
        sed -i "s/I_will_always_like_AyanamiRei/$redis_password/g" config.py
        sed -i "s/redis_passwd123/$redis_password/g" Dockerfile
        echo -e "\033[31m redis password change to \033[35m--->\033[0m\033[0m$redis_password"
    fi
    if [ "$secret_key_required_for_account_registration" = "none" ]  ;then
        echo -e "\033[32m unmodified registration required secret key ~ \033[0m"
    else
        #注册密码key
        sed -i "s/I_will_always_like_SoryuAsukaLangley/$secret_key_required_for_account_registration/g" config.py
        echo -e "\033[31m modify registration required key \033[35m--->\033[0m\033[0m$secret_key_required_for_account_registration"
    fi
    if [ "$forget_password_key" = "none" ]  ;then
        echo -e "\033[32m Unmodified forgot the secret key ~ \033[0m"
    else
        #忘记密码key
        sed -i "s/I_will_always_like_KatsuragiMisato/$forget_password_key/g" config.py
        echo -e "\033[31m modify the secret required for forgot password \033[35m--->\033[0m\033[0m$forget_password_key"
    fi
    if [ "$cross_site_script_uses_domain_names" = "none" ]  ;then
        echo -e "\033[32m Unmodified Medusa build domain name, causing XSS to automatically populate !\033[0m"
    else
        #当前medusa搭建域名
        sed -i "s/127.0.0.1:1234/$cross_site_script_uses_domain_names/g" config.py
        #${cross_site_script_uses_domain_names//\//\/}
        #${parameter/pattern/string}
        #${parameter//pattern/string}
        #将parameter对应值的pattern字符串替换成为string字符串
        #/表示只替换一次
        #//表示全部替换
        sed -i "s/this_is_you_domain_name/$cross_site_script_uses_domain_names/g" Dockerfile
        sed -i "s/http:\/\/127.0.0.1:9999/https:\/\/$cross_site_script_uses_domain_names/g" Vue/faceConfig.js
        echo -e "\033[31m current MEDUSA builds domain name \033[35m--->\033[0m\033[0m$cross_site_script_uses_domain_names"
    fi
    if [ "$domain_name_system_address" = "none" ]  ;then
        echo -e "\033[32m Unmodified DNSLOG configuration can cause this feature unavailable !\033[0m"
    else
        #DNSLOG接收域名
        sed -i "s/dnslog.ascotbe.com/$domain_name_system_address/g" config.py
        sed -i "s/this_is_your_dnslog_name/$domain_name_system_address/g" Dockerfile
        echo -e "\033[31m modify dnslog domain name \033[35m--->\033[0m\033[0m$domain_name_system_address"
    fi
    if [ "$third_party_mail_host" = "none" ]  ;then
        echo -e "\033[32m Unwave to modify a third-party SMTP server, mail sending function is not available !\033[0m"
    else
        #修改第三smtp服务器
        sed -i "s/smtp.163.com/$third_party_mail_host/g" config.py
        echo -e "\033[31m modify third-party SMTP server \033[35m--->\033[0m\033[0m$third_party_mail_host"
    fi
    if [ "$third_party_mail_user" = "none" ]  ;then
        echo -e "\033[32m Unavigified third-party mail server account, mail sending function is not available ~ \033[0m"
    else
        #修改第三方邮件服务器账号
        sed -i "s/ascotbe@163.com/$third_party_mail_user/g" config.py
        echo -e "\033[31m modify a third-party mail server account \033[35m--->\033[0m\033[0m$third_party_mail_user"
    fi
    if [ "$third_party_mail_pass" = "none" ]  ;then
        echo -e "\033[32m Unwind to the third-party mail server secret key, mail delivery function is not available !\033[0m"
    else
        #修改第三方邮件服务器秘钥
        sed -i "s/hello_medusa/$third_party_mail_pass/g" config.py
        echo -e "\033[31m modify the secret key of third-party mail server \033[35m--->\033[0m\033[0m$third_party_mail_pass"
    fi
    if [ "$local_mail_host" = "none" ]  ;then
        echo -e "\033[32m no self-built SMTP server is modified, causing this feature unavailable ! \033[0m"
    else
        #修改自建SMTP服务器,只能传入域名，邮箱@后面的值
        sed -i "s/smtp.ascotbe.com/smtp.$local_mail_host/g" config.py
        sed -i "s/this_is_your_mail_server_domain_name/$local_mail_host/g" Dockerfile
        echo -e "\033[31m modify self-built SMTP server \033[35m--->\033[0m\033[0m smtp.$local_mail_host"
    fi
    if [ "$local_mail_user" = "none" ]  ;then
        echo -e "\033[32m no self-built server mailbox is not modified, causing this feature unavailable ~ \033[0m"
    else
        #修改自建服务器邮箱
        sed -i "s/ascotbe@ascotbe.com/$local_mail_user/g" config.py
        echo -e "\033[31m modify the self-built server mailbox \033[35m--->\033[0m\033[0m$local_mail_user"
    fi
    if [ "$server_ip" = "none" ]  ;then
        echo -e "\033[32m Uncomplete to the server IP address, will cause the dnslog function to not be available !\033[0m"
    else
        #本机服务器代码
        sed -i "s/192.168.1.1/$server_ip/g" config.py
        echo -e "\033[31m This machine IP has been set to \033[35m--->\033[0m\033[0m$server_ip"
    fi
    sleep 3
    tar zcvf Medusa.tat.gz *
    sudo docker build -t medusa_web .
    sudo docker run -d -i -t --name  medusa --net=host medusa_web
fi
