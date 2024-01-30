from random import randint


class Sort:
    lst = None

    @staticmethod
    def bubble_sort(lst, inplace=False):
        """Bubble sort (сортировка пузырьком), complexity: O(n^2)"""
        if inplace is False:
            lst = lst.copy()

        for i in range(len(lst)):
            j = i
            while j > 0 and lst[j] < lst[j-1]:
                lst[j], lst[j-1] = lst[j-1], lst[j]
                j -= 1
        return lst

    @classmethod
    def merge_sort(cls, lst, inplace=False):
        """Merge sort (сортировка слиянием), complexity: O(n*log_n)"""
        return cls.__merge_sort(lst.copy() if not inplace else lst)

    @classmethod
    def __merge_sort(cls, lst):
        """Service method for merge_sort"""
        n = len(lst)
        if n <= 1:
            return lst

        return cls.__merge(cls.__merge_sort(lst[:n//2]), cls.__merge_sort(lst[n//2:]))

    @classmethod
    def __merge(cls, lst1, lst2):
        """Service method for __merge_sort"""
        max1, max2 = len(lst1)-1, len(lst2)-1
        i, j = 0, 0
        res = []
        while i <= max1 and j <= max2:
            if lst1[i] < lst2[j]:
                res.append(lst1[i])
                i += 1
            else:
                res.append(lst2[j])
                j += 1
        res += lst1[i:max1+1] if i <= max1 else lst2[j:max2+1]
        return res

    @classmethod
    def lomuto_sort(cls, lst, inplace=True):
        """Memory-inplace, E(T(n)) = O(n*log_n), but in worst case (sorted array) it will be O(n^2)"""
        cls.lst = lst.copy() if not inplace else lst
        cls.__sort(0, len(lst)-1)
        lst = cls.lst
        cls.lst = None
        return lst

    @classmethod
    def __sort(cls, l, r):
        """Service method for lomuto_sort"""
        if l >= r:
            return

        m = cls.__split(l, r)
        cls.__sort(l, m-1)
        cls.__sort(m+1, r)

    @classmethod
    def __split(cls, l, r):
        """Service method for __sort"""
        ind = randint(l, r)
        cls.lst[l], cls.lst[ind] = cls.lst[ind], cls.lst[l]

        m = l
        for i in range(l+1, r+1):
            if cls.lst[i] < cls.lst[l]:
                m += 1
                cls.lst[i], cls.lst[m] = cls.lst[m], cls.lst[i]

        cls.lst[l], cls.lst[m] = cls.lst[m], cls.lst[l]
        return m

    @classmethod
    def lazy_quick_sort(cls, lst):
        """Complexity: O(n*log_n), but memory-complexity also O(n*log_n)"""
        if len(lst):
            pivot = lst[randint(0, len(lst)-1)]
            left = [x for x in lst if x < pivot]
            eq = [x for x in lst if x == pivot]
            right = [x for x in lst if x > pivot]
            return cls.lazy_quick_sort(left) + eq + cls.lazy_quick_sort(right)
        return lst


if __name__ == '__main__':
    iterations_count = 100
    array_count = 10000

    for i in range(1, iterations_count+1):
        if i % 10 == 0:
            print(f"Iteration #{i}")
        lst = [randint(-10*array_count, 10*array_count) for _ in range(array_count)]
        assert sorted(lst) == Sort.lomuto_sort(lst, inplace=False)
        assert sorted(lst) == Sort.merge_sort(lst, inplace=False)

    print("\nTests passed!")
