import include.analyzer
import libs.builtin

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

        ops = [a for a in include.analyzer.ops_dict.keys()]

        for command, func in self.commands.items():
            if command in ops:
                self.linker[f'{libs.builtin.dictIndex(key_val={command:func}, target=self.commands) - 1}:{libs.builtin.dictIndex(key_val={command:func}, target=self.commands) + 1}'] = [command, func]

        return {'commands': self.commands, 'linker': self.linker}