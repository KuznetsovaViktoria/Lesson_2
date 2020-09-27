def quicksort(d, start, end):
    if end - start > 1:
        p = partition(d, start, end)
        quicksort(d, start, p)
        quicksort(d, p + 1, end)


def partition(d, start, end):
    mid = d[start]
    i = start + 1
    j = end - 1
    while True:
        while (i <= j and d[i] <= mid):
            i = i + 1
        while (i <= j and d[j] >= mid):
            j = j - 1
        if i <= j:
            d[i], d[j] = d[j], d[i]
        else:
            d[start], d[j] = d[j], d[start]
            return j


d = input('Enter the list of numbers: ').split()
d = [int(x) for x in d]
quicksort(d, 0, len(d))
print('Sorted list: ', end='')
print(*d)