import socket
from threading import Thread, Timer
import time
import SocketServer
import os, subprocess
import sys
import math, random
import copy

try:
        check_output = subprocess.check_output
except AttributeError:
        def check_output(*popenargs, **kwargs):
                if 'stdout' in kwargs:
                        raise ValueError('stdout argument not allowed, it will be overridden.')
                process = subprocess.Popen(stdout=subprocess.PIPE, *popenargs, **kwargs)
                output, unused_err = process.communicate()
                retcode = process.poll()
                if retcode:
                        cmd = kwargs.get("args")
                        if cmd is None:
                                cmd = popenargs[0]
                        raise CalledProcessError(retcode, cmd, output=output)
                return output
send=sys.argv[1].rstrip()

def client(ip, port, message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    try:
        sock.sendall(message)
        response = sock.recv(1024)
        return response
    finally:
        sock.close()

if __name__ == "__main__":
    print client("131.247.2.242", 5360, send).rstrip()

