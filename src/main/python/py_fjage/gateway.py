import sys, json, socket
import multiprocessing as mp

class Gateway:

    # supported json keys
    keys = ["id", "action", "inResponseTo", "agentID", "agentIDs", "service", "services", "answer", "message", "relay"]

    # json message
    json_msg = dict()

    # queue
    q = mp.Queue()

    # create socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    pid = 0

    # constructor
    def __init__(self, ip, port):
        # connect to fjage master container
        try:
            self.s.connect((ip, port))
        except:
            #print "Cannot connect to remote server, exiting program"
            sys.exit(0)
            pass;

    # receive process
    def recv_proc(self, q):
        self.s.setblocking(0)
        rmsg = ""

        while 1:
            try:
                c = self.s.recv(1)
                rmsg = rmsg + c
                if c == '}':
                    #print rmsg
                    #put incoming message to queue
                    q.put(rmsg)
                    rmsg = ""
            except:
                pass;

    # start the receive process as another process
    def start_recv(self):
        recv = mp.Process(target=self.recv_proc, args=(self.q,))
        recv.start()

    # destructor
    def __del__(self):
        try:
            self.s.close
        except:
            pass

        try:
            self.recv.terminate()
        except:
            pass

    # create json message
    def create_msg(self, key, value):
        # sanity check
        if key not in self.keys:
            return
        # add to json message
        self.json_msg[key] = value

    def get_msg(self):
        return self.json_msg

##################

    # shutdown master container
    def shutdown(self):
        msg = {"action": "shutdown"}
        self.s.sendall(json.dumps(msg) + '\n')
        #TODO: Kill child process

    # send the json message
    def send(self):
        #msg = {"id": message.id, "action": message.action, "agentID": message.agentID}
        print json.dumps(self.json_msg)
        self.s.sendall(json.dumps(self.json_msg) + '\n')

    # return received response message, null if none available.
    def receive(self):
        if self.q.empty():
            return "null"
        else:
            return self.q.get()

    # return received response message, null if none available.
    def receive_with_tout(self, tout):
        try:
            rmsg = self.q.get(timeout=tout)
        except:
            print "Queue timeout"
            return
        return rmsg

    # return received response message, null if none available.
    def request(self, msg, tout):
        print json.dumps(self.json_msg)
        self.s.sendall(json.dumps(msg) + '\n')
        try:
            rmsg = self.q.get(timeout=tout)
        except:
            print "Queue timeout"
            return
        return rmsg
