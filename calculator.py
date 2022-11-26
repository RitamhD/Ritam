# ADVANCED CALCULATOR Made By Ritam :-

operant = str(input('\33[1m'"Enter operant(+,-,*,/,%): "'\33[m'))
s = []
b = 0
c = 1

if operant == "+":
    print("Enter = to get the output\nEnter the numbers to be added:-")
    while True:
        a = input()

        if a == "=":
            for i in s:
                b += int(i)
            print("Numbers entered: ",s,"\nThe result is: ",b)
            break
        else:
            print("+")
            s.append(a)
elif operant == "-":
    print("\33[1m Maximum two numbers can be taken\33[m" "\n Enter the numbers to be subtracted: ")
    n1 = int(input())
    n2 = int(input())
    print("The result is: ", n1-n2)

elif operant == "/":
    print("\33[1m Maximum two numbers can be taken\33[m" "\nEnter the numbers to be divided: ")
    n1 = int(input())
    n2 = int(input())
    print("The result of",n1,"/",n2,"is",n1/n2)

elif operant == "*":
    print("Enter numbers to be multiplied: ")
    while True:
        a = input()

        if a == "=":
            for i in s:
                c *= int(i)
            print("Numbers entered :",s,"\nThe result is: ",c)
            break
        else:
            s.append(a)
else:
    print("The input is invalid, please enter the correct operant next time")
