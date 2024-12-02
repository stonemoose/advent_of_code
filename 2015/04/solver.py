import hashlib

with open("input") as f:
    input = f.readline().strip()
    for i in range(10000000):
        result = hashlib.md5(f"{input}{i}".encode())
        if result.hexdigest()[:6] == "000000":
            print(f"6 zeros: {i}")
            break
        if result.hexdigest()[:5] == "00000":
            print(f"5 zeros: {i}")
