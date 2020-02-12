#Your task is to complete this function
#Your should return the required output
def maxLen(n, arr):
    #Code here
    dic={}
    max_len=0
    s=0
    for i in range(len(arr)):
        s+=arr[i]
        if(arr[i]==0 and max_len==0):
            max_len=1
        if(s==0):
            max_len=i+1
        if(s in dic):
            max_len=max(max_len,i-dic[s])
        else:
            dic[s]=i
    return max_len

