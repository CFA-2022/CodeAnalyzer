
def indentation_score(AST):
    score = 0
    for exp in AST: 
        if (exp['type'] != 'In Conditional Statement' and exp['poStart'][0] == 0):
        #(exp['type'] == 'In Conditional Statement' and exp['poStart'][0] == 4):
            score += 1 
        if (exp['type'] == 'In Conditional Statement' and exp['poStart'][0] == 4):
            score += 1
  
    if score == len(AST):
        return 1
    else:
        return 0 

def print_statement_score(AST):
    score = 0 
    printStateList = []
    for exp in AST:
        print(exp)
        if exp['typeAssignment'] == 'print':
            printStateList.append(exp)
    
    for printState in printStateList:
        if printState['OpenParenthese'] and printState['CloseParenthese']:
            score += 1 
    
    if score == len(printStateList):
        return 1
    else:
        return 0

            