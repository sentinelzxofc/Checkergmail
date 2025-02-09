#!/bin/bash

pkg update -y
pkg upgrade -y
pkg install python -y
pkg install git -y
pip install --upgrade pip
pip install smtplib socket colorama requests

python3 gmail_checker.py