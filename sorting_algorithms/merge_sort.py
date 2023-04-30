def merge_sort(array):
    if array == []:
        return []

    groups = []
    for number in array:
        groups.append([number])

    while len(groups) > 1:
        group1, group2 = groups.pop(0), groups.pop(0)
        new_group = []
        while not (len(group1) == len(group2) == 0):
            if len(group1) == 0:
                new_group += group2
                break
            if len(group2) == 0:
                new_group += group1
                break
            if group1[0] > group2[0]:
                new_group.append(group2.pop(0))
            else:
                new_group.append(group1.pop(0))
        groups.append(new_group)
    return groups[0]

if __name__ == '__main__':
    print(merge_sort([3,5,2,-1,2]))