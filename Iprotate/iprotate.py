import requests
from time import sleep
from stem import Signal
from stem.control import Controller
import threading


class IProtator:

	def __init__(self,url,method,thread_lmt,response_handler,sleep_time=10,headers={},rotateIP=True):
		self.url     = url
		self.method  = method
		self.thread_lmt = thread_lmt
		self.response_handler = response_handler
		self.sleep_time = sleep_time
		self.headers = headers
		self.rotateIP = rotateIP
		self.thread_handler()


	def thread_handler(self):

		threads = []			
		argumets =[]
		count = 0


		for urld, err, data in self.url:
				
				count+=1
				if len(data) == 0:
					argumets = [urld,self.method,self.headers]
				else:
					argumets = [urld,self.method,self.headers,data,err]
				
				thread = threading.Thread(target=self.try_request,args=argumets) 
				thread.start()
				threads.append(thread)

				if count % self.thread_lmt == 0:

					for thread in threads:
						thread.join()
					if self.rotateIP:
						sleep(self.sleep_time)
						self.changeIP()

					threads.clear()

		for thread in threads:
			thread.join()

	def try_request(self,*,url,method,headers,payload={},err):

	    proxies = {}
	    proxies["http"] = "socks5h://localhost:9050"
	    proxies["https"] = "socks5h://localhost:9050"

	    try:
	        res = requests.request(method,url,data=payload,proxies=proxies,headers=headers)
	    except Exception as e:
	        print(str(e))
	    else:
	        thread = threading.Thread(target=self.response_handler,args=[res,err,payload])
	        thread.start()


	def changeIP(self):
	    with Controller.from_port(port=9051) as controller:
	        controller.authenticate(password="")
	        controller.signal(Signal.NEWNYM)