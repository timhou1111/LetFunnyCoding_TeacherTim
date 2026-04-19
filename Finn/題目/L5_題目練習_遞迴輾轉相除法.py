def find_gcd(a,b):
    if a % b == 0:
        return b
    return find_gcd(b , a%b)

print(find_gcd(16, 12))

