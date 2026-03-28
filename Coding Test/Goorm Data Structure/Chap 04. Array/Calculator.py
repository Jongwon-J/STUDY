import operator

class Stack:
    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            return None

    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            return None

    def __len__(self):
        return len(self.items)

    def isEmpty(self):
        return len(self.items) == 0

def get_token_list(expr):
    tokens = []
    temp = ""
    ops = "+-*/^()"
    
    for char in expr:
        if char.isdigit() or char == ".": # 숫자거나 소수점일 경우
            temp += char
        elif char == " ": # 공백일 경우
            continue
        elif char in ops: # 연산자일 경우
            if temp:
                tokens.append(temp)
                temp = ""
            tokens.append(char)
        else:
            return "INVALID_EXPRESSION"
        
    if temp:
        tokens.append(temp)
        
    return tokens
    
def infix_to_postfix(infix):
    if infix == "INVALID_EXPRESSION":
        return "INVALID_EXPRESSION"
    
    opstack = Stack() # 연산자
    outstack = [] # 결과물
        
    # 연산자의 우선순위 설정
    prec = {'(': 0,
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
            '^': 3 }

    for token in infix:
        if token == '(':
            opstack.push(token)
        elif token == ')':
            while not opstack.isEmpty() and opstack.top() != '(':
                outstack.append(opstack.pop())
            if opstack.isEmpty(): # 짝이 맞는 '('가 없는 경우
                return "INVALID_EXPRESSION"
            opstack.pop() # '(' 제거
        elif token in '+-/*^':
            while not opstack.isEmpty() and prec[opstack.top()] >= prec[token]:
                outstack.append(opstack.pop())
            opstack.push(token)
        else: # operand일 때
            outstack.append(token)

    # opstack 에 남은 모든 연산자를 pop 후 outstack에 append
    while len(opstack) != 0:
        op = opstack.pop()
        if op == '(': # 여는 괄호가 남아있다면 괄호의 짝이 안 맞는 것
            return "INVALID_EXPRESSION"
        outstack.append(op)

    return " ".join(outstack)

def compute_postfix(postfix):
    if postfix == "INVALID_EXPRESSION":
        return "INVALID_EXPRESSION"
    
    res_stack = Stack()
    # 연산자 매핑 딕셔너리 생성 (operator 사용)
    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '^': operator.pow
    }
    
    for token in postfix.split():
        if token in ops:
            if len(res_stack) < 2:
                return "INVALID_EXPRESSION"
            num1 = res_stack.pop()
            num2 = res_stack.pop()
            
            if token == '/' and num1 == 0:
                return "ZERO_DIVISION_ERROR"
            
            res_stack.push(ops[token](num2, num1))
            
        else:
            try:
                res_stack.push(float(token))
            except ValueError: # 숫자가 아닌 피연산자 처리
                return "INVALID_EXPRESSION"
    
    if len(res_stack) != 1:
        return "INVALID_EXPRESSION"
    
    result = res_stack.pop()
    return f"{result:.3f}" # 소수점 4자리까지 반올림

exam = input()
infix_expr = get_token_list(exam)
postfix_expr = infix_to_postfix(infix_expr)
res_num = compute_postfix(postfix_expr)
print(res_num)