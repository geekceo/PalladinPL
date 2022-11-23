import sys
import include.parser
import include.analyzer


if (sys.argv[1]):
    with open(sys.argv[1], 'r') as f:
       for index, line in enumerate(f):
            if not include.parser.brackets_validator(line):
                include.analyzer.brackets_error(line_num=index + 1, line=line)
