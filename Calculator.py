"""
1) Write calculator program.
Take 3 inputs from user.
1st input -> number
2nd input -> number
3rd input -> string (add, sub, div,multi) -> None of these print"Opertion not supported")
"""
print (""" Ratna's personalized calculator:
       List of the operations available:
       a) ADD
       b) SUBTRACT
       c) DIVIDE
       D) MULTIPLY""")
opr=input("Please enter any one of the desired operation among a,b,c & d :")
n1=int(input("Enter the first number:" ))
n2=int(input("Enter the second number:" ))
if opr== 'a':
    print(" Addition of the two numbers is ",n1+n2)
elif opr== 'b':
    print("Subtraction of the two numbers is ", n1-n2)
elif opr== 'c':
    print("Division of the two numbers is ", n1/n2)
elif opr== 'd':
    print("Multiplication of the two numbers is ",n1*n2)
else:
    print("Operation not supported")
print("Bye Bye")

    
