# CSV Quote Character Changer
This Python script changes the quote character in a CSV file. The script removes any enclosing quotes from fields, escapes quotes within fields by doubling them, and then re-quotes all fields. Additionally, the script changes the field delimiter from a comma to a pipe `(|)`.

## Usage
1. Navigate to the directory where the Python file is located.
2. Run the script with two arguments: the input file and the output file. Here is the syntax:


```sh
python3 <main.py> <input_file.csv> <output_file.csv>
```

If the script is run without specifying input_file and output_file arguments, it will default to 'input.csv' for input and 'output.csv' for output.