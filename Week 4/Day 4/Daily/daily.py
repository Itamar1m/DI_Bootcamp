
def matrix(code):
    for i in range(len(code)):
        if code[i]==code[0] and code[i][0].isalpha()==False:
            pass
        elif  code[i][0].isalpha()==True:
            print(code[i][0])
        elif  code[i-1][0].isalpha() ==True and code[i+1][0].isalpha() ==False:                                                       
            print(' ')
            
    for i in range(len(code)):
        # if code[i]==code[0] and(code[i][1].isalpha()==False and code[i-1][1].isalpha()==False):
        #     print(" ")
        if    code[i][1].isalpha()==True:
            print(code[i][1])
        elif code[i-1][1].isalpha() ==True and code[i+1][1].isalpha() ==False:    
            print(' ')
            
    for i in range(len(code)):
        # if code[i]==code[0] and (code[i][2].isalpha()==False and code[i-1][1].isalpha()==False):
        #     print(" ")
        if code[i][2].isalpha()==True:
            print(code[i][2])    
        elif  code[i-1][2].isalpha() ==True and code[i+1][2].isalpha() ==False:    
            print(' ')
            
matrix( [
    ["7","i","3"],
    ["T", "s", "i"],
    ["h", " " ,"x"],
    ["i"," ","#"],
    ["s", "M", " "],
    ["$", "a", " "],
    ["#", "t", "%"],
    [" ", "r", "!"]
])