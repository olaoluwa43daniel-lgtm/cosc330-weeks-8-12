# COSC 330 Systems Programming I

This repository documents the Week 8 Ubuntu and Python assignments and the Week 12 EC2-to-S3 progress report.

| Folder | Contents |
| --- | --- |
| [Week8_Homework](Week8_Homework) | Original Makefile, Python and Bash exercises, and original local test notes. |
| [Systemd_Python_Assignment](Systemd_Python_Assignment) | Separate Week 8 Python-to-systemd assignment, unit files, and original test notes. |
| [week12](week12) | Bash script for the public S3 listing verified from Ubuntu EC2. |
| [evidence](evidence) | Five screenshots from the live Ubuntu EC2 terminal. |
| [report](report) | Word and PDF reports with figure captions and results. |

## Run the Week 8 homework

On Ubuntu with Python 3, GNU Make, and Bash installed:

```bash
cd Week8_Homework
make hello
make q1
make q2
make q3
```

The historical README and AWS setup notes describe the state before the EC2 rerun. The current report and screenshots document the rerun.

## Run the Week 12 test

From the repository root on Ubuntu EC2 with the AWS CLI installed:

```bash
bash week12/ec2-to-s3.sh
```

The command lists NOAA's public GOES-19 S3 bucket using an unsigned request. The test verifies read access. [NOAA GOES dataset](https://registry.opendata.aws/noaa-goes/)
