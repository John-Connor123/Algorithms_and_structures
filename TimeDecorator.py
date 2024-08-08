from functools import wraps
from time import time

import matplotlib.pyplot as plt
import numpy as np


class TimeDecorator:
    @staticmethod
    def data_counter(verbose=False, parts_number=100):
        def set_func(func):
            @wraps(func)
            def wrapper(n):
                times = []
                to_print = -1
                for i in np.linspace(1, n, parts_number):
                    if verbose and i % (n // 10) <= (n // 100):
                        if to_print != round(100 * i / n):
                            print(f"{round(100 * i / n)}%")
                            to_print = round(100 * i / n)
                    times.append(func(round(i)))
                return np.linspace(1, n, parts_number).round(), times

            return wrapper

        return set_func

    @staticmethod
    def time_counter(number=10):
        def set_func(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                time_res = []
                for _ in range(number):
                    start = time()
                    func(*args, **kwargs)
                    time_res.append(time() - start)
                return sum(time_res) / len(time_res)

            return wrapper

        return set_func

    @staticmethod
    def plot(n, func1, func2=None, stats=True):
        plt.figure()
        print(f"Testing {func1.__name__}...")
        n_range, times = func1(n)
        plt.plot(n_range, times)
        if stats:
            print("Average time:", sum(times) / len(times))
            print("Total time", sum(times))

        if func2:
            print(f"\nTesting {func2.__name__}...")
            n_range, times = func2(n)
            plt.plot(n_range, times)
            if stats:
                print("Average time:", sum(times) / len(times))
                print("Total time", sum(times))
        plt.show()
