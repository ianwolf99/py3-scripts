import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
target_host = str(input("Enter hostname to banner_grab:"))
target_port = 80
s.connect(target_host,target_port)

def banner_grabber(s):
    try:
        s.send('GET HTTP/ 1.1 \r\n')
        ret = s.recv(1024)
        print("[+]",str(ret))
        return
    except Exception as error:
        print("NOTHING GRABBED",str(error))
        return    
