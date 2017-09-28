import re
f = open('mbox-short.txt')
newlist= list()
for line in f:
	line = line.rstrip()
	email = re.findall(' ^From:',line)
	if len(email) != 1: continue
	newlist.append(email)
	print(email)