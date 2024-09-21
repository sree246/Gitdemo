def sum_numbers(input_string):
    num_str = ''  # Initialize an empty string to store the current number
    total_sum = 0  # Initialize the total sum of numbers
    for char in input_string:
        if char.isdigit():  # Check if the character is a digit
            num_str += char  # Add the digit to the current number string
        elif num_str:  # If we have a non-empty number string
            total_sum += int(num_str)  # Convert the number string to integer and add to total sum
            num_str = ''  # Reset the number string
    # Add the last number if there's any remaining
    if num_str:
        total_sum += int(num_str)
    return total_sum

# Test the function with sample input
input_string = "guvi21 world 32 hell67all"
output = sum_numbers(input_string)
print("Total sum of numbers:", output)

