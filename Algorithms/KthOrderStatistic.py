from Sort import Sort
from random import randint


class KthOrderStatistics:
    __lst = None
    __k = None

    @classmethod
    def k_order_statistics(cls, lst: list, k: int, randomized: bool = False):
        """
        Based on deterministic select (median of medians) algorithm by default. Sometimes it called BFPRT because of the last names of the authors.
        Using with randomized=True will choose random select (random pivot pick) algorithm.
        Complexity of both algorithms: O(n)
        """
        cls.__lst = lst.copy()
        cls.__k = k
        return cls.__randomised_k_order_statistics(0, len(cls.__lst)-1) if randomized \
            else cls.__determined_k_order_statistics(0, len(cls.__lst)-1, lst=cls.__lst)

    @classmethod
    def __randomised_k_order_statistics(cls, left, right):
        """Based on random pivot pick algorithm. Complexity: O(n)"""
        if left >= right:
            return cls.__lst[left]

        m = cls.__split(left, right)
        if cls.__k < m:
            return cls.__randomised_k_order_statistics(left, m-1)
        else:
            return cls.__randomised_k_order_statistics(m, right)

    @classmethod
    def __determined_k_order_statistics(cls, left, right, lst=None, k=None):
        """Based on median of medians algorithm. Sometimes called BFPRT because of the last names of the authors.
        Complexity: O(n)"""
        if k is None:
            k = cls.__k
        if lst is None:
            lst = cls.__lst
        print(f"Start_loop: left: {left}, right: {right}, lst: {lst}, k={k}")
        if k == 0:
            return lst[k]
        if left >= right:
            return lst[left]

        for i in range(0, len(lst), 5):
            lst[i:i+5] = Sort.quick_sort(lst[i:i+5])
        median_lst = lst[2:len(lst):5] if len(lst) > 2 else lst[0:1]
        print("Median size:", len(median_lst), ", median_lst:", median_lst, end='\n\n')

        pivot = cls.__determined_k_order_statistics(0, len(median_lst)-1, lst=median_lst, k=len(median_lst)//2)
        print("pivot:", pivot)


        m = cls.__split(left, right, pivot=pivot, lst=lst) - 1
        print(f"m={m}, k={k}, left={left}, right={right}")
        print(f'End_loop: left={left}, right={right}, m={m}, k={k}, pivot={pivot}, lst={lst}')
        if k < m:
            print(f"k({k}) < m({m})")
            return cls.__determined_k_order_statistics(left, m-1, k=k, lst=lst)
        elif k == m:
            print(f"k({k})=m({m}), lst[k]={lst[k]}, pivot={pivot}")
            return pivot
        else:
            print(f"k({k}) >= m({m})")
            return cls.__determined_k_order_statistics(m, right, k=k, lst=lst)

    @classmethod
    def __split(cls, left, right, pivot=None, lst=None):
        """Service method for k_order_statistics"""
        if lst is None:
            lst = cls.__lst
        if pivot is None:
            pivot = lst[randint(left, right)]
        while left <= right:
            while lst[left] < pivot:
                left += 1
            while lst[right] > pivot:
                right -= 1

            if left <= right:
                lst[left], lst[right] = lst[right], lst[left]
                left += 1
                right -= 1
        return left


if __name__ == '__main__':
    # print("Description of method k_order_statistics: ", KthOrderStatistics.k_order_statistics.__doc__)
    iterations_count = 100
    array_count = 10000

    for i in range(1, iterations_count+1):
        if i % 10 == 0:
            print(f"Iteration {i}/{iterations_count}")
        lst = [randint(-2*array_count, 2*array_count) for _ in range(array_count)]
        k = randint(0, array_count-1)

        lst1 = KthOrderStatistics.k_order_statistics(lst, k)
        print(f"k = {k}", lst1, sorted(lst)[k])
        assert sorted(lst)[k] == lst1
        assert sorted(lst)[k] == KthOrderStatistics.k_order_statistics(lst, k, randomized=True)

    print("\nTests passed!")
