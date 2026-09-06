def is_anagram(test, original):
    
    return len(test)==len(original) and set(test.lower())==set(original.lower())

print(is_anagram("Buckethead", "DeathCubeK"))