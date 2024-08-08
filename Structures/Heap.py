class Heap:
    def __init__(self, lst=None, make_copy=False):
        if lst is None:
            self.__lst = []
        else:
            self.__lst = lst.copy() if make_copy else lst
            for i in range(len(self) - 1, -1, -1):
                self.__sift_down(i)

    @classmethod
    def heap_sort(cls, lst, inplace=True):
        """O(n)"""
        obj = cls(lst, make_copy=not inplace)
        to_return = []
        for _ in range(len(lst)):
            to_return.append(obj.remove_min())
        return to_return

    def get_min(self):
        """O(1)"""
        if len(self):
            return self.__lst[0]

    def insert(self, value):
        """O(log_n)"""
        self.__lst.append(value)
        self.__sift_up(len(self) - 1)  # O(log_n)

    def remove_min(self):
        """O(log_n)"""
        self.__lst[len(self) - 1], self.__lst[0] = (
            self.__lst[0],
            self.__lst[len(self) - 1],
        )
        to_return = self.__lst.pop()
        self.__sift_down()  # O(log_n)
        return to_return

    def __sift_up(self, i):
        """Просеивание вверх"""
        while i and self.__lst[i] < self.__lst[(i - 1) // 2]:
            self.__lst[i], self.__lst[(i - 1) // 2] = (
                self.__lst[(i - 1) // 2],
                self.__lst[i],
            )
            i = (i - 1) // 2

    def __sift_down(self, i=0):
        """Просеивание вниз"""
        while 2 * i + 1 < len(self):
            index_min_child = 2 * i + 1
            if 2 * i + 2 < len(self) and self.__lst[2 * i + 2] < self.__lst[2 * i + 1]:
                index_min_child = 2 * i + 2

            if self.__lst[i] > self.__lst[index_min_child]:
                self.__lst[i], self.__lst[index_min_child] = (
                    self.__lst[index_min_child],
                    self.__lst[i],
                )
                i = index_min_child
            else:
                break

    @property
    def lst(self):
        return self.__lst

    def __len__(self):
        return len(self.lst)

    def __eq__(self, other):
        return self.lst == other.lst

    def __hash__(self):
        return hash(tuple(self.__lst))


if __name__ == "__main__":
    from random import randint

    n = 10000

    lst = [randint(-2 * n, 2 * n) for i in range(n)]
    assert Heap.heap_sort(lst, inplace=False) == sorted(lst)

    heap = Heap()
    for _ in range(n):
        heap.insert(lst)
    print(f"Inserted {n} elements. Size of heap:", len(heap))

    for _ in range(n):
        heap.remove_min()
    print(f"Removed {n} elements. Size of heap:", len(heap))

    d = {}
    l1 = Heap(lst)
    l2 = Heap(lst.copy())
    assert hash(l1) == hash(l2)

    d[l1] = 1
    d[l2] = 2
    assert d == {l1: 2}
