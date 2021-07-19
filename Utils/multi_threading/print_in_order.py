import threading


class Foo:
    def __init__(self):
        self.s1 = threading.Semaphore(0)
        self.s2 = threading.Semaphore(0)

    def first(self, printFirst: "Callable[[], None]") -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.s1.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        # printSecond() outputs "second". Do not change or remove this line.
        self.s1.acquire()
        printSecond()
        self.s2.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        # printThird() outputs "third". Do not change or remove this line.
        self.s2.acquire()
        printThird()


def printFirst():
    print("first")


def printSecond():
    print("second")


def printThird():
    print("third")


if __name__ == "__main__":
    nums = [2, 1, 3]
    f = Foo()

    for num in nums:
        if num == 1:
            t = threading.Thread(target=f.first, args=(printFirst, ))
            t.start()

        elif num == 2:
            t = threading.Thread(target=f.second, args=(printSecond, ))
            t.start()

        elif num == 3:
            t = threading.Thread(target=f.third, args=(printThird, ))
            t.start()

        else:
            break
