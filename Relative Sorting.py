
for i in range(int(input())):
    n,m=list(map(int,input().split()))
    ar=list(map(int,input().split()))
    br=list(map(int,input().split()))
    dir={}
    for i in ar:
        if i not in dir:
            dir[i]=1
        else:
            dir[i]+=1
    st=''
    for i in br:
        if i in dir:
            st+=(str(i)+' ')*dir[i]    
            del(dir[i])
    for key in sorted(dir.keys()):
        if dir[key]>0:
            st+=(str(key)+' ')*dir[key]
    #res=' '.join(st)
    st.lstrip()
    st.rstrip()
    print(st)
    
    
