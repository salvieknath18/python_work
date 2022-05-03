

LoL=[[1,2,3],['eknath','abhi','amit'],[28,26,24]]

LoD=[{'number':1,'name':'eknath','age':28},
     {'number':2,'name':'abhi','age':26},
     {'number':3,'name':'amit','age':24}]

DoL={'number':[1,2,3],'name':['eknath','abhi','amit'],'age':[28,26,24]}

DoD={1:{'name':'eknath','age':28},
     2:{'name':'abhi','age':26},
     3:{'name':'amit','age':24}}

ToT=((1,2,3),('eknath','abhi','amit'),(28,26,24))

ToL=([1,2,3],['eknath','abhi','amit'],[28,26,24])

ToD=({'number':1,'name':'eknath','age':28},
     {'number':2,'name':'abhi','age':26},
     {'number':3,'name':'amit','age':24})


print "List of List := " ,LoL
print "List of Dict := " ,LoD
print "Dict of List := " , DoL
print "Dict of Dict := " + str(DoD)
print "Tuple of Tuple := " + str(ToT)
print "Tuple of list := " + str(ToL)
print "Tuple of Dict := " + str(ToD)

print "abhi value in LoL LoL[1][1] : " , LoL[1][1]
print "abhi value in LoD str(LoD[1]['name'] : ",LoD[1]['name']
print "abhi value in DoL DoL['name'][1] : " + str(DoL['name'][1])
print "abhi value in DoD DoD[2]['name'] : " + str(DoD[2]['name'])
print "abhi value in ToT ToT[1][1] : " + str(ToT[1][1])
print "abhi value in ToL ToL[1][1] : " + str(ToL[1][1])
print "abhi value in ToD ToD[1]['name'] : " + str(ToD[1]['name'])

