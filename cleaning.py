import csv

# Define the input and output file names
input_file = 'shop_data.csv'
output_file = 'modified_shop_data.csv'

# Open the input and output CSV files
with open(input_file, mode='r', encoding='utf-8') as input_csv, \
     open(output_file, mode='w', newline='', encoding='utf-8') as output_csv:
    
    # Create CSV reader and writer objects
    csv_reader = csv.DictReader(input_csv)
    fieldnames = ['name', 'category']
    csv_writer = csv.DictWriter(output_csv, fieldnames=fieldnames)
    
    # Write the header row
    csv_writer.writeheader()
    
    # Process and write each row
    for row in csv_reader:
        # Split the categories by comma and create a list
        categories = row['category'].split(', ')
        
        # Create a new row with separate columns for each category
        for category in categories:
            new_row = {
                'name': row['name'],
                'category': category
            }
            # Write the new row to the output CSV file
            csv_writer.writerow(new_row)

print(f"Data has been modified and saved to {output_file}.")
