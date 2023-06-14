#!/usr/bin/env python3
#@Author: Akash Manna
#@Date:14/05/2023

import os
import json
import matplotlib.pyplot as plt

# Specify the directory containing the Labelme annotated JSON files
json_dir = '/media/depak/HDD/shared/aug_data_29_05_23_img4050'
# Create a dictionary to hold the category counts
category_counts = {}

corrupt_file = []
# Loop through the JSON files in the directory
counter= 0
for json_file in os.listdir(json_dir):
    print("[Manna-log]: Processing: ", json_file)
    try:
        if json_file.endswith('.json'):
            # Load the JSON file as a Python dict
            with open(os.path.join(json_dir, json_file)) as f:
                data = json.load(f)

            # Count the number of annotations in the file for each category
            for annotation in data['shapes']:
                category = annotation['label']
                if category not in category_counts:
                    category_counts[category] = 0
                category_counts[category] += 1
    except:
        corrupt_file.append(json_file)
    counter+=1
    print(f"Images analysed: {counter}")

print("[Manna-log]: List of corrpupted files is: ", corrupt_file)
        

# Plot the results
categories = list(category_counts.keys())
counts = list(category_counts.values())

# Create a bar plot
fig, ax = plt.subplots(figsize=(8, 6))
ax.bar(categories, counts)

# Add text annotations to the bars
ax.bar_label(ax.containers[-1], label_type='edge')

ax.set_xlabel('Category')
ax.set_ylabel('# annotations')
ax.set_xticklabels(categories, rotation=90)
# Show the plot
plt.show()

# fig = plt.figure(figsize=(8, 6))

# plt.bar(categories, counts)
# plt.xticks(rotation=90)
# plt.xlabel('Category')
# plt.ylabel('Number of annotations')
# plt.title('Number of annotations in Labelme annotated JSON files by category')
# plt.show()
