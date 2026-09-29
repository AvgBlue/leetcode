import threading


class ZeroEvenOdd:
    def __init__(self, n: int):
        self.n = n
        self.zero_sem=threading.Semaphore(1)
        
        self.odd_sem=threading.Semaphore(2)
        self.even_sem=threading.Semaphore(0)
        

        

    def zero(self, printNumber) -> None:
        for _ in range(self.n):
            self.zero_sem.acquire()
            printNumber(0)
            self.odd_sem.release()
            self.even_sem.release()


            
    def odd(self, printNumber) -> None:
            for i in range(1,self.n+1,2):
                self.odd_sem.acquire()
                self.odd_sem.acquire()
                self.odd_sem.acquire()
                printNumber(i)
                self.zero_sem.release()
                self.even_sem.release()


    def even(self, printNumber) -> None:
        for i in range(2,self.n+1,2):
            self.even_sem.acquire()
            self.even_sem.acquire()
            self.even_sem.acquire()
            printNumber(i)
            self.zero_sem.release()
            self.odd_sem.release()




    


def run_test(n: int):
    obj = ZeroEvenOdd(n)
    output = []

    def printNumber(x):
        output.append(x)

    t_zero = threading.Thread(target=obj.zero, args=(printNumber,))
    t_even = threading.Thread(target=obj.even, args=(printNumber,))
    t_odd = threading.Thread(target=obj.odd, args=(printNumber,))

    # Start them in a deliberately mixed order
    t_even.start()
    t_odd.start()
    t_zero.start()

    t_zero.join()
    t_even.join()
    t_odd.join()

    expected = []
    for i in range(1, n + 1):
        expected.append(0)
        expected.append(i)

    print(f"n = {n}")
    print("result:  ", output)
    print("expected:", expected)

    assert output == expected
    print("Passed\n")


def main():
    run_test(1)
    run_test(2)
    run_test(5)
    run_test(10)

    print("All tests passed!")


if __name__ == "__main__":
    main()