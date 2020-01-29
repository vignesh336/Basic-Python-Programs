vowel=0
con=0
dot=0
space=0
list1=['a pple','ora,nge','so,ap']
print(list1)
for i in list1:
    for j in i:
        if j=='a' or j=='e' or j=='i' or j=='o' or j=='u':
            vowel=vowel+1
        elif(j==' '):
            space=space+1
        elif(j=='.'):
            dot+=1
        else:
            con=con+1
print ("vowel=",vowel)
print("consonent=",con)
print ("space=",space)
print("dot=",dot)
