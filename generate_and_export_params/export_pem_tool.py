from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
import argparse

def parse():
    parser = argparse.ArgumentParser(description="export parameters from RSA pem key")
    parser.add_argument("-p", type=str, help="path to the private key pem file")
    args = parser.parse_args()
    return args

def check_key_type(key):
    try :
        serialization.load_pem_private_key(key, password=None, backend=default_backend())
        return "private"
    except:
        try:
            serialization.load_pem_public_key(key, backend=default_backend())
            return "public"
        except:
            return "not a key"
    
def privet_key(key):
    params = serialization.load_pem_private_key(key, password=None, backend=default_backend())
    params =  params.private_numbers()
    print(f'n : {params.public_numbers.n}\n',
          f'e : {params.public_numbers.e}\n',
          f'd : {params.d}\n',
          f'p : {params.p}\n',
          f'q : {params.q}\n')

def public_key(key):
    params = serialization.load_pem_public_key(key, backend=default_backend())
    params = params.public_numbers()
    print(f'n : {params.n}\n',
          f'e : {params.e}\n')
    

def main():
    args = parse()
    key_path = args.p
    type = check_key_type(open(key_path, "rb").read())
    if type == "private":
        print(f'type : {type} key\n')
        privet_key(open(key_path, "rb").read())
    elif type == "public":
        print(f'type : {type} key\n')
        public_key(open(key_path, "rb").read())
    else:
        print("Not a key")


if __name__ == "__main__":
    main()

