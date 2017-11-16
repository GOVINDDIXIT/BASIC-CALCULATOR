print("*****************")
print("   CALCULATOR   ")
print("***********1******")
choose='Y'
while choose.upper()=='Y':
    print("1.ADDITION")
    print("2.SUBTRACTION")
    print("3.MULTIPLICATION")
    print("4.DIVISION")
    print("5.POWER")
    print("\n")
    print("ENTER YOUR CHOICE:-")
    n=int(input())
    print('\n')
    if(n<1 or n>5):
        print("WRONG CHOICE ENTERED!!!")
        print("DO YOU WANT TO TRY AGAIN?")
        print("ENTER (Y) FOR YES  OR (N) FOR NO ")
        choose=input()
        continue
    print("ENTER FIRST NUMBER:")
    a=float(input())
    print("ENTER SECOND NUMBER")
    b=float(input())
    if n==1:
        print(a+b)
        print("YOU WANT TO DO ANOTHER CALCULATION")
        print("ENTER (Y) FOR YES  OR (N) FOR NO ")
        choose = input()
    elif n==2:
        print(a-b)
        print("YOU WANT TO DO ANOTHER CALCULATION")
        print("ENTER (Y) FOR YES  OR (N) FOR NO ")
        choose = input()
    elif n==3:
        print(a*b)
        print("YOU WANT TO DO ANOTHER CALCULATION")
        print("ENTER (Y) FOR YES  OR (N) FOR NO ")
        choose = input()
    elif n==4:
        print(a/b)
        print("YOU WANT TO DO ANOTHER CALCULATION")
        print("ENTER (Y) FOR YES  OR (N) FOR NO ")
        choose = input()
    elif(n==5):
        print(a**b)
        print("YOU WANT TO DO ANOTHER CALCULATION")
        print("ENTER (Y) FOR YES  OR (N) FOR NO ")
        choose = input()
