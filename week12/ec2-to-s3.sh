#!/usr/bin/env bash
set -euo pipefail
export AWS_PAGER=''
printf 'COSC 330 - Week 12 | Ubuntu EC2 to Amazon S3\n'
grep '^PRETTY_NAME=' /etc/os-release
python3 --version
make --version | sed -n '1p'
aws --version
printf '\n$ aws s3 ls --no-sign-request --region us-east-1 s3://noaa-goes19/\n'
aws s3 ls --no-sign-request --region us-east-1 s3://noaa-goes19/ | sed -n '1,8p'
printf '\nPASS: EC2 received the public S3 bucket listing.\n'