class String(str):
    val = None

    def __init__(self, val):
        self.val = str(val)

    def __str__(self):
        return str(self.val)

    def __add__(self, other):
        return String(str(self.val) + str(other))

    def __sub__(self, other):
        if self.val.find(str(other)) != -1:
            val = list(self.val)
            count = 0
            while count < len(str(other)):
                val.pop(self.val.find(str(other)))
                count +=1
            return String(''.join(val))
        else:
            return String(self.val)


print(String('New') + String(890))
print(String(1234) + 5678)
print(String('New') + 'castle')
print(String('New') + 77)
print(String('New') + True)
print(String('New') + ['s',' ', 23])
print(String('New') + None)
print('-' * 30)
print(String('New bala7nce') - 7)
print(String('New balance') - 'bal')
print(String('New balance') - 'Bal')
print(String('pineapple apple pine') - 'apple')
print(String('New balance') - 'apple' )
print(String('NoneType') - None)
print(String(55678345672) - 7)


