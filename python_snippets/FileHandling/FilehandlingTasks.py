'''
FIle Handling Tasks
'''
'''
****************************************              Create Backup File
'''

file_name = input("Enter the file name: ")
Directory = input("Enter the directory of a file: ")

infile = open(Directory+'/'+file_name, 'r')
content = infile.read()

base_file_name = file_name.split('.')[0]

outfile = open(Directory+'/'+base_file_name+'.bckp', 'w')
outfile.write(content)
outfile.flush()
outfile.close()


'''
****************************************          Delete Empty files in directory
'''

import os

basedir = input("Enter the directory")
for dir,subdir,files in os.walk(basedir):
    #print dir
    #print subdir
    #print files
    os.chdir(dir)
    for i in files:
        #print files[i] + str(os.basedir.getsize(files[i]))
        #print i, os.path.getsize(i)
        if os.path.getsize(i) == 0:
            print("file to delete is ", i)
            #os.unlink(i)

'''
************************   Accept directory name from user and remove if it is modify 30days older and if size is 100kb(use fun m10)
'''

import os, datetime, time

directory = input("Enter the directory name")
D_path = input("Enter the directory path")

dir_size = 0
for dir, subdir, files in os.walk(D_path + '/' + directory):
    os.chdir(dir)
    for i in files:
        dir_size += os.path.getsize(i)

dir_time_in_float = os.path.getmtime(D_path + '/' + directory)
Curren_Time_in_float = time.time()
Current_time_in_all = datetime.datetime.fromtimestamp(Curren_Time_in_float)
timeDiff = Curren_Time_in_float - dir_time_in_float

if timeDiff > (3600 * 24 * 30) and dir_size < 100000:
    print(" file or directory is more than 30 days older, Need to remove")
    # os.unlink(D_path+'/'+directory)
else:
    print("file is recently mdified on : ", datetime.datetime.fromtimestamp \
        (dir_time_in_float))



'''
***********************************           Find python files in entered directory
'''

import os

directory = input("Enter the directory name")
D_path= input("Enter the directory path")

cnt = 0
for dir,subdir,files in os.walk(D_path+'/'+directory):
    os.chdir(dir)
    for i in files:
       if i.split('.')[1] == 'py':
           cnt += 1

print("Number of python files are {}".format(cnt))