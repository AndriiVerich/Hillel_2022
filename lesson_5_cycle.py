while True:
    number = input("Введите целое число: ")
    if not number.isdigit() or int(number) <= 0:
        print("Некоректный ввод")
        continue
    break
int_number = int(number)
counter = 0
sum_of_kub = 0
while True:
    if counter == int_number:
        break
    counter += 1
    if counter % 3 == 0:
        continue
    sum_of_kub += counter**3
print(sum_of_kub)

sum_of_kub = 0

for item in range(1, int_number+1):
    if item % 3 == 0:
        continue
    sum_of_kub += item**3
print(sum_of_kub)
