# Вам дан словарь, состоящий из пар слов. Каждое слово является синонимом к парному ему слову.
# Все слова в словаре различны. Для одного данного слова определите его синоним.
# Программа получает на вход количество пар синонимов N.
# Далее следует N строк, каждая строка содержит ровно два слова-синонима. После этого следует одно слово.

n = int(input())
dict = {}
dict2 = {}
for i in range(n):
    word1, word2 = input().split()
    dict[word1] = word2
    dict2[word2] = word1
word3 = input()
if word3 in dict:
    print(dict[word3])
else:
    print(dict2[word3])
