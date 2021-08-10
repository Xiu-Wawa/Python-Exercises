# Create a program that asks our phone number. We type it in digits and then this will translate it into words.

phone_number = input('Phone #: ')
digits_mapping = {
    '0': 'Zero',
    '1': 'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four',
    '5': 'Five',
    '6': 'Six',
    '7': 'Seven',
    '8': 'Eight',
    '9': 'Nine'
}
output = ""
for char in phone_number:
    output += digits_mapping.get(char, "!") + " "
print(output)
