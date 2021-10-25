from math import log, ceil
def log2(x): return log(x, 2)


def decimal(binary):
    decimal = 0
    for digit in binary:
        decimal = decimal*2 + int(digit)
    return decimal


def unary_decoding(x):
    i = 0
    while (x[i] != "1"):
        i += 1
    return i


def elias_gamma_decoding(x):
    return int(x[x. index('1'):], 2)
