import include.analyzer
import include.AST

def token_type(token: str):
    """Check INT"""
    if '.' in token:
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
    return 'op' if token in include.analyzer.ops_dict.keys() else 'block' \
                                    if token in include.analyzer.block_keys_list else 'macros'\
                                    if token in include.analyzer.macros_keys_dict.keys() else 'var_name'



def lexerToAST(line: str) -> dict:
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
        tree[index] = [token,t_id]

    print(tree)

    #return tree#"\n".join(f"{k}:{v}" for k,v in tree.items())

    ast = include.AST.AST()

    return ast.build(tree)