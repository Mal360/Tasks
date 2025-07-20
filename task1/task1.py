# Программа, выводящая путь, по которому, двигаясь интервалом длины m по заданному массиву, концом будет являться первый элемент
def task1(n, m):  # n - Длина массива, m - Длина обхода
    array = [i for i in range(1, n + 1)]  # Круговой массив
    num = 0  # Последнее число интервала
    path = []  # Путь
    while num != 1:
        interval = []
        it = iter(array)
        for i in range(m):
            if interval:
                try:
                    interval.append(next(it))
                except StopIteration:
                    it = iter(array)
                    interval.append(next(it))
            else:
                for j in range(num - 1):
                    next(it)
                interval.append(next(it))
        num = interval[-1]
        path.append(interval[0])
    print(*path, sep='')
    print()


if __name__ == "__main__":
    n, m = map(int, input().split())
    task1(n, m)
