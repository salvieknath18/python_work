import os

main_path = r"D:\scodeen\pythondata"

'''
for file in os.listdir(main_path):
    if 'sample' in file:
        with open(os.path.join(main_path, file), 'a') as f:
            f.write("This is sample text file")
'''

for root, dir, files in os.walk(main_path):
    print(root)
    print(dir)
    print(files)




