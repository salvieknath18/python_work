infile = open('TestFile2.txt','r')
content2 = infile.read()
infile = open('TestFile2.txt','r')
content1 = infile.readlines()

##------ Number of lines words and characters ---------
print "total number of lines", len(content1)
print "total number of lines", content2.count("\n")+1
print "total number of words", content2.count(" ")+content2.count("\n")+1
print "total number of characters", len(content2)

##------ Uppercase the content---------
content3 = content2.upper()

##------ Count the words---------
content4 = list(set(content2.split()))
for i in range(len(content4)):
    print "word %r is %r times " %(content4[i], content2.split().count(content4[i]))

##------ Reverse the content ---------
content5 = content2[::-1]

outfile = open('TestFile2_Copy.txt','w')
outfile.writelines(content3)
outfile.writelines('\n')
outfile.writelines(content5)
outfile.flush()
outfile.close()
