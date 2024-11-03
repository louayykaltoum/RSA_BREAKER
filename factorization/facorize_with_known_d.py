from math import gcd
from random import randrange
import argparse


def argparser():
    parser = argparse.ArgumentParser(description='Factorize with known d')
    parser.add_argument('-n', type=int, help='modulus')
    parser.add_argument('-e', type=int, help='public exponent')
    parser.add_argument('-d', type=int, help='private exponent')
    return parser.parse_args()

def factorize(n, e, d):
    k = e * d - 1
    t = (k & -k).bit_length() - 1
    while True:
        g = randrange(1, n)
        for s in range(1, t + 1):
            x = pow(g, k >>s, n)
            p = gcd(x - 1, n)
            if 1 < p < n and n % p == 0:
                return p , n // p
            
def main():
    args = argparser()
    p, q = factorize(args.n, args.e, args.d)
    print(f'p = {p}\nq = {q}')
    print(f'n = p * q : { args.n == p * q}')

if __name__ == '__main__':
    main()