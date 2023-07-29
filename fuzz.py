#!/usr/bin/env python
# Designed for use with boofuzz v0.0.9
from boofuzz import *

def main():
    session = Session(
        target=Target(
            connection=SocketConnection("192.168.94.1", 8000, proto='tcp')
        ),
    )

    s_initialize(name="Request")
    with s_block("Request-Line"):
        s_group("Method", ['POST'])
        s_delim(" ", name='space-1')
        s_string("/index.html", name='Request-URI')
        s_delim(" ", name='space-2')
        s_string('HTTP/1.1', name='HTTP-Version')
        s_static("\r\n", name="Request-Line-CRLF")
    s_static("\r\n", "Request-CRLF")

    session.connect(s_get("Request"))

    session.fuzz()


if __name__ == "__main__":
    main()