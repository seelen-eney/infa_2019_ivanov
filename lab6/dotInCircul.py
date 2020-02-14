koord = input()
data = [0,0,0]
temp =''
j=0
for i in range(len(koord)):
    if koord[i]==' ':
        data[j]=int(temp)
        temp=''
        j+=1
    temp+=koord[i]
    if i == len(koord)-1:
        data[j]=int(temp)
if data[0]**2+data[1]**2<=data[2]**2:
    print("YES")
else:
    print("NO")
