def select_sort(list, comp=lambda x, y: x < y):
    items = list[:]
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    return items


if __name__ == "__main__":
    print(select_sort([2, 3, 12, 3, 123, 21, 2314, 12, 3124, 98]))
