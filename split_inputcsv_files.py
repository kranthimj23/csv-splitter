import csv
import sys
import os

def split_csv(input_file, lines_per_file):
    try:
        # Ensure the lines_per_file is a positive integer
        lines_per_file = int(lines_per_file)
        if lines_per_file <= 0:
            raise ValueError("The number of lines per file must be greater than 0.")
    except ValueError as e:
        print(f"Invalid input for number of lines per file: {e}")
        sys.exit(1)

    # Read the input CSV file
    with open(input_file, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)

    # Calculate the number of files required
    total_rows = len(rows)
    num_files = (total_rows + lines_per_file - 1) // lines_per_file

    # Create output directory if it doesn't exist
    output_dir = 'output_files'
    os.makedirs(output_dir, exist_ok=True)

    # Split and write to new CSV files
    for i in range(num_files):
        start_index = i * lines_per_file
        end_index = min(start_index + lines_per_file, total_rows)
        output_file = os.path.join(output_dir, f'input{i + 1}.csv')

        with open(output_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(rows[start_index:end_index])

        print(f"Created file: {output_file}")

    print(f"Splitting complete. {num_files} file(s) created.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python split_csv.py <input_file> <lines_per_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    lines_per_file = sys.argv[2]

    if not os.path.isfile(input_file):
        print(f"The file {input_file} does not exist.")
        sys.exit(1)

    split_csv(input_file, lines_per_file)
