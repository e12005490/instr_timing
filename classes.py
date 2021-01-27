from util import r2, unhex

class Function:
	def __init__(self, name):
		self.addr = unhex(r2.cmd("afo " + name))
		self.name = name
		self.end = max(map(unhex, r2.cmd("afbr" + name).split('\n')[:-1]))

	def __eq__(self, other):
		return isinstance(other, self.__class__) and self.name == other.name

	def __hash__(self):
		return hash(self.name)

	def __str__(self):
		return self.name

	def __repr__(self):
		return self.__str__()

	def instructions(self, like = None):
		cond = " | grep " + like if like else ""
		pdi = [i for i in r2.cmd("pdi  @ " + self.name + cond).split('\n')[:-1]
				if i[-1] != ':']
		print(pdi)
		return [i for i in map(Instruction, pdi)
				if self.addr <= i.addr and i.addr <= self.end]

	def called_functions(self):
		calls = r2.cmd("axff @ " + self.name + " | egrep '^C'").split('\n')[:-1]
		return set(map(lambda s: Function(s.split()[-1]), calls))

class Instruction:
	def __init__(self, instr_str):
		split = instr_str.split(None, 2)
		self.addr = unhex(split[0])
		self.instr = split[2]

	def __eq__(self, other):
		return (isinstance(other, self.__class__) and
				self.addr == other.addr and
				self.instr == other.addr)

	def __hash__(self):
		return hash((self.addr, self.instr))

	def __str__(self):
		return hex(self.addr) + " " + self.instr

	def __repr__(self):
		return self.__str__()
