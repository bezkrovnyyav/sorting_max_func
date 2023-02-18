"""
 Prototype a function in max. 15 minutes that:

     - takes as input a long stream of (data:string, cost:int)-tuples, e.g.
    from a generator outputting ("abcdewer", 24), ("lkle", 4), ("ouwecks", 31), ...

     - and returns a generator outputting the same stream of tuples, but such that every `n` elements are sorted in descending order according to cost, e.g. ("abcdewer", 31), ("lkle", 24), ("ouwecks", 4), ...
"""
from __future__ import annotations

from collections.abc import Generator


def sort_gen_chunks(
    long_list: Generator[tuple[str, int], None, None], n: int = 3
) -> Generator[tuple[str, int], None, None]:
    """
    Hints:
        - There is more than one way to implement sorting of a list of tuples.
        - Most likely you will need to use `sorted()` function with `key` and `reverse` passed arguments.
        - Remember that you receive and return a generator, so you must use 'yield' keyword in your function.
    """
    long_list = list(long_list)
    for i in range(0, len(long_list), n):
        decomposed_list = long_list[i:i + n]
        sorted_list = sorted(decomposed_list, key=lambda x: x[1], reverse=True)

        if len(sorted_list) == n:
            for j in range(n):
                yield sorted_list[j]




# This is our input data:
items_gen = (item for item in [("Apple", 4), ("Plum", 9), ("Orange", 1), ("Pear", 3), ("Cherry", 8), ("Mango", 5), ("Grape", 2), ("Kiwi", 59)])

# This is what you must get. As you see, every 'n' tuples are sorted:
expected_result = [('Plum', 9), ('Apple', 4), ('Orange', 1), ('Cherry', 8), ('Mango', 5), ('Pear', 3)]

# Checking your result...
result = list(sort_gen_chunks(items_gen, n=3))
print(f"your result:\n {result}")
print(f"\nexpected result:\n {expected_result}")
if result != expected_result:
    raise Exception("Wrong result")
