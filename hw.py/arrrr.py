while True:
    try:
        array=[0,1,3,2,4]
        a=int(input("any number"))
       
        if a<len(array):
            raise Exception ("not found")
        
        print(array[a])
            
    except Exception as e:
        print("error",e)