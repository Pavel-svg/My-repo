#1
with open("nginx_logs.txt", "r", encoding="utf-8") as file_1:
    sample = ((line.split()[0], line.split()[5][1:], line.split()[6]) for line in file_1)
    for j in sample:
        print(j)


#3
from json import dump
from itertools import zip_longest

with open("users.csv", "r", encoding="utf-8") as user:
    with open("hobby.csv", "r", encoding="utf-8") as hobby:

        if len(user.readline()) > len(hobby.readline()):
            with open("user_hobby.json", "w", encoding="utf-8") as uh:
                all_data = zip_longest(user, hobby, fillvalue=None)
                my_dict = {str(el[0]).strip().replace(",", " "): (el[1].strip()) for el in all_data}

                dump(my_dict, uh, ensure_ascii=False, indent=4)
            print(my_dict)
        else:
            exit(1)

