import include.analyzer

def token_type(token: str):
    """Check INT"""
    try:
        float(token)
        return 'float'
    except:
        pass

    """Check FLOAT"""
    try:
        int(token)
        return 'int'
    except:
        pass

    """Check OTHER"""
    return 'op' if token in include.analyzer.ops_list else 'syntax'



def lexer(line: str) -> dict:
    tokens = []
    tree = {}
    lex = ''
    for c in line:
        if c != ' ':
            lex += c
        else:
            if lex != '':
                tokens.append(lex)
                lex = ''
                
    tokens.append(lex)

    for index, token in enumerate(tokens):
        t_id = token_type(token)
        if token.isdigit():
            t_id = 'int'
        elif token.isnumeric():
            t_id = 'float'

        tree[index] = {token:t_id}

    return "\n".join(f"{k}:{v}" for k,v in tree.items())