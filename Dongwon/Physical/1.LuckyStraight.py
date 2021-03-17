N = input()

a,b = N[:len(N)//2], N[len(N)//2:]

a = sum(map(int, list(a)))
b = sum(map(int, list(b)))

print("LUCKY" if a == b else "READY")