def remove(str):
    #  loop from the middle 
    # add both to a stack 
    # whichever stack is not empty return its length 
    stackA = []
    stackB = []
    n = len(str)
    x = n//2
    for i in range(0,n//2):
        print('i',i)
        
        stackA.append(str[i])
    for i in range(n-1,2,-1):
        print(i)    
    


remove("(()(")                