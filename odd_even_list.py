even=[]
odd=[]
list1=[0,1,2,3,4,5,6,7,8,9,10]
print ("org=",list1)
#rev
list1.sort(reverse=True)
print("rev=",list1)
#odd no
print("odd nos")
for i in list1:
    if i%2!=0:
        print(i)
#real no
print("real  nos")        
for i in list1:
    if i!=0:
       print(i)
#odd index value
for i in list1:
    if i % 2: 
        even.append(list1[i]) 
    else : 
        odd.append(list1[i]) 
print(odd)

