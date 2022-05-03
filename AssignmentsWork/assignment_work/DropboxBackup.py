import zipfile, os

basedir = r'F:\Dropbox'
os.chdir(basedir)

zf = zipfile.ZipFile(r'C:\Users\eknath\Desktop\test\Dropbox.zip','w')

##for filetozip in os.listdir(basedir):
##        zf.write(filetozip)
        
for dir,subdir,files in os.walk(basedir):
    for filetozip in os.listdir(dir):
        os.chdir(dir)
        zf.write(dir + '/' + filetozip)

zf.close()
    
