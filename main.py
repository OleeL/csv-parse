import csv

def change_quote_char(input_file, output_file):
    with open(input_file, 'r') as inp, open(output_file, 'w', newline='') as out:
        reader = csv.reader(inp)
        writer = csv.writer(out, quotechar='|', quoting=csv.QUOTE_MINIMAL)

        for row in reader:
            try:
                new_row = [field.replace('"', '""') for field in row]
                writer.writerow(new_row)
            except Exception as e:
                print(f"Error: {e} occurred while processing row: {row}")

change_quote_char('test.csv', 'output.csv')