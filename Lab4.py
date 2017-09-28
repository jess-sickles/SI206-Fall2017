import re
f = open('mbox-short.txt')
f = f.readlines()
newlist= list()
for line in f:
	line = line.rstrip()
	email = re.findall('From',line)
	if len(email) != 0: 
		print(line)