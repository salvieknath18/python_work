import os, datetime, time 

directory = raw_input("Enter the directory name")
D_path= raw_input("Enter the directory path")

dir_size = 0
for dir,subdir,files in os.walk(D_path+'/'+directory):
    os.chdir(dir)
    for i in files:
       dir_size += os.path.getsize(i)
            
dir_time_in_float = os.path.getmtime(D_path+'/'+directory)
Curren_Time_in_float = time.time()
Current_time_in_all = datetime.datetime.fromtimestamp(Curren_Time_in_float)
timeDiff = Curren_Time_in_float - dir_time_in_float

if timeDiff > (3600 * 24 * 30) and dir_size < 100000:
    print " file or directory is more than 30 days older, Need to remove"
    #os.unlink(D_path+'/'+directory)
else:
    print "file is recently mdified on : ", datetime.datetime.fromtimestamp\
          (dir_time_in_float)
