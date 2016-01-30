from py_fjage import gateway as gy
import time, sys

try:
	g1 = gy.Gateway('localhost', 5081)
except:
	print "Cannot connect to server"
	sys.exit(0)

g1.start_recv()

'''
g1.create_msg("id", 1)
g1.create_msg("action", "containsAgent")
g1.create_msg("agentID", "shell")
g1.send()

time.sleep(1)

print(g1.receive())
'''

'''
g1.create_msg("id", 1)
g1.create_msg("action", "containsAgent")
g1.create_msg("agentID", "shell")
print(g1.request(g1.get_msg(), 1))
'''

print(g1.receive_with_tout(5))

g1.shutdown()
