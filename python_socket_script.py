
# Import socket module 
import socket                
  
# Create a socket object 
s = socket.socket()          
  
# Define the port on which you want to connect 
port = 1025
  
# connect to the server on local computer 
#s.connect(('127.0.0.1', port))
print("hi")
try:
  s.connect(('192.168.98.94', port)) 
except:
    while True:
        if (s.connect(('192.168.98.94', port)) != True ):
            break
        print("trying to connect")
        
  
# receive data from the server 

jatin = s.recv(4096)

if len(jatin)>0:
    res=str(jatin)
    print(res[2:len(res)-1])

def values():
  for i in range(0,6):
    inp=input("enter value")
    s.send(bytes(inp, 'utf-8'))
    jatin = s.recv(4096)
    if len(jatin)>0:
        res=str(jatin)
        print(res[2:len(res)-1])
        
    

values()
    
#s.close()        

