from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    high_score = []
    names = []
    for name, score in scores:
        high_score.append(score)
        names.append(name)
    return names[high_score.index(max(high_score))]
    pass


# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
