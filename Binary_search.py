def search(list, item):
    startPos = 0
    endPos = len(list) - 1

    while startPos <= endPos:
        #在python2.x中 整数/整数得到的还是整数,会自动舍弃掉小数位 但3.x中会变为float值 可以使用//来得到整数结果
        mid = (startPos + endPos) // 2

        guess = list[mid]

        if guess == item:
            return mid
        if guess > item:
            endPos = mid - 1
        else:
            startPos = mid + 1

    else:
        return None


my_list = [1, 2, 3, 4, 5, 6, 7, 8]

print(search(my_list, 8))
