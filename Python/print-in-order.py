import threading
import time
import random


class Foo:
    def __init__(self):
        self.first_event=threading.Event()
        self.second_event=threading.Event()


    def first(self, printFirst) -> None:
        printFirst()
        self.first_event.set()


    def second(self, printSecond) -> None:
        self.first_event.wait()
        printSecond()
        self.second_event.set()

    def third(self, printThird) -> None:
        self.second_event.wait()
        printThird()



def run_test(order):
    foo = Foo()
    output = []

    def printFirst():
        output.append("first")

    def printSecond():
        output.append("second")

    def printThird():
        output.append("third")

    functions = {
        1: lambda: foo.first(printFirst),
        2: lambda: foo.second(printSecond),
        3: lambda: foo.third(printThird),
    }

    threads = [
        threading.Thread(target=functions[i])
        for i in order
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print(f"Start order: {order}")
    print(f"Output:      {output}")

    assert output == ["first", "second", "third"]
    print("Passed\n")


def main():
    # LeetCode-style permutations
    run_test([1, 2, 3])
    run_test([1, 3, 2])
    run_test([2, 1, 3])
    run_test([2, 3, 1])
    run_test([3, 1, 2])
    run_test([3, 2, 1])

    # Stress test with random thread start orders
    for _ in range(100):
        order = [1, 2, 3]
        random.shuffle(order)
        run_test(order)

    print("All tests passed!")


if __name__ == "__main__":
    main()