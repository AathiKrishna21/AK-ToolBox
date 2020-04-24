import requests
import sys         
import threading       
        
def call(url,words):
    for subdomain in words:
        subdomain=subdomain.rstrip()
        url_list=url.split('://')
        new_url=url_list[0]+ '://' + subdomain + '.' + url_list[1]
        try:
            res=requests.get(new_url)
            print(f'{new_url}')
        except:
            pass
        
def main():
    words=open(sys.argv[2],'r') 
    fread=words.readlines()
    url=sys.argv[1]
    thread=sys.argv[3]
    for i in range(0,len(fread),thread):
        wrap=fread[i:i+thread]
        th=threading.Thread(target=call,args=url,wrap)
        th.start()
        threads.append(th)
    for thread in threads:
        thread.join()
    words.close()
    

if __name__=="__main__":
    print("WELCOME to AK's SUBDOMAIN BRUTE FORCER".center(80,'-'))
    if len(sys.argv)==4: 
        main()
    else:
        print("USE : {sys.arg[0]} <url> <wordlist path> <thread>")
    
    

    