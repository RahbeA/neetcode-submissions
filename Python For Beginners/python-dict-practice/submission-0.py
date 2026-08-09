from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    strlist = list(word) #["h", "e", "l", "l", "o"]
    strdic = {}
    for letter in strlist:
        num = 0
        for char in word:
            if char == letter:
                num += 1
        strdic[letter] = num
    return strdic




# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
