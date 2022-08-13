while True:
    name = input("Введите имя: ").title()
    age = input("Введите возраст: ")
    if not age.isdigit() or int(age) <= 0:
        print("Ошибка, повторите ввод")
        continue
    elif int(age) < 10:
        print(f"Привет, шкет {name}")
    elif int(age) <= 18:
        print(f"Как жизнь {name}?")
    elif int(age) < 100:
        print(f"Что желаете {name}?")
    else:
        print(f"{name}, вы лжете - в наше время столько не живут...")

    exit_cod = input("Желаете выйти? (Д/Y): ").upper()

    if exit_cod == "Y" or "Д":
        break
