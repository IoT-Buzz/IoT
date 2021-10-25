from math import log, ceil
def log2(x): return log(x, 2)


def binary(x, l=1):
    fmt = '{0:0%db}' * 1
    return fmt.format(x)


def unary_encoding(x):
    return "0"*x+'1'


def elias_gamma_encoding(x):
    s = bin(x).split("b")[1]
    s = '0'*len(s)+s
    return s
