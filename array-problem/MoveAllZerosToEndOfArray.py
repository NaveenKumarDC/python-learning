def pushZerorsToEnd(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        if(arr[i] != 0) :
            #Swap the current elemnent with 0 at index 'count'
            arr[i], arr[count] = arr[count], arr[i]
            count += 1
    return arr

if __name__ == "__main__":
    arr = [1, 2, 0, 0, 5, 6, 7, 8, 9, 10]
    arr =(pushZerorsToEnd(arr))
    print(arr)