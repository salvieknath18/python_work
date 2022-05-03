#prime number using generator
def getPrime(num):
    prime = list(set(range(2,num+1)) - set([i*j for i in range(2,num+1) for j in range(2,i+1)]))
    for p in prime:
        yield p
    yield "done"

x = getPrime(int(input("Enter Number upto which prime is required")))
getPrime(x)
while True:
    val = next(x)
    if val == "done":
        break
    print(val,end=" ")



#return a e i o u
import  re
print(re.findall("[aeiouAEIOU]",input("Enter String")))



#sentence same words will reversed
#print(" ".join([word[-1::-1] for word in input("enter statement").split(" ")]))

#closure