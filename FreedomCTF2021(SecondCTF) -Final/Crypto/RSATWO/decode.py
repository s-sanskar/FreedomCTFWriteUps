def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
        gcd = b
    return gcd, x, y

def main():

    p = 14978383016497116121
    q = 12968523063040435873
    e = 23
    ct = 65205298022099085283449917096537195340
    # run this a second time with:
    # 152080695252271793478056704090860133614
    # or make this varable an array

    # compute n
    n = p * q

    # Compute phi(n)
    phi = (p - 1) * (q - 1)

    # Compute modular inverse of e
    gcd, a, b = egcd(e, phi)
    d = a

    print( "n:  " + str(d))

    # Decrypt ciphertext
    pt = pow(ct, d, n)
    print( "pt: " + str(pt))

if __name__ == "__main__":
    main()
