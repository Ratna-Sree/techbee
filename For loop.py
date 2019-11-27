#1) l1=['there is error', 'good line', 'error line', 'network error', 'database error', 'success']
#count non error lines and print it.
l1=['there is error', 'good line', 'error line', 'network error', 'database error', 'success']
a=0
b=0
for i in l1:
    if 'error' in i:
        b += 1
        continue
    a = a+1
    print(i," is non error")
print("no of non error items are : ",a)
print("no of error items are : ",b)
