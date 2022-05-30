from tokenize import Token
from tokenizer import lexer
import os 

with open(os.path.join('test.txt')) as file: 
    code = file.read()

print(code)
lex = lexer.Lexer(code)
print(lex.text)
token = lex.next()

while token.kind() != 'EOF':
    print(token.value)
    print(f'Type: {token.type} + Line: {token.line} + Pos: {token.position} + Val: {token.value}')
    token = lex.next()
