import threading


class FooBar:
    def __init__(self, n: int):
        self.n = n
        self.foo_lock=threading.Lock()
        self.bar_lock=threading.Lock()
        self.bar_lock.acquire()

    def foo(self, printFoo) -> None:
        for _ in range(self.n):
            self.foo_lock.acquire()
            printFoo()
            self.bar_lock.release()



    def bar(self, printBar) -> None:
        for _ in range(self.n):
            self.bar_lock.acquire()
            printBar()
            self.foo_lock.release()


def run_test(n: int):
    foo_bar = FooBar(n)
    output = []

    def printFoo():
        output.append("foo")

    def printBar():
        output.append("bar")

    t1 = threading.Thread(target=foo_bar.foo, args=(printFoo,))
    t2 = threading.Thread(target=foo_bar.bar, args=(printBar,))

    # Start in this order
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    result = "".join(output)
    expected = "foobar" * n

    print(f"n = {n}")
    print(f"result:   {result}")
    print(f"expected: {expected}")

    assert result == expected
    print("Passed\n")


def main():
    run_test(1)
    run_test(2)
    run_test(5)
    run_test(10)

    print("All tests passed!")


if __name__ == "__main__":
    main()