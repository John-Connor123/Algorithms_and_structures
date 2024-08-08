from random import randint


class Sort:
    __lst = None

    @staticmethod
    def bubble_sort(lst, inplace=False):
        """Bubble sort (сортировка пузырьком), complexity: O(n^2)"""
        if inplace is False:
            lst = lst.copy()

        for i in range(len(lst)):
            j = i
            while j > 0 and lst[j] < lst[j - 1]:
                lst[j], lst[j - 1] = lst[j - 1], lst[j]
                j -= 1
        return lst

    @staticmethod
    def choice_sort(lst, inplace=False):
        """Complexity: O(n^2)"""
        if inplace is False:
            lst = lst.copy()

        for i in range(len(lst)):
            j_min = i
            for j in range(i, len(lst)):
                if lst[j] < lst[j_min]:
                    j_min = j
            lst[i], lst[j_min] = lst[j_min], lst[i]
        return lst

    @staticmethod
    def insertion_sort(lst, inplace=False):
        """Complexity: O(n^2)"""
        if not inplace:
            lst = lst.copy()

        for i in range(len(lst)):
            ind_sorted_part = i - 1
            while ind_sorted_part >= 0 and lst[ind_sorted_part + 1] < lst[ind_sorted_part]:
                lst[ind_sorted_part + 1], lst[ind_sorted_part] = (
                    lst[ind_sorted_part],
                    lst[ind_sorted_part + 1],
                )
                ind_sorted_part -= 1

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

        return cls.__merge(cls.__merge_sort(lst[: n // 2]), cls.__merge_sort(lst[n // 2 :]))

    @classmethod
    def __merge(cls, lst1, lst2):
        """Service method for __merge_sort"""
        max1, max2 = len(lst1) - 1, len(lst2) - 1
        i, j = 0, 0
        res = []
        while i <= max1 and j <= max2:
            if lst1[i] < lst2[j]:
                res.append(lst1[i])
                i += 1
            else:
                res.append(lst2[j])
                j += 1
        res += lst1[i : max1 + 1] if i <= max1 else lst2[j : max2 + 1]
        return res

    @classmethod
    def lomuto_sort(cls, lst, inplace=False):
        """It's modification of quick sort. Memory-inplace, E(T(n)) = O(n*log_n)"""
        cls.__lst = lst.copy() if not inplace else lst
        cls.__lomuto_sort(0, len(lst) - 1)
        lst = cls.__lst
        cls.__lst = None
        if not inplace:
            return lst

    @classmethod
    def __lomuto_sort(cls, left, right):
        """Service method for lomuto_sort"""
        if left >= right:
            return

        m = cls.__lomuto_split(left, right)
        cls.__lomuto_sort(left, m - 1)
        cls.__lomuto_sort(m + 1, right)

    @classmethod
    def __lomuto_split(cls, left, right):
        """Service method for lomuto_sort"""
        ind = randint(left, right)
        cls.__lst[left], cls.__lst[ind] = cls.__lst[ind], cls.__lst[left]

        m = left
        for i in range(left + 1, right + 1):
            if cls.__lst[i] < cls.__lst[left]:
                m += 1
                cls.__lst[i], cls.__lst[m] = cls.__lst[m], cls.__lst[i]

        cls.__lst[left], cls.__lst[m] = cls.__lst[m], cls.__lst[left]
        return m

    @classmethod
    def lazy_quick_sort(cls, lst):
        """Complexity: O(n*log_n), but memory-complexity also O(n*log_n)"""
        if len(lst):
            pivot = lst[randint(0, len(lst) - 1)]
            left = [x for x in lst if x < pivot]
            eq = [x for x in lst if x == pivot]
            right = [x for x in lst if x > pivot]
            return cls.lazy_quick_sort(left) + eq + cls.lazy_quick_sort(right)
        return lst

    @classmethod
    def quick_sort(cls, lst, inplace=False):
        """Memory-inplace, E(T(n)) = O(n*log_n)"""
        cls.__lst = lst.copy() if not inplace else lst
        cls.__quick_sort(0, len(lst) - 1)
        lst = cls.__lst
        cls.__lst = None
        if not inplace:
            return lst

    @classmethod
    def __quick_sort(cls, left, right):
        """Service method for quick_sort"""
        if left >= right:
            return

        m = cls.__quick_split(left, right)
        cls.__quick_sort(left, m - 1)
        cls.__quick_sort(m, right)

    @classmethod
    def __quick_split(cls, left, right):
        """Service method for quick_sort"""
        pivot = cls.__lst[randint(left, right)]
        while left <= right:
            while cls.__lst[left] < pivot:
                left += 1
            while cls.__lst[right] > pivot:
                right -= 1

            if left <= right:
                cls.__lst[left], cls.__lst[right] = cls.__lst[right], cls.__lst[left]
                left += 1
                right -= 1
        return left


if __name__ == "__main__":
    iterations_count = 100
    array_count = 1000

    for i in range(1, iterations_count + 1):
        if i % 10 == 0:
            print(f"Iteration {i}/{iterations_count}")
        lst = [randint(-2 * array_count, 2 * array_count) for _ in range(array_count)]

        test_slow_algorithms = True
        if test_slow_algorithms:
            assert sorted(lst) == Sort.bubble_sort(lst)
            assert sorted(lst) == Sort.choice_sort(lst)
            assert sorted(lst) == Sort.insertion_sort(lst)

        assert sorted(lst) == Sort.merge_sort(lst)
        assert sorted(lst) == Sort.lomuto_sort(lst)
        assert sorted(lst) == Sort.lazy_quick_sort(lst)
        assert sorted(lst) == Sort.quick_sort(lst)

    print("\nTests passed!")
