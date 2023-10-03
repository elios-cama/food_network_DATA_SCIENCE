import csv
import matplotlib.pyplot as plt

# Initialize an empty dictionary to store category counts
category_counts = {}

# Define the input CSV file name
input_file = 'modified_shop_data.csv'

# Open the input CSV file
with open(input_file, mode='r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    # Count the occurrences of each category
    for row in csv_reader:
        category = row['category']
        if category in category_counts:
            category_counts[category] += 1
        else:
            category_counts[category] = 1

# Extract category names and counts
categories = list(category_counts.keys())
counts = list(category_counts.values())

# Create a vertical bar chart with rotated labels
plt.figure(figsize=(10, 6))
plt.bar(categories, counts, color='skyblue')
plt.xlabel('Category')
plt.ylabel('Count')
plt.title('Distribution of Categories')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Show the bar chart
plt.tight_layout()
plt.show()
