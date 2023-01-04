import csv
import sys
import os

# Check if an input file was provided
if len(sys.argv) < 2:
  print('Usage: python program.py <input file>')
  sys.exit(1)

# Get the name of the input file from the command line
input_file = sys.argv[1]

# Construct the output file name
output_file = os.path.splitext(input_file)[0] + '.csv'

# Open the text file with the addresses
with open(input_file, 'r') as f:
  # Read the addresses into a list
  addresses = f.read().splitlines()

# Open the CSV file for writing
with open(output_file, 'w', newline='') as f:
  # Create a CSV writer
  writer = csv.writer(f)

  # Write the header row
  writer.writerow(['Address', 'Description'])

  # Write the address rows
  for address in addresses:
    writer.writerow([address, ''])
