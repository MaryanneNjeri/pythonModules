def goatLatin(S):
    vowels = {'a','e','i','o','u'}
    if len(S) == 0:
        return " "
    S = S.split(" ")
    count = 1
    for i in range(len(S)):
        begin = 'a'
        newWord = ""
        if S[i][0] in vowels:
            begin = begin * count
            newWord += S[i] + "ma" + begin 
        else:
            begin = begin * count
            newWord = S[i][1:] + S[i][0]+ "ma" + begin
        S[i] = newWord 
        count +=1 
    print(" ".join(S)) 
goatLatin("The quick brown fox jumped over the lazy dog")       