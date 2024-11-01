from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa


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
    return {
        "n": params.public_numbers.n,
        "e": params.public_numbers.e,
        "d": params.d,
        "p": params.p,
        "q": params.q,
    }

def public_key(key):
    params = serialization.load_pem_public_key(key, backend=default_backend())
    params = params.public_numbers()
    return {
        "n": params.n,
        "e": params.e,
    }

def main():
    key_path = "private_key.pem"
    type = check_key_type(open(key_path, "rb").read())
    if type == "private":
        params = privet_key(open(key_path, "rb").read())
        print(f'n: {params["n"]}\n',
              f'e: {params["e"]}\n',
              f'd: {params["d"]}\n',
              f'p: {params["p"]}\n',
              f'q: {params["q"]}\n')
    elif type == "public":
        params = public_key(open(key_path, "rb").read())
        print(f'n: {params["n"]}\n',
              f'e: {params["e"]}\n')
    else:
        print("Not a key")


if __name__ == "__main__":
    main()