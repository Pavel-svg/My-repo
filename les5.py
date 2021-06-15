#1
def odd_nums(n):
    for num in range(1, n + 1, 2):
        yield num
odd_to_n = odd_nums(15)
from itertools import islice
print(*islice(odd_to_n, None), sep=', ')
print(type(odd_to_n))

#5
from collections import Counter

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
my = [k for k, v in Counter(src).items() if v == 1]
print(my)

#3
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

n = (r for r in zip(tutors, klasses))

from itertools import islice

print(*islice(n, len(tutors)), sep='\n')
print(type(n))


#4
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [j for i, j in zip(src, src[1:]) if j > i]

print(result)