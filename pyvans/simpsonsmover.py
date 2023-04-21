#!/usr/bin/python3
import paramiko

# log results
paramiko.util.log_to_file('/tmp/paramiko.log')

# Open a transport
hosts = ["10.10.2.3", "10.10.2.4", "10.10.2.5"]
users = ["bender", "fry", "zoidberg"]
port = 22
passw = "alta3"

for host, user in zip(hosts, users):
    transport = paramiko.Transport((host, port))
    transport.connect(username = user, password = passw)

    sftp = paramiko.SFTPClient.from_transport(transport)

    # Upload - sftp.put(src, dest)
    sftp.put("/home/student/mycode/pyvans/simpsons-ans.txt", "simpsons-ans.txt")
    sftp.put("/home/student/mycode/pyvans/simpsons-py.txt", "simpsons-py.txt")

    # Close
    sftp.close()
    transport.close()
