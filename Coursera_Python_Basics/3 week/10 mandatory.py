# Дана строка. Если в этой строке буква f встречается только один раз, выведите её индекс. Если она встречается два и
# более раз, выведите индекс её первого и последнего появления. Если буква f в данной строке не встречается,
# ничего не выводите. При решении этой задачи нельзя использовать метод count и циклы.

S = input()
A = S.find('f')
B = S.rfind('f')
if A == -1:
    print()
elif A == B:
    print(A)
else:
    print(A, B)
