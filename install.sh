#!/bin/bash
#if [ $# != 10 ] ; then
#    echo "Please enter 10 parameters, use the default value, use 'none' instead of the input"
#    exit 1;
#fi
func() {
    echo "Usage:"
    echo "install.sh [-u WebDomain] [-d DNSLogDomain] [-s LocalSMTP]"
    echo "Description:"
    echo "WebDomain,web端的域名."
    echo "DNSLogDomain,DNSLog域名."
    echo "LocalSMTP,自建SMTP服务器."
    exit -1
}
while getopts 'u:d:s:h' OPT; do
    case $OPT in
        u) cross_site_script_uses_domain_names="$OPTARG";;#web端的域名
        d) domain_name_system_address="$OPTARG";;#DNSLog域名
        s) local_mail_host="$OPTARG";;#自建SMTP服务器
#        m) third_party_mail_host="$OPTARG";;#第三方smtp服务器
#        n) third_party_mail_user="$OPTARG";;#第三方smtp服务器账号
#        k) third_party_mail_pass="$OPTARG";;#第三方smtp服务器秘钥
        h) func;;
    esac
done

#判断是否传入最基础的两个参数
if [ "$cross_site_script_uses_domain_names" = "" ] || [ "$domain_name_system_address" = "" ] ;then
    func
else
    echo -e "\033[32m Installing..... \033[0m"
fi

server_ip=`curl ip.0xc2.cn`
if [[ `uname` == 'Linux' ]]; then
    sudo apt update
    sudo apt install git -y
    sudo apt install docker.io -y
    sudo apt install pwgen -y
    sudo systemctl start docker
    redis_password=`pwgen 26 -c 1 -n 5`
    secret_key_required_for_account_registration=`pwgen 40 -c 1 -n 5`
    forget_password_key=`pwgen 40 -c 1 -n 5`

    #当前medusa搭建域名
    sed -i "s/127.0.0.1:1234/$cross_site_script_uses_domain_names/g" manage.py
    #${cross_site_script_uses_domain_names//\//\/}
    #${parameter/pattern/string}
    #${parameter//pattern/string}
    #将parameter对应值的pattern字符串替换成为string字符串
    #/表示只替换一次
    #//表示全部替换
    sed -i "s/this_is_you_domain_name/$cross_site_script_uses_domain_names/g" Dockerfile
    sed -i "s/http:\/\/127.0.0.1:9999/https:\/\/$cross_site_script_uses_domain_names/g" Vue/faceConfig.js
    echo -e "\033[31m current MEDUSA builds domain name \033[35m--->\033[0m\033[0m$cross_site_script_uses_domain_names"
    #DNSLOG接收域名
    sed -i "s/dnslog.ascotbe.com/$domain_name_system_address/g" manage.py
    sed -i "s/this_is_your_dnslog_name/$domain_name_system_address/g" Dockerfile
    echo -e "\033[31m modify dnslog domain name \033[35m--->\033[0m\033[0m$domain_name_system_address"

#    if [ "$third_party_mail_host" = "" ]  ;then
#        echo -e "\033[32m Unwave to modify a third-party SMTP server, mail sending function is not available !\033[0m"
#    else
#        #修改第三smtp服务器
#        sed -i "s/smtp.163.com/$third_party_mail_host/g" config.py
#        echo -e "\033[31m modify third-party SMTP server \033[35m--->\033[0m\033[0m$third_party_mail_host"
#    fi
#    if [ "$third_party_mail_user" = "" ]  ;then
#        echo -e "\033[32m Unavigified third-party mail server account, mail sending function is not available ~ \033[0m"
#    else
#        #修改第三方邮件服务器账号
#        sed -i "s/ascotbe@163.com/$third_party_mail_user/g" config.py
#        echo -e "\033[31m modify a third-party mail server account \033[35m--->\033[0m\033[0m$third_party_mail_user"
#    fi
#    if [ "$third_party_mail_pass" = "" ]  ;then
#        echo -e "\033[32m Unwind to the third-party mail server secret key, mail delivery function is not available !\033[0m"
#    else
#        #修改第三方邮件服务器秘钥
#        sed -i "s/hello_medusa/$third_party_mail_pass/g" config.py
#        echo -e "\033[31m modify the secret key of third-party mail server \033[35m--->\033[0m\033[0m$third_party_mail_pass"
#    fi
    if [ "$local_mail_host" = "" ]  ;then
        echo -e "\033[32m no self-built SMTP server is modified, causing this feature unavailable ! \033[0m"
    else
        #修改自建SMTP服务器,只能传入域名，邮箱@后面的值
        sed -i "s/smtp.ascotbe.com/smtp.$local_mail_host/g" manage.py
        sed -i "s/this_is_your_mail_server_domain_name/$local_mail_host/g" Dockerfile
        echo -e "\033[31m modify self-built SMTP server \033[35m--->\033[0m\033[0m smtp.$local_mail_host"
    fi

    #本机服务器代码
    sed -i "s/192.168.1.1/$server_ip/g" manage.py
    echo -e "\033[31m This machine IP has been set to \033[35m--->\033[0m\033[0m$server_ip"
    #修改自建服务器邮箱
    sed -i "s/ascotbe@ascotbe.com/test@$local_mail_host/g" manage.py
    #注册密码key
    sed -i "s/I_will_always_like_SoryuAsukaLangley/$secret_key_required_for_account_registration/g" manage.py
    #redis密码
    sed -i "s/I_will_always_like_AyanamiRei/$redis_password/g" manage.py
    sed -i "s/redis_passwd123/$redis_password/g" Dockerfile
    #忘记密码key
    sed -i "s/I_will_always_like_KatsuragiMisato/$forget_password_key/g" manage.py

    sleep 3
    tar zcvf Medusa.tat.gz *
    sudo docker build -t medusa_web .
    sudo docker run -d -i -t --name  medusa --net=host medusa_web
    sleep 2
    echo -e "\033[31m[ + ] redis password change to \033[35m--->  \033[0m\033[0m$redis_password"
    echo -e "\033[31m[ + ] modify registration required key \033[35m--->  \033[0m\033[0m$secret_key_required_for_account_registration"
    echo -e "\033[31m[ + ] modify the secret required for forgot password \033[35m--->  \033[0m\033[0m$forget_password_key"

fi
