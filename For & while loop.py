"""
3) l1=['san', 'tan', 'jai']
print the output as
A)print in 3 sets
san
tan
jai
san
tan
jai
san
tan
jai
B) print in repetation 3 times
san
san
san
tan
tan
tan
jai
jai
jai """
j=1
l1=['san', 'tan', 'jai']
print(len(l1))
print("first loop in sequence list")
while j <= len(l1):
    
    for i in l1:
        print(i)
    j=j+1
#
print("first loop in sequence list")

for i in l1:
    j=1
    while j <= len(l1):
        print(i)
        j=j+1
