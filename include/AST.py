import include.analyzer

class AST:
    def __init__(self):
        self.commands = {}
        self.linker = {}

    def build(self, lex_tree: dict) -> None:
        for command in lex_tree.values():
            if command[1] not in include.analyzer.type_keys_dict.keys():
                self.commands[command[0]] = include.analyzer.tokens_id[command[1]][command[0]] if command[1] != 'var_name' else 'var_name'
            else:
                self.commands[command[0]] = include.analyzer.type_keys_dict[command[1]]
        print(self.commands)