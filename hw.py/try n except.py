while True:
    try:
        a=int(input("number"))
        b=int(input("second number"))
        
        
        
        if b==5:
            raise Exception("5 is not accepted")
        
        print(a/b)
        
    except ZeroDivisionError:
        print("0 mildaina")
        
    except Exception as e:
        print("something went wrong",e)