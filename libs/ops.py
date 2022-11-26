import include.analyzer

import libs.throw

def plus(vara:any, varb:any, file:str, line_num:int, line_content:str):
    return vara + varb

def minus(vara:any, varb:any, file:str, line_num:int, line_content:str):
    return vara - varb

def mult(vara:any, varb:any, file:str, line_num:int, line_content:str):
    return vara * varb

def divi(vara:any, varb:any, file:str, line_num:int, line_content:str):
    if varb != 0:
        return vara / varb
    else:
        libs.throw.Throw(file=file, line_num=line_num, line_content=line_content).exception(namespace='<script>', exc_type=include.analyzer.exception_types['ZeroDiv'])
        return False

def eq(varfin:any, vara:any, file:str, line_num:int, line_content:str):
    return vara