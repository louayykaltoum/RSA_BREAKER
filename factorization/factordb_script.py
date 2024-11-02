import requests

def factorize(n):
    url = f"http://factordb.com/api?query={n}"
    response = requests.get(url)
    data = response.json()
    if data["status"] == "FF":
        return data["factors"]
    return None

def main():
    n = 1337
    factors = factorize(n)
    if factors:
        for factor in factors:
            print(f'Factor: {factor[0]} , Power: {factor[1]}')
    else:
        print("Failed to factorize")

if __name__ == "__main__":
    main()