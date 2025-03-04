def majorityIIElements(arr):
    result = []
    n = len(arr)
    #Using Byoers-vooting algorithm
    count1 = 0
    count2 = 0
    ele1 = -1
    ele2 = -1
    for i in range(n):
        if ele1 == arr[i] :
            count1 += 1
        elif ele2 == arr[i] :
            count2 += 1
        elif count1 == 0:
            ele1 = arr[i]
            count1 += 1
        elif count2 == 0:
            ele2 = arr[i]
            count2 += 1
        else :
            count1 -= 1
            count2 -= 1

    count1 = count2 = 0
    for i in range(n):
        if arr[i] == ele1:
            count1 += 1
        elif arr[i] == ele2:
            count2 += 1

    #If the frequency is more than 3 then add element ele1 and ele2 to result list
    if count1 > n / 3:
        result.append(ele1)
    if count2 > n /3:
        result.append(ele2)

    #Swap the first with second element if first > second
    if (len(result) == 2 and result[0] > result[1]):
        temp = result[0]
        result.insert(0, result[1])
        result.insert(1, temp)

    return result

if __name__ == '__main__':
    arr = [1, 4, 3 ,4, 4,4, 3, 3,3]
    print(majorityIIElements(arr))