import sys
import random
import math
from optparse import OptionParser
from custom_rand import CustomRand
class Flow:
	def __init__(self, src, dst, size, t):
		self.src, self.dst, self.size, self.t = src, dst, size, t 
	def __str__(self): #the third parameter is priorityGroup
		#return "%d %d 3 100 %d %.9f"%(self.src, self.dst, self.size, self.t)
		if self.size < 10000:
			return "%d %d 0 100 %d %.9f"%(self.src, self.dst, self.size, self.t)
		elif self.size > 10000 and self.size < 50000:
			return "%d %d 1 100 %d %.9f"%(self.src, self.dst, self.size, self.t)
		elif self.size > 50000 and self.size < 200000:
			return "%d %d 2 100 %d %.9f"%(self.src, self.dst, self.size, self.t)
		elif self.size > 200000 and self.size < 1000000:
			return "%d %d 3 100 %d %.9f"%(self.src, self.dst, self.size, self.t)
		elif self.size > 1000000 and self.size < 2000000:
			return "%d %d 4 100 %d %.9f"%(self.src, self.dst, self.size, self.t)
		elif self.size > 2000000 and self.size < 5000000:
			return "%d %d 5 100 %d %.9f"%(self.src, self.dst, self.size, self.t)
		elif self.size > 5000000 and self.size < 10000000:
			return "%d %d 6 100 %d %.9f"%(self.src, self.dst, self.size, self.t)
		elif self.size > 10000000:
			return "%d %d 7 100 %d %.9f"%(self.src, self.dst, self.size, self.t)
                else:
                    return ""

def translate_bandwidth(b):
	if b == None:
		return None
	if type(b)!=str:
		return None
	if b[-1] == 'G':
		return float(b[:-1])*1e9
	if b[-1] == 'M':
		return float(b[:-1])*1e6
	if b[-1] == 'K':
		return float(b[:-1])*1e3
	return float(b)

def poisson(lam):
	return -math.log(1-random.random())*lam

if __name__ == "__main__":
	port = 80
	parser = OptionParser()
	parser.add_option("-c", "--cdf", dest = "cdf_file", help = "the file of the traffic size cdf", default = "uniform_distribution.txt")
	parser.add_option("-n", "--nhost", dest = "nhost", help = "number of hosts",default=320)
	parser.add_option("-p", "--npg", dest = "npg", help = "number of priority groups", default=8)
	parser.add_option("-l", "--load", dest = "load", help = "the percentage of the traffic load to the network capacity, by default 0.3", default = "0.3")
	parser.add_option("-b", "--bandwidth", dest = "bandwidth", help = "the bandwidth of host link (G/M/K), by default 10G", default = "10G")
	parser.add_option("-t", "--time", dest = "time", help = "the total run time (s), by default 10", default = "10")
	options,args = parser.parse_args()

	base_t = 2000000000

	if not options.nhost:
		print ("please use -n to enter number of hosts")
		sys.exit(0)
	nhost = int(options.nhost)
	npg = int(options.npg)
	load = float(options.load)
	bandwidth = translate_bandwidth(options.bandwidth)
	time = float(options.time)*1e9 # translates to ns
	if bandwidth == None:
		print( "bandwidth format incorrect")
		sys.exit(0)

	fileName = options.cdf_file
	file = open(fileName,"r")
	lines = file.readlines()
	# read the cdf, save in cdf as [[x_i, cdf_i] ...]
	cdf = []
	for line in lines:
		x,y = map(float, line.strip().split(' '))
		cdf.append([x,y])

	# create a custom random generator, which takes a cdf, and generate number according to the cdf
	customRand = CustomRand()
	if not customRand.setCdf(cdf):
		print ("Error: Not valid cdf")
		sys.exit(0)

	f_list = []
	avg = customRand.getAvg()
	avg_inter_arrival = 1/(bandwidth*load/8./avg)*1000000000
	# print avg_inter_arrival
	for i in range(nhost):
		t = base_t
		while True:
			inter_t = int(poisson(avg_inter_arrival))
			t += inter_t
			dst = random.randint(0, nhost-1)
			while (dst == i):
				dst = random.randint(0, nhost-1)
			if (t > time + base_t):
				break
			size = int(customRand.rand())
			if size <= 0:
				size = 1
			f_list.append(Flow(i, dst, size, t * 1e-9))

	f_list.sort(key = lambda x: x.t)
	print( len(f_list))
	for f in f_list:
            if f is not None:
                print (f)

