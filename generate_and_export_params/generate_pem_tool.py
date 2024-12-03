from Crypto.PublicKey import RSA
from Crypto.Util.number import *
import argparse


def parse():
    parser = argparse.ArgumentParser(description="Generate RSA keys with specified parameters.")
    parser.add_argument("--random", action='store_const', const=1, default=0, help="generate random primes for p and q")
    parser.add_argument("--type", type=str,default="all" ,help="type of the key u wanna generate (private/public/all)")
    parser.add_argument("-n", type=int, help="the modulus of the key (only needed for public key)")
    parser.add_argument("-p", type=int, help="First prime number (p) (only needed for private key)")
    parser.add_argument("-q", type=int, help="Second prime number (q) (only needed for private key)")
    parser.add_argument("-e", type=int, help="Public exponent (e)")
    parser.add_argument("--private", type=str, default="private_key.pem", help="Output file for private key")
    parser.add_argument("--public", type=str, default="public_key.pem", help="Output file for public key")
    args = parser.parse_args()
    return args

def generate_params(p, q, e):
    n = p * q
    phi_n = (p - 1) * (q - 1)
    d = inverse(e, phi_n)
    return n, e, d, p, q


def generate_public_key(n, e):
    key = RSA.construct((n, e))
    public_key_pem = key.export_key(format='PEM')
    return public_key_pem

def generate_private_key(n, e, d, p, q):
    key = RSA.construct((n, e, d, p, q))
    private_key_pem = key.export_key(format='PEM')
    return private_key_pem



def main():
    args = parse()
    if args.random:
        args.p = getPrime(1024)
        args.q = getPrime(1024)
        args.e = 65537    
    if args.type == "all":
        if args.p is None or args.q is None:
            print("p and q are required for private key generation")
            return
        n, e, d, p, q = generate_params(args.p, args.q, args.e)
        prive_key_pem = generate_private_key(n, e, d, p, q)
        public_key_pem = generate_public_key(n, e)
    elif args.type == "private":
        n, e, d, p, q = generate_params(args.p, args.q, args.e)
        prive_key_pem = generate_private_key(n, e, d, p, q)
        public_key_pem = None
    elif args.type == "public":
        public_key_pem = generate_public_key(args.n, args.e)
        prive_key_pem = None


    if prive_key_pem is not None:
        with open(args.private, "wb") as f:
            f.write(prive_key_pem)
    if public_key_pem is not None:
        with open(args.public, "wb") as f:
            f.write(public_key_pem)

if __name__ == "__main__":
    main()


