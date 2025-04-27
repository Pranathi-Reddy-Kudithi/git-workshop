import re 
 
# ----- PHASE 1: Lexical Analysis ----- 
def lexer(input_code): 
    tokens = [] 
 
    token_specification = [ 
        ('NUMBER', r'\d+'), 
        ('ID', r'[a-zA-Z_]\w*'),  # allow full variable names 
        ('ASSIGN', r'='), 
        ('OP', r'[+\-*/]'), 
        ('SKIP', r'[ \t]+'), 
        ('MISMATCH', r'.'), 
    ] 
 
    tok_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specification) 
    print(tok_regex) 
 
    for mo in re.finditer(tok_regex, input_code): 
        kind = mo.lastgroup 
        value = mo.group() 
        if kind == 'NUMBER': 
            tokens.append(('NUMBER', int(value))) 
        elif kind == 'ID': 
            tokens.append(('ID', value)) 
        elif kind == 'ASSIGN' or kind == 'OP': 
            tokens.append((kind, value)) 
        elif kind == 'SKIP': 
            continue 
        else: 
            raise SyntaxError(f'Unexpected token: {value}')
    return tokens 
 
# ----- PHASE 2: Syntax Analysis + PHASE 3: Semantic Analysis ----- 
def parser(tokens): 
    if len(tokens) < 3 or tokens[1][0] != 'ASSIGN': 
        raise SyntaxError("Expected '=' after identifier") 
 
    lhs = tokens[0][1]  # variable name 
    rhs = tokens[2:]   # expression 
    return lhs, parse_expression(rhs) 
 
def parse_expression(tokens): 
    output = [] 
    ops = [] 
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2} 
 
    for token in tokens: 
        if token[0] in ('NUMBER', 'ID'): 
            output.append(token) 
        elif token[0] == 'OP': 
            while ops and precedence[ops[-1][1]] >= precedence[token[1]]: 
                output.append(ops.pop()) 
            ops.append(token) 
 
    while ops: 
        output.append(ops.pop()) 
 
    return output  # Postfix expression 
 
# ----- PHASE 4: Intermediate Code Generation ----- 
def generate_intermediate(lhs, postfix_expr): 
    code = [] 
    temp_count = 0 
    stack = [] 
 
    for token in postfix_expr: 
        if token[0] in ('NUMBER', 'ID'): 
            stack.append(token[1]) 
        elif token[0] == 'OP': 
            b = stack.pop() 
            a = stack.pop() 
            temp = f"t{temp_count}" 
            temp_count += 1 
            code.append(f"{temp} = {a} {token[1]} {b}")
            stack.append(temp) 
 
    code.append(f"{lhs} = {stack.pop()}") 
    return code 
 
# ----- PHASE 5: Assembly Code Generation ----- 
def generate_assembly(lhs, postfix_expr): 
    assembly = [] 
    for token in postfix_expr: 
        if token[0] == 'NUMBER': 
            assembly.append(f"PUSH {token[1]}") 
        elif token[0] == 'ID': 
            assembly.append(f"LOAD {token[1]}") 
        elif token[0] == 'OP': 
            if token[1] == '+': 
                assembly.append("ADD") 
            elif token[1] == '-': 
                assembly.append("SUB") 
            elif token[1] == '*': 
                assembly.append("MUL") 
            elif token[1] == '/': 
                assembly.append("DIV") 
            assembly.append(f"STORE {lhs}") 
    return assembly 
 
# ----- DRIVER ----- 
def mini_compiler(input_code): 
    print("Input:", input_code) 
     
    tokens = lexer(input_code) 
    print("Tokens:", tokens) 
     
    lhs, postfix_expr = parser(tokens) 
    print("Postfix Expression:", postfix_expr) 
    
    print("\nIntermediate Code:") 
    intermediate = generate_intermediate(lhs, postfix_expr) 
    for line in intermediate: 
        print(line) 
     
    print("\nAssembly Code:") 
    assembly = generate_assembly(lhs, postfix_expr) 
    for line in assembly: 
        print(line)
mini_compiler("c=a+2*4") 