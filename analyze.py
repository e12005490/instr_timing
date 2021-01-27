import sys
from classes import *
from util import r2, unhex

base = Function(sys.argv[2])

print("#### find calls")

fcns = base.called_functions()
print(fcns)

print("#### find instructions in function")

instr = base.instructions()
print("\n".join(map(str, instr)))
