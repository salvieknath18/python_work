import os

basedir = raw_input("Enter the directory")
for dir,subdir,files in os.walk(basedir):
    #print dir
    #print subdir
    #print files
    os.chdir(dir)
    for i in files:
        #print files[i] + str(os.basedir.getsize(files[i]))
        #print i, os.path.getsize(i)
        if os.path.getsize(i) == 0:
            print "file to delete is ", i
            #os.unlink(i)
