def find_sum(array,n):
    #input a sorted array of integers and an integer n,return a list containing all pairs whose sum is n
    result=[]
    data={}#从小到大记录每个数的个数
    for arr in array:
        data[arr]=1+data.get(arr,0)

    if n%2==0 and data.get(n//2,0)>1:
        times=data.get(n//2)
        add_last=[(n//2,n//2)]*int(times*(times-1)/2)
        del data[n//2]
    else:
        add_last=[]
    i=0
    j=len(data)-1
    keys=list(data.keys())
    while i<j:
        tmp1=keys[i]
        tmp2=keys[j]
        if tmp1+tmp2<n:
            i=i+1#就往后推
        elif tmp1+tmp2>n:
            j=j-1
        else:#add to result
            result.extend([(tmp1,tmp2)]*data[keys[i]]*data[keys[j]])
            i=i+1
    return result+add_last
                    