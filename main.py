import sys
import re

def remove_quotes(string: str):
    pattern = r'^"(.*)"$'
    replacement = r'\1'
    result = re.sub(pattern, replacement, string)
    return result

def change_quote_char(input_file: str, output_file: str):
    with open(input_file, 'r') as inp, open(output_file, 'w', newline='') as out:
        for line in inp:
            line = line.strip()
            fields = line.split(',')
            fields = ['"' + remove_quotes(field).replace('"', '""') + '"' for field in fields]
            out.write('|'.join(fields) + '\n')

if __name__ == '__main__':
    input_file = sys.argv[1] or 'input.csv'
    output_file = sys.argv[2] or 'output.csv'
    change_quote_char(input_file, output_file)