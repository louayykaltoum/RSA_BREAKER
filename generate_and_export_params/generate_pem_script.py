from Crypto.PublicKey import RSA
from Crypto.Util.number import *

def generate_params(p, q, e):
    n = p * q
    phi_n = (p - 1) * (q - 1)
    d = inverse(e, phi_n)
    return n, e, d, p, q


def generate_rsa_keys(params):
    key = RSA.construct(params)
    private_key_pem = key.export_key(format='PEM')
    public_key_pem = key.publickey().export_key(format='PEM')

    return private_key_pem, public_key_pem

def main():
    p = getPrime(1024)
    q = getPrime(1024)
    e = 65537  

    params = generate_params(p, q, e)

    private_key_pem, public_key_pem = generate_rsa_keys(params)

    with open("private_key.pem", "wb") as f:
        f.write(private_key_pem)

    with open("public_key.pem", "wb") as f:
        f.write(public_key_pem)

    print("keys saved as private_key.pem and public_key.pem")

if __name__ == "__main__":
    main()
