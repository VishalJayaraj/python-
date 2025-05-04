from collections import defaultdict

def group_anagrams(words):
    anagrams = defaultdict(list)
    for word in words:
        key = ''.join(sorted(word))
        anagrams[key].append(word)
    return list(anagrams.values())

print(group_anagrams(["bat", "tab", "eat", "tea", "tan", "nat"]))
