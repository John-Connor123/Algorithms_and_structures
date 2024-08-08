from Sort import Sort

from TimeDecorator import TimeDecorator


class Divisors:
    @staticmethod
    @TimeDecorator.data_counter(verbose=True)
    @TimeDecorator.time_counter()
    def fast_divisors(n):
        lst = []
        i = 1
        while i**2 <= n:
            if n % i == 0:
                lst.append(i)
                if i**2 != n:
                    lst.append(int(n / i))
            i += 1
        return Sort.merge_sort(lst)

    @staticmethod
    @TimeDecorator.data_counter(verbose=True)
    @TimeDecorator.time_counter()
    def slow_divisors(n):
        lst = []
        for i in range(1, n):
            if n % i == 0:
                lst.append(i)
        return lst

    @staticmethod
    @TimeDecorator.data_counter(verbose=True, parts_number=1000)
    @TimeDecorator.time_counter(number=3)
    def slow_all_divisors(n):
        lst = []
        i = 2
        while i <= n:
            if n % i == 0:
                lst.append(i)
                n /= i
            else:
                i += 1
        return lst

    @staticmethod
    @TimeDecorator.data_counter(verbose=True, parts_number=1000)
    @TimeDecorator.time_counter(number=3)
    def fast_all_divisors(n):
        lst = []
        i = 2
        while i**2 <= n:
            if n % i == 0:
                lst.append(i)
                n /= i
            else:
                i += 1
        if n > 1:
            lst.append(round(n))
        return lst


if __name__ == "__main__":
    n = 10000000000
    # print(check_new_func(n, slow_all_divisors, fast_all_divisors))
    TimeDecorator.plot(n, Divisors.fast_all_divisors)
