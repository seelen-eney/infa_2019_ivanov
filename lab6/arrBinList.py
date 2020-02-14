arrLan = int(input())
binAr = [] #[0] * arrLan
N=0

numOfOnes1 =0
numOfOnes2 =0
while N < arrLan:
    temp=input()
    if temp=='' or temp==' ':
        print("Try again, you should input digits")
        continue
    if int(temp) ==0 or int(temp) ==1:
        N += 1
        binAr.append(int(temp))
    else:
        print("Try again, you shoul input 0 or 1")
for i in range(len(binAr)):

    if binAr[i]==1:
        numOfOnes1+=1
    if numOfOnes1>numOfOnes2:
        numOfOnes2=numOfOnes1
    if binAr[i]==0:
        numOfOnes1=0
print(binAr)
print(numOfOnes2)