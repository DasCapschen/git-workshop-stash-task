import os


def main():
    with open('.env', 'r') as f:
        contents = f.readlines()
        for line in contents:
            sep = line.find("=")
            if line[0:sep] == "WORKSHOP_HTTPS":
                use_https = line[sep+1:]
            elif line[0:sep] == "WORKSHOP_ENV":
                dev_env = line[sep+1:]

    use_https = os.getenv("WORKSHOP_HTTPS")
    dev_env = os.getenv("WORKSHOP_ENV")

    if use_https is None or use_https == "false":
        print("Running Program insecurely.")
        if dev_env == "Production":
            print("Env is set to Production. Aborting.")
            exit(32)
        elif dev_env == "Development":
            print("Running Dev Server...")
            input()
        else:
            print("invalid value for env var WORKSHOP_ENV")
            exit(11)
    elif use_https == "true":
        print("Running Program securely.")
        if dev_env == "Production":
            print("Could not find SSL Certificate. Aborting")
            exit(44)
        elif dev_env == "Development":
            print("Running Dev Server...")
            create_self_sign_cert()
    else:
        print("invalid value for env var WORKSHOP_HTTPS")
        exit(12)


def create_self_sign_cert():
    print("Creating self-sign certificate...")

    # step 1, generate RSA
    p = 23629  # choose 2 big prime numbers
    q = 35671
    n = p * q
    phi = (p-1) * (q-1)
    e = 7  # is a prime, this guarantees gcd(e, phi) = 1

    gcd, d, _ = extended_euclid(e, phi)
    assert gcd == 1, gcd
    assert (e*d) % phi == 1


def extended_euclid(a, b):
    s = 1
    t = 0
    u = 0
    v = 1

    while b != 0:
        q = a // b  # integer division!!
        b1 = b
        b = a - q * b
        a = b1
        u1 = u
        u = s - q * u
        s = u1
        v1 = v
        v = t - q * v
        t = v1

    return a, s, t


if __name__ == "__main__":
    main()
