def format_phone_number(phone_number:str):

    only_digit = ''.join(filter(str.isdigit, phone_number))

    if not only_digit.startswith('0'):
        return "Invalid phone number"
    
    if len(only_digit) != 10:
        return "Invalid phone number"
    
    formatted_number = '+84' + only_digit[1:]
    return formatted_number

phone_number = input("phone number:  ")
print(format_phone_number(phone_number))

