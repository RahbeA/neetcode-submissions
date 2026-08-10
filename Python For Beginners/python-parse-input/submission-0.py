from typing import List

def read_integers() -> List[int]:
    num = input("")
    lis = num.split(",")
    for n in lis:
        lis[lis.index(n)] = int(n)
    return lis

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
