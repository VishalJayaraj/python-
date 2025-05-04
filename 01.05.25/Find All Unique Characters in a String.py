def unique_chars(s):
    return [c for c in s if s.count(c) == 1]

print(unique_chars("programming"))  
