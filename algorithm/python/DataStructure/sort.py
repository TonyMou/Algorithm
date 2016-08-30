# -*- coding:utf-8 -*-
###############################################
# 冒泡排序
# 1. 比较相邻的元素。如果第一个比第二个大，就交换位置；
# 2. 对每一对相邻元素作同样的操作，从开始第一对到结尾的最后一对。这步就做完后，最后的元素会是最大的数；
# 3. 针对所有的元素重复以上的步骤，除了最后一个；
# 4. 持续每次对越来越少的元素重复上述的操作，直到没有任何一对数字需要比较。


def bubble_sort(list):
    length = len(list)
    for index in range(length):
        flag = True
        for j in range(1, length - index):
            if list[j - 1] > list[j]:
                list[j - 1], list[j] = list[j], list[j - 1]
                flag = False
        if flag:
            return list
    return list


#######################################
# 选择排序
# 1. 在未排序序列中找到最小（大）的元素，存放到排序列表的起始位置；
# 2. 再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾；
# 3. 重复第二步，直到所有元素均排序完毕


def selection_sort(list):
    n = len(list)
    for i in range(n - 1):
        min = i
        for j in range(i + 1, n):
            if list[j] < list[min]:
                min = j
        if min != i:
            list[min], list[i] = list[i], list[min]
    return list


#################################
# 插入排序
# 1. 从第一个元素开始，该元素可以认为已经被排序
# 2. 取出下一个元素，在已经排序的元素序列中从后向前扫描
# 3. 如果该元素（已排序）大于新元素，将该元素移到下一位置
# 4. 重复步骤3，直到找到已排序的元素小于或者等于新元素的位置
# 5. 将新元素插入到该位置
# 6. 重复步骤2~5


def insert_sort(list):
    n = len(list)
    for i in range(1, n):
        if list[i] < list[i - 1]:
            temp = list[i]
            index = i
            for j in range(i - 1, -1, -1):
                if list[j] > temp:
                    list[j + 1] = list[j]
                    index = j
                else:
                    break
            list[index] = temp
    return list


################################
# 希尔排序
# 每次以一定步长进行排序，直至步长为1


def shell_sort(list):
    n = len(list)
    gap = int(n / 2)
    while gap > 0:
        for i in range(int(gap), n):
            temp = list[i]
            j = i
            while j >= gap and list[int(j - gap)] > temp:
                list[j] = list[int(j - gap)]
                j -= gap
            list[int(j)] = temp
        gap = int(gap / 2)
    return list


#############################
# 归并排序
# 迭代法：
#       1. 申请空间，使其大小为两个已经排序序列之和，该空间用来存放合并后的序列
#       2. 设定两个指针，最初位置分别为两个已经排序序列的起始位置
#       3. 比较两个指针所指向的元素，选择相对小的元素放入到合并空间，并移动指针到下一位置
#       4. 重复步骤3直至某一指针到达序列尾
#       5. 将另一序列剩下的所有元素直接复制到合并序列尾
def merge(left, right):
    l, r = 0, 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
        result += left[l:]
        result += right[r:]
    return result


def merge_sort(list):
    if len(list) <= 1:
        return list
    middle = len(list) // 2
    left = merge_sort(list[:middle])
    right = merge_sort(list[middle:])
    return merge(left, right)


def sort_cls(list):
    n = len(list)
    if n <= 1:
        return list
    list.sort()
    last = list[-1]
    for i in range(n - 2, -1, -1):
        if last == list[i]:
            del list[i]
        else:
            last = list[i]
    return list
