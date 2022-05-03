'''
FIle Handing Basic Operations
'''

'''
Modification in content of the file
'''

infile = open('TestFile2.txt','r')
content2 = infile.read()
infile = open('TestFile2.txt','r')
content1 = infile.readlines()

##------ Number of lines words and characters ---------
print("total number of lines", len(content1))
print("total number of lines", content2.count("\n")+1)
print("total number of words", content2.count(" ")+content2.count("\n")+1)
print("total number of characters", len(content2))

##------ Uppercase the content---------
content3 = content2.upper()

##------ Count the words---------
content4 = list(set(content2.split()))
for i in range(len(content4)):
    print("word %r is %r times " %(content4[i], content2.split().count(content4[i])))

##------ Reverse the content ---------
content5 = content2[::-1]

outfile = open('TestFile2_Copy.txt','w')
outfile.writelines(content3)
outfile.writelines('\n')
outfile.writelines(content5)
outfile.flush()
outfile.close()

'''
Python File Modes

Mode	Description
'r'	Open a file for reading. (default)
'w'	Open a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
'x'	Open a file for exclusive creation. If the file already exists, the operation fails.
'a'	Open for appending at the end of the file without truncating it. Creates a new file if it does not exist.
't'	Open in text mode. (default)
'b'	Open in binary mode.
'+'	Open a file for updating (reading and writing)

f = open("test.txt")      # equivalent to 'r' or 'rt'
f = open("test.txt",'w')  # write in text mode
f = open("img.bmp",'r+b') # read and write in binary mode
#############################################################################
1.For listing a directory
	os.listdir()
2.to get current directory
	print(os.getcwd())
3.To change directory
	os.chdir('C:\\Python33')
4.To rename file name
	os.rename('test-->file name','new_one-->new file name')
5.Removing Directory or File
	os.remove('old.txt')
'''
