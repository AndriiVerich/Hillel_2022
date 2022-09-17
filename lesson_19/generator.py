# Создать генератор геометрической прогрессии
def simple_generator(start, step):
    val = 0
    while True:
        if val == 0:
            val = start
            yield val
        val *= step
        yield val


for item in simple_generator(1, 2):
    print(item)
    if item >=500:
        break
