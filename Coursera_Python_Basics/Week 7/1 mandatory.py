# Дан список чисел, который может содержать до 100000 чисел.
# Определите, сколько в нем встречается различных чисел.
flist = list(map(int, input().split()))
fset = set(flist)
print(len(fset))
