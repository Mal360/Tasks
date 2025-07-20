# Программа, которая рассчитывает положение точки относительно окружности
def task2(path1, path2):
    with open(path1, 'r', encoding='utf-8') as file:
        coord_center_circle = tuple(map(float, file.readline().split()))  # Координаты центра окружности
        radius = float(file.readline())  # Радиус окружности

    coord_points = []  # Список координат точек
    with open(path2, 'r', encoding='utf-8') as file:
        for line in file.readlines():
            coord_points.append(tuple(map(float, line.split())))

    for i in range(len(coord_points)):
        point = (coord_points[i][0] - coord_center_circle[0]) ** 2 + (coord_points[i][1] - coord_center_circle[1]) ** 2
        radius_squared = radius ** 2
        if point == radius_squared:
            print(0)  # 0 - точка лежит на окружности
        elif point < radius_squared:
            print(1)  # 1 - точка внутри
        else:
            print(2)  # 2 - точка снаружи


if __name__ == "__main__":
    task2('circle.txt', 'dot.txt')
