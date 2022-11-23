import include.analyzer

tree = {}

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

def validate(line: str):
    pass