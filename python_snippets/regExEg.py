import re

string = open(r"C:\Users\Eknath\Desktop\sample.txt").read()

#print(string)

pattern = re.compile("[^ ]+@\w+\.\w+")
#print(pattern.findall(string))

#print(re.findall("\d{10}", string))

match_list = re.finditer("\d{10}", string)
result_str = ""
rstart = 0
for m in match_list:
    rend = m.start()
    result_str = result_str + string[rstart:m.start()] + "******" + m.group()[6:]
    rstart = m.end()
# print(result_str)

string2 = """raj is good student, he weakup in the morning
he knows java,
Java is programming Language
he also know javascript, he lives in mumbai"""

string_to_write = re.split("[,\n][ \n]*",re.sub("[jJ]ava\W+", "Pyathon", string2))
print(string_to_write)
                           
