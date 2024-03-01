def array_diff(a, b):
    # your code here
    for i, j in enumerate(a):
        for n in b:
            if j == n:
                del(a[i])
    print(a)


array_diff([1,2], [1])
array_diff([1,2,2], [1])
array_diff([1,2,2], [2])
array_diff([1,2,2], [])
array_diff([], [1,2])
array_diff([1,2,3], [1, 2])
