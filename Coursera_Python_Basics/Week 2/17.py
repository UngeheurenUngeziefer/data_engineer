# По данному натуральному n вычислите сумму 1²+2²+3²+...+n².
n = int(input())
rez = []
if n > 100:
    for i in range(1, 101):
        rez.append(i)
else:
    for i in range(1, n+1):
        rez.append(i)
print(sum(i * i for i in rez))
