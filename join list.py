"""3) 
l1=['A','B','C','D','E','F','G','H','I']
Output should be like below:
    ABC
    DEF
    GHI
"""
l1=['A','B','C','D','E','F','G','H','I']
lst=[]
count=0
for i in range(len(l1)):
    lst.append(l1[i])
    count+=1
    if count %3==0:
        print(''.join(lst))
        lst=[]
