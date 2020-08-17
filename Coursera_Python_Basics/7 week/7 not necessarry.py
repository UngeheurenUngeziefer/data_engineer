# Дан список стран и городов каждой страны. Затем даны названия городов.
# Для каждого города укажите, в какой стране он находится.
# Программа получает на вход количество стран N. Далее идет N строк, каждая строка начинается с названия страны,
# затем идут названия городов этой страны. Название каждого город состоит из одного слова.
# В следующей строке записано число M, далее идут M запросов — названия каких-то M городов, перечисленных выше.

n = int(input())
councity = {}
for i in range(n):
    country, *cities = input().split()
    for city in cities:
        councity[city] = country
n2 = int(input())
for name in range(n2):
    city2 = input()
    print(councity[city2])
