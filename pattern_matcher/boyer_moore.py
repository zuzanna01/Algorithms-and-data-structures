def last(pattern):
    dict = {}
    for i in range(len(pattern)):
        dict.update({pattern[i]: i})
        i += 1
    return dict


def search(pattern, text):
    list_results = []
    len_pattern = len(pattern)
    len_text = len(text)

    list_last = last(pattern)

    ck_index = 0
    while ck_index <= len_text - len_pattern:
        ck_pattern = len_pattern - 1
        while (ck_pattern >= 0 and
               text[ck_index + ck_pattern] == pattern[ck_pattern]):
            ck_pattern -= 1
        if ck_pattern < 0:
            list_results.append(ck_index)
            ck_index += 1
        else:
            if text[ck_index + ck_pattern] not in list_last:
                ck_index += len_pattern
            else:
                ck_index += (2 * len_pattern -
                             list_last[text[ck_index + ck_pattern]]
                             - 2
                             - ck_pattern)
    return list_results
