import math

def parse(fileName):
	datafile = open(fileName, 'r')
	data = []
	for line in datafile:
		data.append(line)
		#print(line)	
	data = list(map(float, data))
	datafile.close()
	return data

def mean(data):
	length = len(data)
	avg = sum(data)/length
	return avg

def stdd(data):
	length = len(data)
	avg = mean(data)
	innerSum = 0
	for i in data:
		innerSum = innerSum + math.pow((i - avg), 2) 
	stdd = math.sqrt((1/(length-1))*innerSum)
	return stdd
def sdom(data, stdd):
	length = len(data)
	sdom = stdd/(math.sqrt(length))
	return sdom
data = parse("hw4.txt")
print ("{0} is the mean. {1} is the std d. {2} is the SDOM.".format(mean(data), stdd(data), sdom(data, stdd(data))))
