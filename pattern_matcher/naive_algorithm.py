def search(pattern, text):
    m = len(pattern)
    n = len(text)

    matching_indexes = []

    if m > n or m == 0:
        return matching_indexes
    else:
        for i in range(n - m + 1):
            j = 0
            while j < m:
                if text[i + j] != pattern[j]:
                    break
                j += 1

            if j == m:
                matching_indexes.append(i)
        return matching_indexes


if __name__ == '__main__':
    text_1 = "AABAACAADAABAAABAA"
    pattern_1 = "AABA"

    print(search(pattern_1, text_1))