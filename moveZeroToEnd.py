def moveZeroestoEnd(arr1, n):
    count = 0

    for i in range(n):
        if(arr1[i] != 0):
            arr1[count] = arr1[i]
            count += 1

    while count < n:
        arr1[count] = 0
        count += 1

    print(arr1)


if __name__ == "__main__":

    arr = [1,2,3,4,0,0,0,3,0,9,0]
    n = len(arr)

    moveZeroestoEnd(arr, n)
