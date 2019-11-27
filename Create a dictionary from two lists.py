#assignment 28/9/19
"""
1)l1=['A','B','C','D','E','F','G']
l2=[40,80,[2,6,4],16]
    OUTPUT SHOULD BE LIKE BELOW
d1={'A':40,
    'B':80,
    'C':[2,6,4],
    'D':16,
    'E':'NOVALUE',
    'F':'NOVALUE',
    'G':'NOVALUE'}
"""
l1=['A','B','C','D','E','F','G']
l2=[40,80,[2,6,4],16]
d1={}
for x in range(len(l1)):
    a=l1[x]
    if x< len(l2):
        b=l2[x]
        d1[a]=b
for y in l1:
    d1.setdefault(y,"novalue")  
print(d1)
