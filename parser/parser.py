
def parse(tokenList):
    AST = []
    totalLine = tokenList[-1]['line']
    lineDict = prepare_line_dict(totalLine, tokenList)
    for key in lineDict.keys():
        expression = {'poStart': []}
        if lineDict[key][0]['type'] == 'id':
            expression['type'] = 'Assignment Statement'
            expression['variableName'] = lineDict[key][0]['value']
            expression['poStart'].append(lineDict[key][0]['pos'])
            assignment_statement(lineDict[key][1:], expression)
            
        if lineDict[key][0]['type'] == 'if':
            expression['type'] = 'Conditional Statement'
            expression['poStart'].append(lineDict[key][0]['pos'])
            conditional_statement(lineDict[key][1:], expression)
            
        if lineDict[key][0]['type'] == 'Space':
            i = 0 
            while lineDict[key][i]['type'] == 'Space':
                i += 1
            expression['poStart'].append(i)
            expression['type'] = 'In Conditional Statement'
            if lineDict[key][i]['type'] == 'id':
                expression['variableName'] = lineDict[key][4]['value']
                assignment_statement(lineDict[key][i:], expression)   
            if lineDict[key][i]['type'] == 'print': 
                expression['typeAssignment'] = 'print'   
                print_statement(lineDict[key][i:], expression)
                
        AST.append(expression)
    return AST
                
    
def prepare_line_dict(totalLine, tokenList):
    lineDict = {}
    for line in range(1, totalLine + 1):
        statementInLine = []
        for token in tokenList:
            if token['line'] == line:
                statementInLine.append(token)
        lineDict[line] = statementInLine
    return lineDict

def assignment_statement(value, expression):
    for val in value:
        if val['type'] == '=':
            expression['typeAssignment'] = {'type': val['type'], 'pos': val['pos']}
        elif val['type'] == 'Number':
            expression['variableValue'] = val['value']
        elif val['type'] == 'Newline':
            expression['ExpFinished'] = True
        
def conditional_statement(value, expression):
    for val in value:
        if val['value'] in ['<', '>', '<=', '>=', '==', '!=']:
            expression['typeAssignment'] = val['type']
        elif val['type'] == 'Number':
            expression['conditionalValue'] = val['value']
        elif val['type'] == 'id':
            expression['variableName'] = val['value']
        elif val['type'] == 'Statement':
            expression['ExpFinished'] = True

def print_statement(value, expression):
    for val in value:
        if val['type'] == '(':
            expression['OpenParenthese'] = True 
        elif val['type'] == ')':
            expression['CloseParenthese'] = True 
        elif val['type'] == 'id':
            expression['ValueToPrint'] = val['value']
    
        
    
        
                

