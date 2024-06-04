import matplotlib.pyplot as plt
import random

MAX = 100


class Point:
    def __init__(self, id: int, x: int, y: int):
        self.id = id
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f'({self.id}, {self.x}, {self.y})'


def dist_squere(a: Point, b: Point) -> int:
    return round(((a.x - b.x) ** 2 + (a.y - b.y) ** 2) ** 0.5, 2)


def random_point(id, max_x=MAX, max_y=MAX):
    return Point(id, random.randint(0, max_x), random.randint(0, max_y))


def draw_points(points, marks=None):
    xs = list(map(lambda p: p.x, points))
    ys = list(map(lambda p: p.y, points))
    colours = ['green'] * len(points)
    if marks:
        for i in marks:
            colours[i] = 'red'
    plt.scatter(xs, ys, color=colours)
    plt.show()


def sort_points(points: list, axis: str):
    if axis == 'x':
        return sorted(points, key=lambda p: p.x)
    return sorted(points, key=lambda p: p.y)


def filter(points,  midle_x, delta):
    repr = []
    for i in range(len(points)):
        if points[i].x > midle_x - delta and points[i].x < midle_x + delta:
            repr.append(points[i])
    return repr


def count_min_distance_simple(points):
    ans = (MAX, -1, -1)
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist = dist_squere(points[i], points[j])
            if ans[0] > dist:
                ans = (dist, points[i].id, points[j].id)
    return ans


def count_min_distance(p_x, p_y, min_x, max_x):
    if len(p_x[min_x: max_x]) < 4:
        return count_min_distance_simple(p_x[min_x: max_x])
    n = (max_x - min_x) // 2 + min_x
    d1 = count_min_distance(p_x, p_y, min_x, n)
    d2 = count_min_distance(p_x, p_y, n, max_x)
    if d1[0] < d2[0]:
        ans = d1
    else:
        ans = d2
    delta = min(d1[0], d2[0])
    middle_x = p_x[n].x
    filtered_y = filter(p_y, middle_x, delta)
    for i in range(len(filtered_y)):
        for j in range(i + 1, min(7, (len(filtered_y)))):
            d = dist_squere(filtered_y[i], filtered_y[j])
            if d < ans[0]:
                ans = (d, filtered_y[i].id, filtered_y[j].id)
    return ans


points = []
for i in range(30):
    points.append(random_point(i))
# ps = [(0, 11, 50), (1, 76, 73), (2, 92, 65), (3, 85, 37), (4, 96, 50), (5, 10, 60), (6, 13, 28), (7, 28, 36), (8, 68, 31), (9, 41, 8), (10, 6, 28), (11, 93, 87), (12, 38, 70), (13, 28, 16), (14, 55, 78), (15, 62, 27), (16, 41, 22), (17, 89, 74), (18, 4, 75), (19, 15, 55), (20, 81, 100), (21, 20, 24), (22, 17, 61), (23, 67, 17), (24, 61, 1), (25, 27, 47), (26, 45, 64), (27, 84, 100), (28, 26, 6), (29, 65, 32)]
# points = [Point(p[0], p[1], p[2]) for p in ps]
ans_simple = count_min_distance_simple(points)
sorted_points_x = sort_points(points, 'x')
sorted_points_y = sort_points(points, 'y')
ans = count_min_distance(sorted_points_x, sorted_points_y, 0, len(points))
# print(points)
print(ans, ans_simple)
draw_points(points, marks=[ans[1], ans[2]])
