#code
from collections import OrderedDict as DIC
for i in range(int(input())):
    n=int(input())
    ls=list(map(int,input().split()))
    dic=DIC()
    for i in ls:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
    #print(dic)
    res=sorted(dic.items(),key=lambda x:(-x[1],x[0]))
    temp=''
    for i in res:
        temp+=(str(i[0])+' ')*i[1]
    temp.lstrip()
    temp.rstrip()
    print(temp)
