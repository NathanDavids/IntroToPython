import re

def validate_phone_number(number):
    # Define the pattern for the phone number format
    pattern = r'\+27\d{2}-\d{3}-\d{4}'
    
    # Check if the number matches the pattern
    if re.match(pattern, number):
        return "The number is in the correct format."
    else:
        return "Error: Incorrect format or wrong country code. \n ============== RESTART =================="

# Prompt the user to enter a phone number
phone_number = input("Enter a cell phone number in the format +2778-123-4567: ")

# Validate the phone number
result = validate_phone_number(phone_number)
print(result)