print("choose the operator '+','*','/''-'")
sign=input("select the operator")
a=int(input("1st_num"))
b=int (input("2nd num"))
if (sign=="+"):
    print("Additon",(a+b))
elif(sign=="*"):
    print("multiplication",(a*b))
elif(sign=="/"):
    if b==0:
        print("error")
    print("divide"(a/b))
elif(sign=="-"):
    print("substraction",(a-b))
else:
    print("error")