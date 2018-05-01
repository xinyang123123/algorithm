# 快速排序 
def quick_sort(array):
    # 基线条件(跳出递归条件)
    if len(array) < 2:
        return array
    else:
        # 指定基准值
        pivot = array[0]

        # 取出比基准值小的部分
        less = [i for i in array[1:] if i <= pivot]

        # 取出大于基准值的部分
        greater = [i for i in array[1:] if i > pivot]

        return quick_sort(less) + [pivot] + quick_sort(greater)


print(quick_sort([1, 8, 9, 5, 7, 4, 3, 2, 6]))

# 快速排序使用分治法思想 把数据通过指定的基准值分割为两部分 其中一部分值必然小于另一部分 然后再按此方法对这两部分分别进行快速排序 整个过程可以递归进行
# 分治法:
    # 1.找到简单的基线条件
    # 2.确定如何缩小问题的规模,使其符合基线条件
# 时间复杂度:取决于基准值...
    # 最优 O(n log n)
    # 最差 O(n²)
