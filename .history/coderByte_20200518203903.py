

def QuestionsMarks(str):
    numbers = []
    # others = []
    for char in str:
        if char.isdigit():
            numbers.append(int(char))
        elif char == '?':
            numbers.append(char) 
        else:
            break    
        
    
             
     
        # break    


    print(numbers) 
    return str
# keep this function call here 
QuestionsMarks("acc?7??sss?3rr1??????5")