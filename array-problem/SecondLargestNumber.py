

def secondLarget(arr):
    n = len(arr)

    largest = -1
    secondLarget = -1

    for i in range(n):
        if arr[i] > largest:
            secondLarget = largest
            largest = arr[i]

        elif arr[i] > secondLarget and arr[i] < largest:
            secondLarget = arr[i]
    return secondLarget

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(secondLarget(arr))