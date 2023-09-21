import sys
import csv

def main():
    # Check for the correct number of command-line arguments
    if len(sys.argv) != 3:
        sys.exit("Usage: python scourgify.py input.csv output.csv")

    # Get input and output file names from command-line arguments
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        with open(input_file, newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip the header row

            rows = []  # Store cleaned data
            for row in reader:
                name, house = row
                first, last = name.split(", ")
                rows.append([first, last, house])

        with open(output_file, mode='w', newline='') as csvfile:
            writer = csv.writer(csvfile)

            # Add the header row
            writer.writerow(['first', 'last', 'house'])

            writer.writerows(rows)

    except FileNotFoundError:
        sys.exit("Input file not found.")

if __name__ == "__main__":
    main()
