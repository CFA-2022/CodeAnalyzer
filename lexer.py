import re

class Token:
    def __init__(self, value, name):
        self.value = value
        self.name = name

tokens = [
        ('^(#.*\n)\Z', "comments"),
        ('^("""[\w\W]*?""")\Z', "comments"),
        ("^[\s\t\n]\Z", "spaces"),
        ("^[\(\)\[\]\{\}]\Z", "bracket"),
        ("^(\+|\-|\*|/|=)\Z", "operator"),
        ("^(\d)+(.(\d)+)?\Z", "number"),
        ("^[a-zA-Z][a-zA-Z0-9]*\Z", "id"),
]
        
def lexer(code):
    tokenList = []
    startPos = 0
    matched = False
    
    i = 0
    n = len(code)
    while i < n:
        print(n)
        current = code[startPos: i + 1]
        print(current)
        flag = matched
        
        for j in range(len(tokens)):
            print(f"{tokens[j]}")
            if(None != re.match(tokens[j][0], current)):
                print(f"Finded + {code[startPos: i]}")
                matched = j 
                flag = True 
                break 
        
        if(flag != False):
            print("Go Here")
            expName = tokens[matched][1] 
            tokenList.append(Token(code[startPos: i], expName))
            begin = i
            i -= 1 
            matched = False 
        print("Finished")
        i += 1 
        

    print("Breaks")
    for i in tokenList: 
        print(f"{i.name} + {i.value}")
        
    return tokenList

code = open("test.txt", "r").read()
print(code)
print("Startted lexer")
tokenList = lexer(code)
print(tokenList)
print("Finished lexer")
