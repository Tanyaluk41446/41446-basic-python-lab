text = input().strip()
first_char = text[0].lower()
second_char = text[-1].lower()
if first_char < second_char:
    print('A comes before B')
elif first_char > second_char:
    print('A comes after B')
else:
    print('A equals B')