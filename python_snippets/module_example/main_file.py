from module_example.file1 import C1
from module_example.file2 import f2
import sys
import os

print(os.getcwd())
os.chdir("")
def my_function():
    print("This is my main function")

if __name__ == "__main__":
    C1().f1()
    f2()
    my_function()