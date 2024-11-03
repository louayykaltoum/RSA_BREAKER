
from sympy.ntheory.modular import crt
import gmpy2
from Crypto.Util.number import long_to_bytes
import argparse

def parse_args():
    parser = argparse.ArgumentParser("Hastad's Broadcast Attack")
    parser.add_argument("-ns", type=str, required=True, help="path to file containing moduls")
    parser.add_argument("-cs", type=str, required=True, help="path to file containing ciphertexts")
    parser.add_argument("-e", type=int, required=True, help="public exponent")
    return parser.parse_args()

def read(path):
    with open(path, "r") as f:
        for lines in f:
            l = int(lines.strip())
            yield l

def hastad_broadcast_attack(ns ,cs, e):
    m = crt(ns, cs)[0]
    return gmpy2.iroot(m,e)[0]


def main():
    args = parse_args()
    ns , cs , e = args.ns, args.cs, args.e
    ns = list(read(ns))
    cs = list(read(cs))
    m = hastad_broadcast_attack(ns ,cs, e)
    print(f"m: {long_to_bytes(m)}")

if __name__ == "__main__":
    main()