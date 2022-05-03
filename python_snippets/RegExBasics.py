import re, urllib

#Fibonacci Series
def fib(n):
    a=1
    b=1
    c=list([1,1])
    for i in range(2,n+1):
       c.append(a+b)
       a = b
       b = c[-1]

    return c
#print(fib(5))


#Rotational String
def isrotational(substr,mainstr):
    mainstr = mainstr + mainstr[0:len(substr)]
    if mainstr.find(substr)==-1:
        print("Not a Rotational Field")
    else:
        print("Yes this is Rotational String")
#isrotational('ekka','kasachcdcoicjek')


#Regular Expressions
"""
Important functions in re module
re.match() give the single match object at the begining
re.compile() gives compiled pattern of substring
re.fullmatch() matches the complete string
re.finditr() gives the all matched objects(from object can get start, end and pattern groups)
re.search() give the single match object at the begining
re.findall() gives the all occurrence of the match returns list of occurrence
re.sub() substitute the one pattern with another in the string re.sub(pattern,replacement,mainstring)
re.subn() same as sub() but it also return number of replacements
re.split() split the main string with particular pattern and return list of split values
we can add parameter re.IGNORECASE in search() function to have case insensitive search
"""
def findstr(substr,mainstr):
    count = 0
    pattern = re.compile(substr)  # Compile a pattern in to regExobject
    matcher = pattern.finditer(mainstr)  # gives match object for every match
    matcher2 = re.finditer(pattern, mainstr)  # gives match object for every match
    for m in matcher:
        print(m.start(), m.end(), m.group())  # start index, end index+1, pattern for every match object
        count += 1
    print("Number of patterns found: ", count)
    m = re.match(pattern, mainstr)  # object is created m if match found in main string/
    # (check for ony first occurance(begining) of substring)
    if m != None:
        print("match found at ", m.start(), m.end())


#findstr("ab","abaababa")
'''
[abc] => Either a or b or c
[^abc] => Except a and b and c
[a-zA-Z0-9] => Any alphanumeric Character (Except alphanumeric : [^a-zA-Z0-9])

\s : space   \S : any character except space
\d : digit   \D : -------========----- digit
\w : word character [a-zA-Z0-9] \W : Except word character
.  : any character including special

a  : only one 'a'
a+ : at least one 'a'
a* : any no. of 'a' even zero 'a'
a? : at most one 'a', not more than one a
a{m} : exactly m no of 'a'
a{m,n}: minimum m and maximum n no.s of 'a'

"^abc" : we can use ^ to check whether our main string starts with provided pattern(abc) or not
"abc$" : we can use ^ to check whether our main string ends with provided pattern(abc) or not
'''
#findstr("[a-z]","1nath@PY00#7")


################## extract digits from string
def extDigit(mainstr):

    listDigits = re.findall("[0-9]", mainstr)
    listNums = re.findall("[0-9]+", mainstr)
    addition = 0
    for num in listNums:
        addition += int(num)

    print(listDigits,listNums, addition)


#extDigit('12eknath 23 jdhj 4 $% 30')


################# Check input pattern from user
'''
Take password from user and check whether it follows following condition
password length should be minimum 8 characters
atleast one digit
at least one capital characters
atleast one special characters 
'''
def getpassword():
    pattern="(\d+\w+)"


def countDays():
    monthdict = {1:['jan',31], 2:['feb',28], 3:['march',31], 4:['april',30], 5:['may',31], 6:['jun',30], 7:['july',31], 8:['aug',31], 9:['sept',30], 10:['oct',31], 11:['nov',30], 12:['dec',31]}
    date = input("Enter date")
    datelist = date.split('-')
    datelist=[int(i) for i in datelist]
    days = 0
    for m in range(1,datelist[1]):
        days += monthdict[m][1]
    days = days + datelist[0]
    if datelist[2] % 4 == 0 and (datelist[1]>2 or (datelist[0]==29 and datelist[1]==2 )):
        days += 1
    print(days)


def getTitles():
    import urllib.request
    infile = open('urls.txt')
    sites = infile.readlines()
    title = []
    for s in sites:
        u = urllib.request.urlopen(s)
        text = u.read()
        title.append(str(re.findall("<title>.*</title>",str(text)))[9:-10])
    print(title)




def getInfoSite():  #Error in opening file
    import urllib.request
    u = urllib.request.urlopen("https://www.redbus.in/info/contactus")
    text = u.read()
    city_list = re.findall('<div class="reachUs-header">.*</div>',str(text))
    print(city_list)


# lambda function
# lambda argument_list: Expression
def lambdademo():
    f1 = lambda x: (x*x)+1
    print(f1(3))
    f2 = lambda a, b: a + b
    print(f2(2, 3))
    list1 = [2, 4, 6]
    print(list(map(f1, list1)))  # map every element of list to function and return results
    f3 = lambda x: x % 2 == 0
    list2 = [5, 10, 15, 20, 25, 30]
    print(list(filter(f3, list2)))  # filter values of sequence as per condition given by lambda function
    # filter return only true value and filter out false value
    from functools import reduce
    print(reduce(f2, list1))


lambdademo()

'''
Challenging patterns
Alternating value check : r"(\w)(?=\w\1)"
        (\w) -- "single character":: (\w+) ==> more than one (\w{2})==> exact 2 
        (?=) -- this resembels to "is it matches to"
        (?=\w)-- "character after this character"
               to check value after 2 char we must use(?=\w{2}/1)
        (/1) -- it resembles exact value match, if not given match any char of \w 
'''
