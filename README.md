## Remote Backup Script

## Description

---

Python script that backs up files from a remote server to your local machine. It uses the
[Paramiko library](https://www.paramiko.org) to connect to the remote server via SSH and
then uses the SFTP protocol to transfer the files to your local machine. The script can be
run manually or scheduled to run automatically using the Windows Task Scheduler or the
Linux Cron utility.

## Requirements

---

-   Python 3.6 or higher
-   Paramiko library

## Installation

---

-   Install Python 3.6 or higher
-   Install the Paramiko library using `pip install paramiko`

## Usage

---

-   Clone the repository using `git clone https://github.com/jim3/remote-backup-script.git`
