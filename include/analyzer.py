import include.parser
import include.analyzer
import libs.iostream


"""Tokens"""

ops_list = ['+', '-', '*', '/', '=']

syntax_keys_list = [
    'var',
    'func',
    'input',
    'output',
    'for',
    'while'
]

tokens_id = {
    'op': ops_list,
    'syntax': syntax_keys_list
}

start_block = ':'

newline_block = ['   ', ' '*4]

end_block = ''

bracket_start = '('

bracket_end = ')'

str_start = '"'
str_end = '"'

brack_err = "Brackets Error, check brackets count in line: "

quotes_err = "Quotes Error, check quotes count in line: "

func_not_found_err = "Func Error,func with name '{0}' not found in line: {1}"

def brackets_error(line_num: int, line: str) -> None:
    print(f'###$$$ {line}')
    print(f'{brack_err} {line_num}')

def quotes_error(line_num: int, line: str) -> None:
    print(f'###$$$ {line}')
    print(f'{quotes_err} {line_num}')

def func_not_found_error(line_num: int, line: str, func_name: str):
    print(f'###$$$ {line}')
    print(f'{func_not_found_err.format(func_name, line_num)}')

def getStr(line: str):
    start = line.find('"')
