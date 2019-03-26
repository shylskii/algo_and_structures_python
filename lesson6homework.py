# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
# Результаты анализа вставьте в виде комментариев к коду.
# Также укажите в комментариях версию Python и разрядность вашей ОС.

# разрадность ОС - 64bit

from memory_profiler import profile


# Первая задача:

@profile
def cycle_sum(n):
    res = 1
    elem = 1

    for i in range(1, n):
        elem *= -0.5
        res += elem

    return res

n = 600

print("Сумма ряда: %f" % cycle_sum(n))


"""
Вывод от memory_profiler:
Line #    Mem usage    Increment   Line Contents
================================================
    20     14.3 MiB     14.3 MiB   @profile
    21                             def cycle_sum(n):
    22     14.3 MiB      0.0 MiB       res = 1
    23     14.3 MiB      0.0 MiB       elem = 1
    24
    25     14.3 MiB      0.0 MiB       for i in range(1, n):
    26     14.3 MiB      0.0 MiB           elem *= -0.5
    27     14.3 MiB      0.0 MiB           res += elem
    28
    29     14.3 MiB      0.0 MiB       return res
функция cycle_sum() использует 14.3 Мбайт без приращений памяти
"""

# Вторая задача:



@profile
def find_prime_erotosfen(i):
    if i > 1:
        n = i ** 2
    else:
        n = 3
    a = [x for x in range(n)]

    a[1] = 0

    m = 2
    cur_count = 0
    while m < n:
        if a[m] != 0:
            cur_count += 1
            if cur_count == i:
                return a[m]
            j = m * 2
            while j < n:
                a[j] = 0
                j = j + m
        m += 1

i = 100

print("Найдено %d-ое простое число через решето Эратосфена: %d" % (i, find_prime_erotosfen(i)) )



"""
Вывод от memory_profiler:
Line #    Mem usage    Increment   Line Contents
================================================
    59     14.3 MiB     14.3 MiB   @profile
    60                             def find_prime_erotosfen(i):
    61     14.3 MiB      0.0 MiB       if i > 1:
    62     14.3 MiB      0.0 MiB           n = i ** 2
    63                                 else:
    64                                     n = 3
    65     14.7 MiB      0.3 MiB       a = [x for x in range(n)]
    66
    67     14.7 MiB      0.0 MiB       a[1] = 0
    68
    69     14.7 MiB      0.0 MiB       m = 2
    70     14.7 MiB      0.0 MiB       cur_count = 0
    71     14.7 MiB      0.0 MiB       while m < n:
    72     14.7 MiB      0.0 MiB           if a[m] != 0:
    73     14.7 MiB      0.0 MiB               cur_count += 1
    74     14.7 MiB      0.0 MiB               if cur_count == i:
    75     14.7 MiB      0.0 MiB                   return a[m]
    76     14.7 MiB      0.0 MiB               j = m * 2
    77     14.7 MiB      0.0 MiB               while j < n:
    78     14.7 MiB      0.0 MiB                   a[j] = 0
    79     14.7 MiB      0.0 MiB                   j = j + m
    80     14.7 MiB      0.0 MiB           m += 1
функция find_prime_erotosfen() использует 14.7 Мбайт
фиксируется приращение в 0.3 Мбайт из-зи создания массива для решета Эратосфена
"""



# Третья задача:



@profile
def find_prime(i):
    cur_count = 0
    n = 2
    while True:
        d = 2
        while d*d <= n and n%d != 0:
            d += 1
        if (d*d > n):
            cur_count += 1
            if cur_count == i:
                return n
        n += 1


print("Найдено %d-ое простое число без решета Эратосфена: %d" % (i, find_prime(i)))



"""
Вывод от memory_profiler:
Line #    Mem usage    Increment   Line Contents
================================================
   119     14.5 MiB     14.5 MiB   @profile
   120                             def find_prime(i):
   121     14.5 MiB      0.0 MiB       cur_count = 0
   122     14.5 MiB      0.0 MiB       n = 2
   123     14.5 MiB      0.0 MiB       while True:
   124     14.5 MiB      0.0 MiB           d = 2
   125     14.5 MiB      0.0 MiB           while d*d <= n and n%d != 0:
   126     14.5 MiB      0.0 MiB               d += 1
   127     14.5 MiB      0.0 MiB           if (d*d > n):
   128     14.5 MiB      0.0 MiB               cur_count += 1
   129     14.5 MiB      0.0 MiB               if cur_count == i:
   130     14.5 MiB      0.0 MiB                   return n
   131     14.5 MiB      0.0 MiB           n += 1
т.е. функция find_prime() использует 14.5 Мбайт без приращений
"""