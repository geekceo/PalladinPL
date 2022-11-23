import include.analyzer

tree = {}

"""Brackets Analyzer"""

def getBeforeBrackets(line: str) -> str:
    first_bracket = line.find(include.analyzer.bracket_start)

    return line[0:first_bracket]

def isBrackets(line: str) -> bool:
    return (include.analyzer.bracket_start in line or include.analyzer.bracket_end in line)

def brackets_validator(line: str):
    #start = line.find(analyzer.bracket_end)

    brackets_start_dict = {}
    brackets_end_dict = {}

    for index, c in enumerate(line):
        if c == include.analyzer.bracket_start:
            brackets_start_dict[index] = include.analyzer.bracket_start

    for index, c in enumerate(line):
        if c == include.analyzer.bracket_end:
            brackets_end_dict[index] = include.analyzer.bracket_end

    return True if len(brackets_start_dict) == len(brackets_end_dict) else False

def bracketsContent(line: str) -> str:
    brackets_start_dict = {}
    brackets_end_dict = {}

    for index, c in enumerate(line):
        if c == include.analyzer.bracket_start:
            brackets_start_dict[index] = include.analyzer.bracket_start

    for index, c in enumerate(line):
        if c == include.analyzer.bracket_end:
            brackets_end_dict[index] = include.analyzer.bracket_end

    return line[min(brackets_start_dict.keys()) + 1:max(brackets_end_dict.keys())]


"""Quotes Analyzer"""

def isQuotes(line: str) -> bool:
    return include.analyzer.str_start in line

def quotes_validator(line: str):
    quotes_start_dict = {}

    for index, c in enumerate(line):
        if c == include.analyzer.str_start:
            quotes_start_dict[index] = include.analyzer.str_start

    return True if len(quotes_start_dict) % 2 == 0 else False

def quotesContent(line: str) -> str:
    return line[1:len(line) - 1]




def validate(line: str):
    pass