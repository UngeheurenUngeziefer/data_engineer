# На Новом проспекте для разгрузки было решено пустить два новых автобусных маршрута на разных участках проспекта.
# Известны конечные остановки каждого из автобусов. Определите количество остановок,
# на которых можно пересесть с одного автобуса на другой.
# Вводятся четыре числа, не превосходящие 100, задающие номера конечных остановок.
# Сначала для первого, потом второго автобуса (см. примеры и рисунок).

s = list(map(int, input().split()))
a, b, c, d = s[0], s[1], s[2], s[3]
set1 = set(range(min(a, b), max(a, b) + 1))
set2 = set(range(min(c, d), max(c, d) + 1))
e = (set1 & set2)
print(len(list(e)))
