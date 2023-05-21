import sys
import re

remove_quotes = lambda string : re.sub(r'^"(.*)"$', r'\1', string)

def change_quote_char(input_file: str, output_file: str):
    with open(input_file, 'r') as inp, open(output_file, 'w', newline='') as out:
        for line in inp:
            line = line.strip()
            fields = line.split(',')
            fields = [f"|{remove_quotes(field)}|" for field in fields]
            out.write(','.join(fields) + '\n')

if __name__ == '__main__':
    input_file = sys.argv[1] or 'input.csv'
    output_file = sys.argv[2] or 'output.csv'
    change_quote_char(input_file, output_file)