import socket
import threading
import SocketServer
import os, subprocess, time

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

start=time.time()
def client(ip, port, message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    try:
        sock.sendall(message)
        response = sock.recv(1024)
        return response
    finally:
        sock.close()


f=open("Stream", 'a')
class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        data = self.request.recv(1024) # read in data here
        response = None
        try:
                if data[-1] == "P":
                        ds= data.split()
                        if ds[0] =="send":
                                check=open("Stream", 'r')
                                line=check.readline()
                                while line !="":
                                        ls=line.split()
                                        if ls[0] == ds[2]:
                                                client(ds[1], 5360, ds[2] + " " +ds[3])
                                                check.close()
                                                line=""
                                                response = "untaken"
                                        else:
                                                line=check.readline()
                        else:
				t=time.time()-start
                                f.write(data +" " +t+"\n")
                        response = None
                elif data[-1] =="d":
                        data=data.split()
                        f.write(data[0]+" determined by server \n")
                else:
                        response = check_output("sudo bwping "+data +" -b 1000 -s 100 -v 10000 | grep rcvd", shell=True)
                        response = response.split()
                        response =response[12]
        except:
                response = None
        cur_thread = threading.current_thread()
        print response
        self.request.sendall(response)

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

if __name__ == "__main__":
    HOST, PORT = check_output("hostname -i",shell=True).rstrip() , 5360
    print HOST,PORT

    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)


    # Start a thread with the server -- that thread will then start one
    # more thread for each request
    server_thread = threading.Thread(target=server.serve_forever)
    # Exit the server thread when the main thread terminates
    server_thread.daemon = True
    server_thread.start()
    print "Server loop running in thread:"
    while True:
        time.sleep(.01)
    


