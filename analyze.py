import r2pipe

class Fcn:
	def __init__(self, call_str):
		split = call_str.split(' ')
		self.addr = split[2]
		self.name = split[3]

	def __eq__(self, other):
		return (isinstance(other, self.__class__) and
				self.addr == other.addr and
				self.name == other.name)

	def __hash__(self):
		return hash((self.addr, self.name))

	def __str__(self):
		return self.addr + " " + self.name

	def __repr__(self):
		return self.__str__()

r2 = r2pipe.open("client")
r2.cmd("aaa")

base = "sym.parse_args"

print("#### find calls")

fcns = set(map(Fcn, r2.cmd("axff @ " + base + " | grep '^C'").split('\n')[:-1]))

print(fcns)

print("#### find mov in function")

print(r2.cmd("pif @ " + base + " | fgrep mov"))
