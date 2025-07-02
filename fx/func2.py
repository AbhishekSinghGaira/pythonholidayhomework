'''String's Permutation'''

def unique_permutations(s):
    result = []
    used = [False] * len(s)
    s = sorted(s)  # sort to detect duplicates

    def backtrack(path):
        if len(path) == len(s):
            result.append(''.join(path))
            return

        for i in range(len(s)):
            if used[i]:
                continue
            if i > 0 and s[i] == s[i-1] and not used[i-1]:
                continue  # skip duplicates
            used[i] = True
            backtrack(path + [s[i]])
            used[i] = False

    backtrack([])
    return result

# Input from user
s = input("Enter a string: ")
perms = unique_permutations(s)
print("Unique permutations:")
print(perms)
