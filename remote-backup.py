import paramiko
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Backup:
    def __init__(self, ip, username, password, port=22):
        self.ip = ip
        self.username = username
        self.password = password
        self.port = port
        self.ssh = None
        self.sftp = None
        self.connect()

    # Connect to the server
    def connect(self):
        try:
            self.ssh = paramiko.client.SSHClient()
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh.connect(self.ip, self.port, self.username, self.password)
            self.sftp = self.ssh.open_sftp()  # Open an SFTP session on the SSH server
        except Exception as e:
            print(e)
            print("Connection Failed")
            self.ssh.close()
    # Close the connection

    def close(self):
        self.ssh.close()

    # Copy a remote file (remote_dir) from the SFTP server to a local directory (local_dir)
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

    # Create a backup object
    backup = Backup(host, username, password, port)
    backup.backup(local_dir, remote_dir)
    backup.close()
