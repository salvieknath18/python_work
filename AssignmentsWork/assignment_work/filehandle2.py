path = raw_input('enter the path')
fname = raw_input('enter the filr name')
firstname = fname
infile = open(path+'/'+fname,'r')
content = infile.read()
print content
outfile = open(path+'/'+fname+'.bckp','w')
outfile.write(content)
outfile.flush()
