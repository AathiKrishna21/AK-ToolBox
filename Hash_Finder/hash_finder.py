import hashlib


def wor(n,m):
    print("Word to hash Converter".center(75,'*'))
    word=input("Enter the word :  ")
    en=word.encode('utf-8')
    if(m==1):
        digest=hashlib.md5(en.strip()).hexdigest()
    elif(m==2):
        digest=hashlib.sha1(en.strip()).hexdigest()
    elif(m==3):
        digest=hashlib.sha224(en.strip()).hexdigest()
    elif(m==4):
        digest=hashlib.sha256(en.strip()).hexdigest()
    elif(m==5):
        digest=hashlib.sha384(en.strip()).hexdigest()
    elif(m==6):
        digest=hashlib.sha512(en.strip()).hexdigest()       
    print("the hash function of the word is : "+digest)
    print("THANK YOU".center(75,'*'))
    

def has(n,m):  
    print("Hash to word Converter".center(75,'*'))  
    ha=input("Enter the hash : ")
    fname=input("Enter the name of password list : ") 
    flag=0   
    try:
        file=open(fname,"r")
        fread=file.readlines()
        for word in fread:
                word=word.rstrip()
                en=word.encode('utf-8')
                if(m==1):
                    digest=hashlib.md5(en.strip()).hexdigest()
                elif(m==2):
                    digest=hashlib.sha1(en.strip()).hexdigest()
                elif(m==3):
                    digest=hashlib.sha224(en.strip()).hexdigest()
                elif(m==4):
                    digest=hashlib.sha256(en.strip()).hexdigest()
                elif(m==5):
                    digest=hashlib.sha384(en.strip()).hexdigest()
                elif(m==6):
                    digest=hashlib.sha512(en.strip()).hexdigest()
                if digest == ha:
                    print("password found")
                    print("password is: "+word)
                    flag=1
                    break
        if flag==0:
                print("Sorry!, password is not in the list")
                print("THANK YOU".center(75,'*'))
        file.close()            
    except Exception as e:    
        print(str(e).center(75,'-'))
        print("THANK YOU".center(75,'*'))
        quit()
    


def main():
    print("Welcome to AK's hash converter".center(75,'-'))
    print("[1]Press 1 to convert word into hash")
    print("[2]Press 2 to convert hash into word")
    n=int(input("Your choice :  "))
    print("Choose your hash type:")
    print("[1]md5 hash")
    print("[2]sha1 hash")
    print("[3]sha224 hash")
    print("[4]sha256 hash")
    print("[5]sha384 hash")
    print("[6]sha512 hash")
    m=int(input("hash type :  "))
    if (n==1):
        wor(n,m)
    elif n==2:
        has(n,m)
    print("".center(75,'-'))

    
# Driver program 
if __name__ == "__main__": 
    main()     
                    
