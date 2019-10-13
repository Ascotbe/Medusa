import requests
def Medusa():
    s=requests.session()
    get=s.get("www.ascotbe.com")
    get.close()