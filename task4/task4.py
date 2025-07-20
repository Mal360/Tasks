# Программа, выводящая минимальное количество ходов, требуемых для приведения всех элементов к одному числу
def task4(path):
    with open(path, 'r', encoding='utf-8') as file:
        nums = tuple(map(int, file.readlines()))

    median = sorted(nums)[len(nums) // 2]  # Поиск медианного значения
    t = 0  # Минимальное количество ходов
    for num in nums:
        while num != median:
            if num > median:
                num -= 1
            else:
                num += 1
            t += 1
    print(t)


if __name__ == "__main__":
    task4('numbers.txt')
