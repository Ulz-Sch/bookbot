#!/bin/bash

# Loop through all txt files in the directory
for file in *.txt; do
    # Extract the title from line 11
    title=$(sed -n '11p' "$file" | sed 's/^Title: //')

    # Clean the title to make it a valid filename (replace spaces with underscores, remove invalid characters)
    title=$(echo "$title" | tr -s '[:space:]' '_' | tr -d '[:punct:]')

    # Rename the file
    mv "$file" "${title}.txt"
done

