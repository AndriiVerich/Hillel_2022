# При помощи функции filter() из котрежа слов отфильтровать только те,
# которые являются полиндромами (слова которые читаются одинаково в обе стороны),
# регистр букв не учитывать.


inputdata = ['Страна', 'шалаш', 'Летел', 'вертолёт', 'УЧУ', 'мэм', 'язык']

def palindrome (input_list):
    out_list = []
    for item in input_list:
        counter = 0
        while counter <= len(item)/2:
            if item[counter].lower() != item[-1-counter].lower():
                break
            counter += 1
        else:
            out_list.append(item)
    return out_list



print(palindrome(inputdata))
