import sys
import time
import include.parser
import include.lexer
import include.analyzer

import libs.builtin
import libs.iostream

ops_counter = {}

line_buffer = ''

inter_calcs = {}

line_variables = {}

if (sys.argv[1]):
    file = sys.argv[1]

    with open(file, 'r') as f:
        time_start = time.time()

        for index, line in enumerate(f):

            line_num = index + 1

            lt = include.lexer.lexerToAST(line)
            print(f'{lt["commands"]}\n\n{lt["linker"]}')

            for k, v in reversed(lt['linker'].items()):
                if v[0] in include.analyzer.ops_dict.keys():
                    prev_index = libs.builtin.getPairByIndex(k.split(':')[0], lt['commands'])
                    next_index = libs.builtin.getPairByIndex(k.split(':')[1], lt['commands'])

                    prev_val = prev_index[libs.builtin.getKeyFromDictPair(prev_index)](libs.builtin.getKeyFromDictPair(prev_index).split(':')[1])
                    next_val = next_index[libs.builtin.getKeyFromDictPair(next_index)](libs.builtin.getKeyFromDictPair(next_index).split(':')[1])

                    inter_calcs[k] = include.analyzer.ops_dict[v[0]](vara=prev_val, varb=next_val, file=file, line_num=line_num, line_content=line)

                    if inter_calcs[k] == False:
                        break


                    break

        print(inter_calcs)




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
