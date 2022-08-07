
input_word_1 = input("Введите два слова: ").split()

word_new_1 = "!" + str(input_word_1[1]).upper() + " " + str(input_word_1[0]).title() + "?"
word_new_2 = "!{} {}?".format(input_word_1[1].upper(), input_word_1[0].title())
word_new_3 = f"!{input_word_1[1].upper()} {input_word_1[0].title()}?"

s_file= open("python.txt", "w")

print(str(input_word_1[0]) + " " + str(input_word_1[1]), file=s_file, end="<<<>>>")
print(word_new_1, file=s_file, end="<<<>>>")
print(word_new_2, file=s_file, end="<<<>>>")
print(word_new_3, file=s_file)

s_file.close()
