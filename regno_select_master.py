# %%
# Variable to hold range and sumdigits.
start, end = 4000, 5700
digit = 9

def digit_sum(n):
    """Calculates the sum of digits of a number repeatedly until a single digit is obtained."""
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

def process_numbers(start, end):
    """Process numbers in the range [start, end] to find those whose digit sum is 9."""
    result = []
    for num in range(start, end + 1):
        sum_of_digits = digit_sum(num)
        if sum_of_digits == digit:
            result.append(num)
    return result

def highlight_numbers(numbers):
    """Highlight numbers where last two digits are >= first two digits."""
    highlighted = []
    for num in numbers:
        first_two = num // 100  # Extract the first two digits
        last_two = num % 100   # Extract the last two digits
        if last_two >= first_two:
            #highlighted.append(f"**{num}**")  # Highlight with '**'
            highlighted.append(str(num))
        else:
            #highlighted.append(str(num))
            None
    return highlighted

# Main execution
# start, end = 4250, 5250
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
print("Numbers with a digit sum of "+ str(digit) +" and last two digits >= first two digits \nfrom the range of " + str(start) + " to " + str(end) + ":")
print(formatted_string)


