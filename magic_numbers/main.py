from pathlib import Path
import math

def next_magic_num(num):
    stringNum = str(num)
    lenght = len(stringNum)

    if stringNum == str(9) * lenght:
        return num + 2

    half = (lenght + 1) // 2
    firstHalf = stringNum[:half]

    def makingMagicNum(h):
        if lenght % 2 == 0:
            return h + h[::-1]
        else:
            return h + h[:-1][::-1]

    magicN = makingMagicNum(firstHalf)

    if int(magicN) <= num:
        firstHalf = str(int(firstHalf) + 1)
        magicN = makingMagicNum(firstHalf)
        
    return magicN


def main():
    data = Path("input.txt").read_text(encoding="utf-8").splitlines()

    for line in data:
        stripped = line.strip()
        if stripped:
            if "^" in stripped:
                base, index = stripped.split("^")
                number = pow(int(base), int(index))
            else:
                number = int(stripped)
            
            print(next_magic_num(number))
            

    


if __name__ == "__main__":
    main()


