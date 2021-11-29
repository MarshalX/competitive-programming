class BitMask:
    def __init__(self, n: int):
        self.__value = n

    def __str__(self) -> str:
        subset = []

        for i in range(10):
            if self.find(i):
                subset.append(i)

        return f'<BitMask>{{{self.__value=}, {subset=}}}'

    @classmethod
    def create(cls, seq: list[int]):
        value = 0
        for i in seq:
            value = value ^ (1 << i)

        return cls(value)

    def find(self, v: int):
        return self.__value & (1 << v)

    def add(self, v: int):
        if not self.find(v):
            self.__value = self.__value ^ (1 << v)

    def remove(self, v: int):
        if self.find(v):
            self.__value = self.__value ^ (1 << v)


if __name__ == '__main__':
    for n in range(63 + 1):
        print(n, bin(n))

    print(BitMask.create([1, 3, 5, 7]))

    bm = BitMask(30)
    print(bm)

    bm.add(5)
    print(bm)

    bm.remove(3)
    bm.remove(3)
    print(bm)
