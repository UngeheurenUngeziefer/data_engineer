# Как известно, в США президент выбирается не прямым голосованием, а путем двухуровневого голосования.
# Сначала проводятся выборы в каждом штате и определяется победитель выборов в данном штате.
# Затем проводятся государственные выборы: на этих выборах каждый штат имеет определенное число голосов
# — число выборщиков от этого штата. На практике, все выборщики от штата голосуют в соответствии с результатами
# голосования внутри штата, то есть на заключительной стадии выборов в голосовании участвуют штаты, имеющие различное
# число голосов. Вам известно за кого проголосовал каждый штат и сколько голосов было отдано данным штатом.
# Подведите итоги выборов: для каждого из участника голосования определите число отданных за него голосов.
# Каждая строка входного файла содержит фамилию кандидата, за которого отдают голоса выборщики этого штата,
# затем через пробел идет количество выборщиков,отдавших голоса за этого кандидата.

with open('input.txt', 'r') as f:
    nums = f.read().splitlines()
dict = {}

for i in nums:
    cand, vote = i.split()
    dict[cand] = dict.get(cand, 0) + int(vote)

for cand, vote in sorted(dict.items()):
    print(cand, vote)
