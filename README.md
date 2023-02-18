## Prototype a function in max.:
- takes as input a long stream of (data:string, cost:int)-tuples, e.g.
    from a generator outputting ("abcdewer", 24), ("lkle", 4), ("ouwecks", 31), ...
- and returns a generator outputting the same stream of tuples, but such that every `n` elements are sorted in descending 