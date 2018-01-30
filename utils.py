import math


def get_radian(x1, y1, x2, y2):
    if (x2 - x1) == 0:
        return 0
    else:
        return math.atan2((y2 - y1), (x2 - x1))


if __name__ == '__main__':
    print(math.degrees(get_radian(0, 0, 1, 1)))
