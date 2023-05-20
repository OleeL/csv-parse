import csv
import re

def remove_quotes(string):
    pattern = r'^"(.*)"$'
    replacement = r'\1'
    result = re.sub(pattern, replacement, string)
    return result

def change_quote_char(input_file, output_file):
    with open(input_file, 'r') as inp, open(output_file, 'w', newline='') as out:
        for line in inp:
            line = line.strip()
            fields = line.split(',')
            fields = ['"' + remove_quotes(field).replace('"', '""') + '"' for field in fields]
            out.write('|'.join(fields) + '\n')

change_quote_char('input.csv', 'output.csv')