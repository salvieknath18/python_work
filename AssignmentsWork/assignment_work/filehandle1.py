infile = open(r'TestFIle.txt','r')
lrange = len(infile.readlines())
infile = open(r'TestFIle.txt','r')
for i in range(lrange):
	if 'python' in infile.readline():
		print i
