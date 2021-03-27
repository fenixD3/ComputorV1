import sys


def print_error(error_str):
    sys.stderr.write(error_str + '\n')
    exit(1)


def absolut(number):
    return number if number >= 0 else -number


def float_to_int(number):
    if number.is_integer():
        return int(number)
    return number


def sqrt(x, epsilon=10e-12):
    if x < 0:
        return None
    if x == 0:
        return 0
    u = 1
    v = x
    error_u = abs(u * u - x)
    error_v = abs(v * v - x)
    old_error_u = error_u
    old_error_v = error_v
    while error_u > epsilon and error_v > epsilon:
        tmp = u
        u = 2. / (1. / u + 1. / v)
        v = (tmp + v) / 2.
        error_u = abs(u * u - x)
        error_v = abs(v * v - x)
        if old_error_u == error_u and old_error_v == old_error_v:
            break
        old_error_u = error_u
        old_error_v = error_v

    return u if error_u <= error_v else v
