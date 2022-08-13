old_dict = {'aa': 1, 'b': 2, 'cccc': 3}
print(old_dict)
new_dict = {value: key for key, value in old_dict.items()}
print(new_dict)
