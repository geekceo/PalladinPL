import sys
import time
import include.parser
import include.lexer
import include.analyzer

tree = {}
syntax = {}
ops = {}
strokes = {}

buff = []

stop_chars = [
    include.analyzer.str_start,
    include.analyzer.bracket_start,
    include.analyzer.start_block,
    ' '
] + include.analyzer.ops_list

if (sys.argv[1]):
    with open(sys.argv[1], 'r') as f:
        time_start = time.time()

        for index, line in enumerate(f):

            print(include.lexer.lexer(line))


            #while include.parser.isBrackets(line):
            #    line = include.parser.bracketsContent(line)

            #    if not include.parser.getBeforeBrackets(line) in include.analyzer.syntax_keys_dict.keys():
            #        include.analyzer.func_not_found_error(line_num=index + 1, line=line, func_name=include.parser.getBeforeBrackets(line))
            #        break
            #    else:
            #        syntax[len(syntax) + 1] = include.parser.getBeforeBrackets(line)

            #    if include.parser.isBrackets(line):
            #        if not include.parser.brackets_validator(line):
            #            include.parser.brackets_error(line_num=index + 1, line=line)
            #            break
            #        
            #        


            #    if include.parser.isQuotes(line):
            #        if not include.parser.quotes_validator(line):
            #            include.analyzer.quotes_error(line_num=index + 1, line=line)
            #            break
            #        #strokes[len(strokes) + 1]
            #        
            #        print(include.parser.quotesContent(line))

                    

        print('Program end for {:.3f} s.'.format(time.time() - time_start))
