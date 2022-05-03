import re

################## extract digits from string
def extDigit(mainstr):

    listDigits = re.findall("[0-9]", mainstr)
    listNums = re.findall("[0-9]+", mainstr)
    addition = 0
    for num in listNums:
        addition += int(num)

    print(listDigits,listNums, addition)


################## read text file and replace the contact number with '#' and find count the word java in the file
def replacePattern():
    infile = open("sample.txt")
    content = infile.read()
    s = re.sub("[7-9]\d{9}","#"*10,content)
    count = len(re.findall("[jJ]ava[^\w]",content))
    print(s)
    print("java count", count)

replacePattern()