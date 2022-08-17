int_parity = 2
int_noparity = 3
parity = lambda a: "Четное" if a % 2 == 0 else "Не четное"

print(int_parity, parity(int_parity))
print(int_noparity, parity(int_noparity))
