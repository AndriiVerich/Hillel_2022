int_parity = 2
int_noparity = 3
parity = lambda a: "Четное" if a % 2 == 0 else "Не четное"

print(parity(int_parity))
print(parity(int_noparity))
