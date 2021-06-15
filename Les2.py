# 1
a = 15 * 3
b = 15 / 3
c = 15 // 2
d = 15 ** 2
print(type(a))
print(type(b))
print(type(c))
print(type(d))

# 2
arr = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
up_arr = []
for i in arr:
    if i.replace("+", "").replace("-", "").isdigit():
        if i.isdigit():
            up_arr.append(f'"{int(i):02}"')
        else:
            up_arr.append(f'"{i[0]}{int(i[1:]):02}"')
    else:
        up_arr.append(i)
print(up_arr)
print(' '.join(up_arr))

#4
n = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for i in n:
    print(f'Hello, {i.split()[-1].title()}')

#5
# A
prices = [55.30, 23, 35.23, 87, 65.50, 34.03, 25.01, 444, 555, 6]
for i in prices:
    r, k = str(f'{i:.2f}').split(".")
    print(f'{int(r):02d} рублей {int(k):02d} копеек')

# B
for i in prices:
    prices.sort()
    break
print(prices)

# C
for i in prices:
    n = sorted(prices, reverse=True)
    break
print(n)

# D
nn = n[:5]
for i in nn:
    nn.sort()
    break
print(nn)

