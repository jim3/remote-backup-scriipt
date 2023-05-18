import paramiko
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Backup:
    # Constructor: Initialize the object with the IP address, username, password, and port
    def __init__(self, ip, username, password, port=22):
        self.ip = ip
        self.username = username
        self.password = password
        self.port = port
        self.ssh = None
        self.sftp = None
        self.connect()

    # Connect to the server using SSH and open an SFTP session
    def connect(self):
        try:
            # Create an SSH client
            self.ssh = paramiko.client.SSHClient()
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            # Connect to the host
            self.ssh.connect(self.ip, self.port, self.username, self.password)
            # Create an SFTP session
            self.sftp = self.ssh.open_sftp()
        except Exception as e:
            print(e)
            print("Connection Failed")
            self.ssh.close()

    def close(self):
        self.ssh.close()

    # Copy a remote file from `remote_dir` to a `local_dir`
    def backup(self, local_dir, remote_dir):
        try:
            self.sftp.stat(remote_dir)
        except FileNotFoundError:
            print("Remote path does not exist")
            return
        except Exception as e:
            print(e)
            return
        self.sftp.get(remote_dir, local_dir)
        print("File copied successfully")


# Use environment variables to store the data
if __name__ == "__main__":
    host = os.environ.get("HOST")
    username = os.environ.get("USERNAME")
    password = os.environ.get("PASSWORD")
    port = os.environ.get("PORT")
    local_dir = os.environ.get("LOCAL_DIR")
    remote_dir = os.environ.get("REMOTE_DIR")

    # Create a backup object and call the backup method
    backup = Backup(host, username, password, port)
    backup.backup(local_dir, remote_dir)
    backup.close()

# Run the script
# `python3 remote-backup.py``
