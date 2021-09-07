phone = input('Phone:')
digits_map = {
    '1': 'One',
    '2': 'Two',
    '3': 'Three'
}
output = ''
for char in phone:
    output += digits_map.get(char, '!') + ''
print(output)