import paramiko

hostname = "127.0.0.1"
port = 22
user = "Danish"
password = "pythoncode"

try:
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, port=port, username=user, password=password)
    while true:
        try:
            cmd = input("S> ")
            if cmd == "exit": break
            stdin, stdout, stderr = client.exec_command(cmd)
            print(stdout.read().decode())
        except KeyboardInterrupt:
            break
    client.close()
except Exception as err:
    print(str(err))

