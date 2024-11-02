from Crypto.Util.number import *
import gmpy2

def small_exponent_attack(e, c):
    return gmpy2.iroot(c, e)[0]

def main():
    e = 3
    c = 1337
    m = small_exponent_attack(e, c)
    print(f"m: {long_to_bytes(m)}")


if __name__ == "__main__":
    main()