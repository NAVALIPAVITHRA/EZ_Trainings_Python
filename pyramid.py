input1=int(input())
res=input1*1
num=2
for i in range(input1-1,0,-1):
    res+=res*num+1
print(res)

