class QuickSorter:
    num = 0

    def sort_first_pivot(self, array, left, right):
        if right <= left:
            return
        self.num += right - left
        p = array[left]
        i = left + 1
        for j in range(left + 1, right + 1):
            if array[j] < p:
                array[i], array[j] = array[j], array[i]
                i = i + 1
        array[left], array[i - 1] = array[i - 1], array[left]
        self.sort_first_pivot(array, i, right)
        self.sort_first_pivot(array, left, i - 2)

    def sort_last_pivot(self, array, left, right):
        if right <= left:
            return
        self.num += right - left
        array[left], array[right] = array[right], array[left]
        p = array[left]
        i = left + 1
        for j in range(left + 1, right + 1):
            if array[j] < p:
                array[i], array[j] = array[j], array[i]
                i = i + 1
        array[left], array[i - 1] = array[i - 1], array[left]
        self.sort_last_pivot(array, i, right)
        self.sort_last_pivot(array, left, i - 2)

    def sort_median_pivot(self, array, left, right):
        if right <= left:
            return
        if right - left >= 2:
            middle = (right - left) // 2 + left
            if ((array[middle] > array[left] and array[middle] < array[right])
                    or (array[middle] < array[left] and array[middle] > array[right])):
                array[left], array[middle] = array[middle], array[left]
            if ((array[left] > array[middle] and array[left] < array[right])
                    or (array[left] < array[middle] and array[left] > array[right])):
                pass
            if ((array[right] > array[left] and array[right] < array[middle])
                    or (array[right] < array[left] and array[right] > array[middle])):
                array[left], array[right] = array[right], array[left]
        self.num += right - left
        p = array[left]
        i = left + 1
        for j in range(left + 1, right + 1):
            if array[j] < p:
                array[i], array[j] = array[j], array[i]
                i = i + 1
        array[left], array[i - 1] = array[i - 1], array[left]
        self.sort_median_pivot(array, i, right)
        self.sort_median_pivot(array, left, i - 2)


# array = [5, 1, 6, 7, 9, 2, 3, 4, 8, 10]
file = open('unsorted.txt', 'r')
array = file.read().split()
array = list(map(int, array))

sorter = QuickSorter()
sorter.sort_median_pivot(array, 0, len(array) - 1)
# print(array)
print(sorter.num)

# 162085
# 164123
# 138984 , 139450- not correct
