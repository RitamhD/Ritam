# ADVANCED CALCULATOR Made By Ritam :-

s = []
b = 0
c = 1
print("Basic Instructions:-\n1) After input completion enter '=' to get the output"
"\n2) To terminate the calculator enter 'c'\n3) Else to run the calculator again enter 'a'"
"\n4) An empty input will provide an error")
while True: 
    operant = str(input('\33[1m'"Enter operant(+,-,*,/,%): "'\33[m'))

    if operant == "+":
        print("\nEnter the numbers to be added:-")
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
        q = input("Again or Exit: ")
        if q == "c":
            break

    elif operant == "-":
        print("\33[1m Maximum two numbers can be taken\33[m" "\n Enter the numbers to be subtracted: ")
        n1 = int(input())
        n2 = int(input())
        print("The result is: ", n1-n2)
        q = input("Again or Exit: ")
        if q == "c":
            break

    elif operant == "/":
        print("\33[1m Maximum two numbers can be taken\33[m" "\nEnter the numbers to be divided: ")
        n1 = int(input())
        n2 = int(input())
        print("The result is: ",n1/n2)
        q = input("Again or Exit: ")
        if q == "c":
            break

    elif operant == "%":
        print("\33[1m Maximum two numbers can be taken\33[m" "\nEnter the numbers to be divided: ")
        n1 = int(input())
        n2 = int(input())
        print("The result is: ",n1%n2)
        q = input("Again or Exit: ")
        if q == "c":
            break

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
        q = input("Again or Exit: ")
        if q == "c":
            break
    elif operant == "c":
        break
    else:
        print("The input is invalid, please enter a correct operant")