
a=float(input())

b=float(input())

sum=a+b

subtraction=a-b

multiplication=a*b

division=a/b

ope={"+":sum,"-":subtraction,"*":multiplication,"/":division }


operation=input()


print(ope[operation])

