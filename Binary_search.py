# 二分查找算法

def search(list, item):
    # 开始索引
    startPos = 0
    # 结束索引
    endPos = len(list) - 1
    # 只要开始索引不大于结束索引 就继续查找
    while startPos <= endPos:
        # 取查找范围的中间索引 注:在python2.x中 整数/整数得到的还是整数,会自动舍弃掉小数位 但3.x中会变为float值 可以使用//来得到整数结果
        mid = (startPos + endPos) // 2
        # 获得中间值
        guess = list[mid]
        # 判断中间值是否是我们所查找的值
        if guess == item:
            return mid
        # 如果中间值大于结果值 说明我们需要的值在前半段 则把结束索引变为中间索引-1
        if guess > item:
            endPos = mid - 1
        # 否则说明我们需要的值在后半段 则把开始索引变为中间索引+1
        else:
            startPos = mid + 1
    # 没有查到结果
    else:
        return None


my_list = [1, 2, 3, 4, 5, 6, 7, 8]

print(search(my_list, 8))
