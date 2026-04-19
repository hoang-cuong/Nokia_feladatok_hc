from pathlib import Path

def min_num_of_drops(N, H):
    if N == 1:
        return H
    f = [0] * (N + 1)
    attempts = 0
    
    while f[N] < H:
        attempts += 1
        for n in range(N, 0, -1):
            f[n] = f[n] + f[n-1] + 1
            
    return attempts

def main():
    lines = Path("input.txt").read_text(encoding="utf-8").strip().splitlines()
    
    for line in lines:
        parts = line.split()
        if parts:
            N = int(parts[0])
            H = int(parts[1])
            print(min_num_of_drops(N, H))


if __name__ == "__main__":
    main()