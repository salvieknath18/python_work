import os

directory = raw_input("Enter the directory name")
D_path= raw_input("Enter the directory path")

cnt = 0
for dir,subdir,files in os.walk(D_path+'/'+directory):
    os.chdir(dir)
    for i in files:
       if i.split('.')[1] == 'py':
           cnt += 1

print "Number of python files are {}".format(cnt)
