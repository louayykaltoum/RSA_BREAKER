from sympy import *
from Crypto.Util.number import getPrime
import argparse


def get_args():
    parser = argparse.ArgumentParser("Fermat factorization")
    parser.add_argument("-n", type=int, help="number to factorize",required=True)
    return parser.parse_args()

def fermat(n):
    a = int(n ** 0.5)
    for i in range(2**50):
        temp = a+i 
        if ( isprime(temp) and n%temp == 0 and isprime(n//temp)):
            return temp , n // temp
def main():
    args = get_args()
    p, q = fermat(args.n)
    print(f'p: {p}\n',
          f'q: {q}\n')

if __name__ == "__main__":
    main()