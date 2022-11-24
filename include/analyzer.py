import include.parser
import include.analyzer
import libs.iostream
import libs.macses
import libs.ops


"""Tokens"""

ops_dict = {
    '+': libs.ops.plus,
    '-': libs.ops.minus,
    '*': libs.ops.mult,
    '/': libs.ops.divi,
    '=': libs.ops.eq
    }


macros_keys_dict = {
    'var': libs.macses.var,
    'del': None,
    'input': None,
    'output': libs.iostream.output
}

block_keys_list = [
    'for',
    'while',
    'func'
]

type_keys_dict = {
    'int': int,
    'float': float,
    'str': str
}

tokens_id = {
    'op': ops_dict,
    'macros': macros_keys_dict,
    'block': block_keys_list,
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
