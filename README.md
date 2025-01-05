# VVehicle Registration Number Selection (Commonly Practiced in India)

## Overview
This script processes numbers within a specified range to find those whose digit sum is given digit (1-9) and highlights numbers where the last two digits are greater than or equal to the first two digits. The results are then formatted into a table.

## Functions

### `digit_sum(n)`
Calculates the sum of digits of a number repeatedly until a single digit is obtained.

**Parameters:**
- `n` (int): The number to calculate the digit sum for.

**Returns:**
- `int`: The single digit sum of the number.

### `process_numbers(start, end)`
Processes numbers in the range `[start, end]` to find those whose digit sum is 9.

**Parameters:**
- `start` (int): The starting number of the range.
- `end` (int): The ending number of the range.

**Returns:**
- `list`: A list of numbers whose digit sum is 9.

### `highlight_numbers(numbers)`
Highlights numbers where the last two digits are greater than or equal to the first two digits.

**Parameters:**
- `numbers` (list): A list of numbers to be highlighted.

**Returns:**
- `list`: A list of highlighted numbers.

## Main Execution
1. Define the range and digit to be checked.
2. Process the numbers in the range to find those whose digit sum is given digit.
3. Highlight the numbers where the last two digits are greater than or equal to the first two digits.
4. Separate the highlighted numbers into series based on the first two digits.
5. Pad the shorter series with empty strings to match the length of the longest series.
6. Format the numbers into rows and columns.
7. Print the table of results.

## Example Usage
```python
# Variable to hold range and sumdigits.
start, end = 4000, 4500
digit = 9

# Main execution
numbers = process_numbers(start, end)
highlighted_numbers = highlight_numbers(numbers)

# Initialize a dictionary to hold series
series_dict = {}

# Separate numbers into series based on the first two digits
for num in highlighted_numbers:
    prefix = num[:2]
    if prefix not in series_dict:
        series_dict[prefix] = []
    series_dict[prefix].append(num)

# Determine the maximum length of the series
max_length = max(len(series) for series in series_dict.values())

# Pad the shorter series with empty strings to match the length of the longest series
for prefix in series_dict:
    series_dict[prefix] += [''] * (max_length - len(series_dict[prefix]))

# Initialize the formatted string
formatted_string = ""

# Iterate over the numbers and format them into rows and columns
for i in range(max_length):
    row = [series_dict[prefix][i] for prefix in sorted(series_dict.keys())]
    formatted_string += "\t".join(row) + "\n"

# Print the table of results
print("Numbers with a digit sum of " + str(digit) + " and last two digits >= first two digits \nfrom the range of " + str(start) + " to " + str(end) + ":")
print(formatted_string)
```


Numbers with a digit sum of 9 and last two digits >= first two digits from the range of 4000 to 4500:

```
4041	4149	4248	4347	4446
4050	4158	4257	4356	4455
4059	4167	4266	4365	4464
4068	4176	4275	4374	4473
4077	4185	4284	4383	4482
4086	4194	4293	4392	4491
4095												
```

-----