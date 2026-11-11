from typing import List, Tuple


def sum_3_integers(triplet: List[int]) -> int:
    one, two, three = triplet
    return one + two + three
    pass


def compute_volume(box_dimensions: Tuple[int, int, int]) -> int:
    width, length, height = box_dimensions
    return width * length * height
    pass
  

# do not modify below this line
print(sum_3_integers([1, 2, 3]))
print(sum_3_integers([4, 6, 2]))

print(compute_volume((1, 2, 3)))
print(compute_volume((3, 2, 1)))
print(compute_volume((3, 9, 7)))
