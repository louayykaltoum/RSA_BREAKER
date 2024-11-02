import gmpy2
import argparse
from Crypto.Util.number import long_to_bytes

def parse_args():
    parser = argparse.ArgumentParser("RSA Wiener Attack")
    parser.add_argument("-n", type=int, required=True, help="Modulus"  )
    parser.add_argument("-e", type=int, required=True, help="Public exponent")
    parser.add_argument("-c", type=int, required=True, help="Ciphertext")
    return parser.parse_args()

def convergents(e):
    n = [] 
    d = [] 
    for i in range(len(e)):
        if i == 0:
            ni , di = e[i] , 1
        elif i == 1:
            ni , di = (e[i]*e[i-1] + 1) , (e[i])
        else: 
            ni , di  = (e[i]*n[i-1] + n[i-2]) , (e[i]*d[i-1] + d[i-2])
        n.append(ni)
        d.append(di)
    return n,d

def get_cf_expansion(e, n):
    cf_list = []
    while n != 0:
        q = e // n
        cf_list.append(q)
        e, n = n, e % n
    return cf_list


def main():
    args = parse_args()
    N , e , c  = args.n , args.e , args.c
    cf_expansion = get_cf_expansion(e, N)
    for i in range(len(cf_expansion)):
        guess_expansion = cf_expansion[:i]
        if i % 2 == 0:
            guess_expansion.append(cf_expansion[i] + 1)
        else:
            guess_expansion.append(cf_expansion[i])
        
        numerators, denominators = convergents(guess_expansion)
        k ,d = numerators[i] , denominators[i]
        ed = e * d
        phi , g = ed // k , ed % k
        
        if (N - phi + 1) % 2 == 1:
            continue
        
        p_plus_q_by_2 = (N - phi + 1) // 2
        p_minus_q_by_2_sq = p_plus_q_by_2**2 - N
        
        if gmpy2.iroot(p_minus_q_by_2_sq, 2)[1]:
            print(f"D: {d // g}")
            print(f"message: {long_to_bytes(pow(c, d, N))}")
            break

if __name__ == "__main__":
    main()