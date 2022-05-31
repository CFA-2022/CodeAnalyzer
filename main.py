from tokenize import Token
from tokenizer import lexer
from parser import parser
import scoring
import os 
import json

with open(os.path.join('test.txt')) as file: 
    code = file.read()

lex = lexer.Lexer(code)
token = lex.next()
tokenList = []

while token.type != 'EOF':
    #print(f'Type: {token.type} + Line: {token.line} + Pos: {token.position} + Val: {token.value}')
    tokenDict = {'type': token.type, 'value': token.value, 'line': token.line, 'pos': token.position}
    tokenList.append(tokenDict)
    token = lex.next()

jsonToken = json.dumps(tokenList, indent=4)
print(jsonToken)
print('-------AST---------')
AST = parser.parse(tokenList)
jsonAST = json.dumps(AST, indent=4)
print(jsonAST)

print('--------Scoring------')
indentation_score = scoring.indentation_score(AST)
print_statement_score = scoring.print_statement_score(AST)

print(f'Score total: {indentation_score + print_statement_score}')
print(f'Indentation score: {indentation_score}')
print(f'Print statement score: {print_statement_score}')