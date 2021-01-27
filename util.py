import r2pipe
import sys

r2 = r2pipe.open(sys.argv[1])
r2.cmd("aaa")

def unhex(x):
	return int(x, 16)
