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

class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        data = self.request.recv(1024) # read in data here
        response = check_output("ping -c 1 "+ data +" | grep from", shell=True).split("=")[3].split()[0]
        #cur_thread = threading.current_thread()
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
        time.sleep(1)
    
