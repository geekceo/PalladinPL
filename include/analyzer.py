import include.parser
import include.analyzer


"""Tokens"""

ops_list = ['+', '-', '*', '/']

syntax_keys_list = ['var', 'func', 'input', 'output', 'for', 'while']

start_block = ':'

newline_block = ['   ', ' '*4]

end_block = ''

bracket_start = '('

bracket_end = ')'

str_start = '"'
str_end = '"'

brack_err = "Brackets Error, check brackets count in line: "

def brackets_error(line_num: int, line: str) -> None:
    print(f'###$$$ {line}')
    print(f'{include.analyzer.brack_err} {line_num}')

def getStr(line: str):
    start = line.find('"')
