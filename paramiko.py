import getpass 
import paramiko

print(**************************************)
print(************ianwolf99*****************)
print(*****conect and exec cmd,port22*******)
print(**************************************)
HOSTNAME = 127.0.0.1
PORT = 22

def  run_ssh_cmd(username , password , cmd hostname= HOSTNAME port=PORT):
    ssh_client = paramiko.ssh_client()
    ssh_client.set_missing_host_key_policy(\paramiko.AutoAddPolicy())
    ssh_client.load_system_host_keys()
    ssh_client.connect(hostname,port,username,password)
    stdin, stdout, stderr = ssh_client.exec_command(cmd)
    print(stdout.read())

if __name__ == '__main__':
    username = input("Enter username:")
    password = getpass.getpass(prompt="Enter password:")
    cmd = input("Enter the command to run")
    run_ssh_cmd(username,password,cmd)    