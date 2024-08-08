from random import randint

from Algorithms.Sort import Sort


class KthOrderStatistics:
    __lst = None
    __k = None

    @classmethod
    def k_order_statistics(cls, lst: list, k: int, randomized: bool = True):
        """
        Based on random select (random pivot pick) algorithm by default.
        Using with randomized=False will choose deterministic select
        (median of medians) algorithm.
        Sometimes it called BFPRT because of the last names of the authors.
        Complexity of both algorithms: O(n).
        Memory-complexity of random select is O(n),
        but memory-complexity of deterministic select is O(n*log_n).
        """
        cls.__lst = lst.copy()
        cls.__k = k - 1
        return (
            cls.__randomised_k_order_statistics(0, len(cls.__lst) - 1)
            if randomized
            else cls.__determined_k_order_statistics(0, len(cls.__lst) - 1)
        )

    @classmethod
    def __randomised_k_order_statistics(cls, left, right):
        """Based on random pivot pick algorithm. Complexity: O(n)"""
        if left >= right:
            return cls.__lst[left]

        m = cls.__split(left, right)
        if cls.__k < m:
            return cls.__randomised_k_order_statistics(left, m - 1)
        elif cls.__k == m:
            return cls.__lst[m]
        else:
            return cls.__randomised_k_order_statistics(m + 1, right)

    @classmethod
    def __determined_k_order_statistics(cls, left, right, lst=None, k=None):
        """Based on median of medians algorithm.
        Sometimes called BFPRT because of the last names of the authors.
        Complexity: O(n)"""
        if k is None:
            k = cls.__k
        if lst is None:
            lst = cls.__lst
        if left >= right:
            return lst[left]

        m = cls.__split(left, right, pivot=cls.__pick_pivot(lst), lst=lst)
        if k < m:
            return cls.__determined_k_order_statistics(0, m - 1 - left, k=k, lst=lst[left:m])
        elif k == m:
            return lst[k]
        else:
            return cls.__determined_k_order_statistics(
                0, right - m - 1, k=k - m - 1, lst=lst[m + 1 : right + 1]
            )

    @classmethod
    def __pick_pivot(cls, lst):
        if len(lst) == 1:
            return lst[0]

        for i in range(0, len(lst), 5):
            lst[i : i + 5] = Sort.quick_sort(lst[i : i + 5])
        median_lst = (
            lst[2 : len(lst) : 5] if len(lst) >= 5 else [lst[randint(0, len(lst) - 1)]]
        )
        return cls.__pick_pivot(lst=median_lst)

    @classmethod
    def __split(cls, left, right, pivot=None, lst=None):
        """Service method for k_order_statistics"""
        if lst is None:
            lst = cls.__lst
        if pivot is None:
            pivot = lst[randint(left, right)]
        ind = lst.index(pivot)
        lst[left], lst[ind] = lst[ind], lst[left]

        m = left
        for i in range(left + 1, right + 1):
            if lst[i] <= lst[left]:
                m += 1
                lst[i], lst[m] = lst[m], lst[i]

        lst[left], lst[m] = lst[m], lst[left]
        return m


if __name__ == "__main__":
    print(
        "Description of method k_order_statistics: ",
        KthOrderStatistics.k_order_statistics.__doc__,
    )
    iterations_count = 100
    array_count = 10000

    for i in range(1, iterations_count + 1):
        if i % 10 == 0:
            print(f"Iteration {i}/{iterations_count}")
        lst = [randint(-3 * array_count, 3 * array_count) for _ in range(array_count)]
        k = randint(1, array_count)

        assert sorted(lst)[k - 1] == KthOrderStatistics.k_order_statistics(
            lst, k, randomized=True
        )
        assert sorted(lst)[k - 1] == KthOrderStatistics.k_order_statistics(
            lst, k, randomized=False
        )

    print("\nTests passed!")
