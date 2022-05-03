import os

print(os.getcwd()) #current working directory
print(os.path.abspath('.'))
print(os.listdir('.'))  #get file list of current worlking directory

''' File Commands for OS
file = os.popen('filename.txt', 'w') 
file.write("Hello")
#os.close(file)
os.rename('filename.txt','New.txt')
'''

cmd = "python --version"

returned_value = os.system(cmd)  
print('returned value:', returned_value)
