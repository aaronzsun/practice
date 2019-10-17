# prints permutations of a word | runtime: O(n^2 * n!)
def perm(word, prefix):
    if len(word) == 0:
        print(prefix)
    else:
        for i in range(0, len(word)):
            hold = word[:i] + word[i + 1:]
            perm(hold, prefix + word[i])


perm("Hello", "")
