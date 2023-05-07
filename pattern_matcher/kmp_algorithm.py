def search(pattern, text):
    m = len(pattern)
    n = len(text)

    matching_indexes = []

    if m > n or m == 0:
        return matching_indexes
    else:
        lps = create_lps(pattern)
        i = 0  # index for text
        j = 0  # index for pattern
        while (n - i) >= (m - j):
            if pattern[j] == text[i]:
                i += 1
                j += 1
    
            if j == m:
                matching_indexes.append(i-j)
                j = lps[j-1]
    
            # mismatch after j matches
            elif i < n and pattern[j] != text[i]:
                # Do not match lps[0..lps[j-1]] characters,
                # they will match anyway
                if j != 0:
                    j = lps[j-1]
                else:
                    i += 1
        return matching_indexes



#lps - longest proper prefix which is also a sufix
def create_lps(pattern):
    m = len(pattern)
    lps = [0]*m

    i = 1
    prefix_len = 0
    while i < m:
        if pattern[i] == pattern[prefix_len]:
            prefix_len += 1
            lps[i] = prefix_len
            i += 1
        else:
            if prefix_len == 0:
                lps[i] = 0
                i += 1
            else:
                prefix_len = lps[prefix_len - 1]

    return lps

if __name__ == '__main__':
    text_1 = "AABAACAADAABAAABAA"
    pattern_1 = "AABA"

    print(search(pattern_1, text_1))

    #do testów: dla wzoru 'ABXAB' lps to [0, 0, 0, 1, 2] 
    pattern_2 = "ABXAB"
    print(create_lps(pattern_2))