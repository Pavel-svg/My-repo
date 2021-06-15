#1
my_dict = {'zero': 'нуль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'чертыре', 'five': 'пять', 'six': 'шесть',
           'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}

def translator(i):
    print(my_dict.get(i))


translator('zero')

#3
def func_name(*args):
    d_name = {}
    for i in args:
        letter = i[0]
        if letter in d_name:
            d_name[letter] += [i]
        else:
            d_name[letter] = [i]
    return d_name

print(func_name('Иван', 'Мария', 'Кардамон', 'Бенидикт', 'Шустрый', 'Магамед', 'Индус'))
