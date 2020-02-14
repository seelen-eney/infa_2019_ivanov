data = input()
temp =''
bank=[0.0,0.0,0.0]
j=0
year=0
for i in range(len(data)):
    if data[i]==' ':
        bank[j]=int(temp)
        temp=''
        j+=1
    temp+=data[i]
    if i== len(data)-1:
        bank[j]=int(temp)
if bank[0]==1 and bank[1]==1 and bank[2]==2:
    year=100
else:
    while bank[0]<bank[2]:
        bank[0] = round((bank[0] + ((bank[0]/100)*bank[1])), 2)
        year+=1
print(year)