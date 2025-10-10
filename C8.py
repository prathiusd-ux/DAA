import time

def lps(pattern):
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp(text, pattern):
    n = len(text)
    m = len(pattern)
    l_p_s = lps(pattern)
    j = 0
    i = 0
    results = []
    comparisons = 0
    while i < n:
        comparisons += 1
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            results.append(i - j)
            j = l_p_s[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = l_p_s[j - 1]
            else:
                i += 1
    return results, comparisons

def naive_search(text, pattern):
    n = len(text)
    m = len(pattern)
    results = []
    comparisons = 0
    for i in range(n - m + 1):
        match = True
        for j in range(m):
            comparisons += 1
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            results.append(i)
    return results, comparisons

text = "CATSABCBCABCDOGSABCBCABC"
pattern = "ABCBCABC"

start = time.perf_counter()
kmp_matches, kmp_comparisons = kmp(text, pattern)
end = time.perf_counter()
kmp_time = end - start

start = time.perf_counter()
naive_matches, naive_comparisons = naive_search(text, pattern)
end = time.perf_counter()
naive_time = end - start

print("Text:", text)
print("Pattern:", pattern)
print()
print("--- KMP Algorithm ---")
print("Pattern found at indices:", kmp_matches)
print("Comparisons:", kmp_comparisons)
print("Time taken:", round(kmp_time, 8), "seconds")
print()
print("--- Naive Search ---")
print("Pattern found at indices:", naive_matches)
print("Comparisons:", naive_comparisons)
print("Time taken:", round(naive_time, 8), "seconds")
