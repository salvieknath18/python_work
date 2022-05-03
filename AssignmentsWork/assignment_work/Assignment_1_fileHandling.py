file_name = raw_input("Enter the file name: ")
Directory = raw_input("Enter the directory of a file: ")

infile = open(Directory+'/'+file_name, 'r')
content = infile.read()

base_file_name = file_name.split('.')[0]

outfile = open(Directory+'/'+base_file_name+'.bckp', 'w')
outfile.write(content)
outfile.flush()
outfile.close()

