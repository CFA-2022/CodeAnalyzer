class Token(object):
    def __init__(self, type, line, position, value):
        self.type = type
        self.line = line
        self.position = position
        self.value = value
    
    def type(self):
        return self.type
    
    def position(self):
        return f'(Line: {self.line}, Pos: {self.position})'
    
    def value(self):
        return self.value

class Lexer:
    KEYWORDS = frozenset(['and', 'or', 'not', 'else', 'if', 'elif', 'print'])
    
    def __init__(self, code):
        self.text = code
        self.index = -1 
        self.line = 1 
        self.pos = 0
        self.token = None
        
    def next_char(self):
        self.index = self.index + 1
        self.pos = self.pos + 1 
        if self.index == len(self.text):
            return 'EOF'
        return self.text[self.index]
    
    def next(self):
        currentChar = self.next_char()
        match(currentChar):
            case currentChar if currentChar.isalpha() and currentChar != "EOF":
                words = ''
                while currentChar.isalpha() or currentChar == '_' or currentChar.isdigit():
                    words = words + currentChar
                    currentChar = self.next_char()
                    if currentChar == 'EOF':
                        break 
                self.index -= 1
                self.pos -= 1
                if words not in Lexer.KEYWORDS:
                    self.token = Token('id', self.line, self.pos - len(words), words)
                else: 
                    self.token = Token(words, self.line, self.pos - len(words), words)
            
            case currentChar if currentChar.isdigit():
                num = 0 
                digits = 0 
                while currentChar.isdigit():
                    num = 10 * num + int(currentChar, 10)
                    currentChar = self.next_char()
                    digits += 1
                self.index = self.index - 1
                self.pos = self.pos - 1
                self.token = Token('Number', self.line, self.pos - digits, num)
            
            case '/': 
                self.token = Token('/',  self.line, self.pos - 1, '/')
            
            case '*': 
                self.token = Token('*', self.line, self.pos - 1, '*')
            
            case '+':
                self.token = Token('+', self.line, self.pos - 1, '+')
                
            case '-':
                self.token = Token('-', self.line, self.pos - 1, '-')
            
            case '(':
                self.token = Token('(', self.line, self.pos - 1, '(')
            
            case ')':
                self.token = Token(')', self.line, self.pos - 1, ')')
        
            case ',':
                self.token = Token('Comma', self.line, self.pos - 1, ',')
            
            case '=':
                currentChar = self.next_char()
                str_len = 1
                if currentChar == '=':
                    while currentChar != ' ': 
                        str_len += 1  
                        currentChar = self.next_char()
                
                    if str_len > 2:
                        print('IllegalCharacterError')
                    else: 
                        self.token = Token('==', self.line, self.pos - 2, "==")
                
                else: 
                    self.index -= 1
                    self.pos -= 1
                    self.token = Token('=', self.line, self.pos - 1, '=')
            
            case '>': 
                currentChar = self.next_char()
                if currentChar == '=':
                    self.token = Token('>=', self.line, self.pos - 1, '>=')
                else: 
                    self.index -= 1
                    self.pos -= 1
                    self.token = Token('>', self.line, self.pos - 1, '>')
            
            case '<': 
                currentChar = self.next_char()
                if currentChar == '=':
                    self.token = Token('<= ', self.line, self.pos - 1, '<=')
                else: 
                    self.index -= 1
                    self.pos -= 1
                    self.token = Token('<', self.line, self.pos - 1, '<')
            
            case '\n':
                #self.pos = 0
                self.token = Token('Newline', self.line, self.pos, '\n')
                self.line += 1
                self.pos = 0
                #return self.next()
            
            case ':':
                currentChar = self.next_char()
                if currentChar == '\n':
                    self.token = Token('Statement', self.line, self.pos - 1, ':')
                    self.line += 1
                                            
            case 'EOF':
                self.token = Token('EOF', self.line, self.pos, 'EOF')
                
            case currentChar if currentChar.isspace():
                self.token = Token('Space', self.line, self.pos, 'Space')
                self.pos += 1
            
            case '!':
                currentChar = self.next_char()
                if currentChar == '=':
                    self.token = Token('Operator', self.line, self.pos - 1, '!=')
                else: 
                    print('Error: unexpected character')
            
        return self.token
                    
            

            
                