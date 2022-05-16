import json

card_number = list(input("Please enter a card number: ").strip())

check_digit = card_number.pop()

card_number.reverse()
print(card_number[2])

