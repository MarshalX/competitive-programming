import math
import random


class Heap:
    def __init__(self, store=None):
        self.__store = store or []
        self.__last_index = len(store) - 1 if store else -1

    def get_store(self):
        return self.__store

    # O(logN)
    def sift_up(self, index):
        # while its not a root and parent higher than current do swap
        while index > 0 and self.__store[index] < self.__store[(index - 1) // 2]:
            self.__store[index], self.__store[(index - 1) // 2] = self.__store[(index - 1) // 2], self.__store[index]
            index = (index - 1) // 2

    # O(logN)
    def sift_down(self, index):
        while True:
            min_idx = index     # cant use index because we should stay on the same layer (cant change index)
            for shift in range(1, 3):
                # if child is exists and is lower than the current node do swap
                if 2 * index + shift <= self.__last_index and self.__store[2 * index + shift] < self.__store[min_idx]:
                    min_idx = 2 * index + shift
            if min_idx == index:     # the current position is min already. so its right position of the node
                break
            self.__store[index], self.__store[min_idx] = self.__store[min_idx], self.__store[index]
            index = min_idx     # now we can move to more deep level

    def get_min(self) -> int:
        return self.__store[0]

    def remove_min(self):
        self.__store[0], self.__store[self.__last_index] = self.__store[self.__last_index], self.__store[0]
        self.__last_index -= 1
        self.sift_down(0)

    def get_min_and_remove(self):
        val = self.get_min()
        self.remove_min()
        return val

    def insert(self, n: int):
        self.__store.append(n)
        self.__last_index += 1
        self.sift_up(self.__last_index)

    def __str__(self):
        s = ['Heap:']
        for i in range(int(math.log2(self.__last_index + 1)) + 1):
            r = []
            for j in range(2 ** i - 1, 2 ** (i + 1) - 1):
                if j <= self.__last_index:
                    r.append(f'{self.__store[j]}')
                    if j % 2 == 0:
                        r.append('| ')
            if (r[len(r) - 1]) == '| ':
                r.pop(len(r) - 1)
            s.append(' '.join(r))

        return '\n'.join(s)


# with O(n) additional memory
def heap_sort1(arr: list[int]):
    h = Heap()
    for i in arr:   # O(NlogN)
        h.insert(i)

    print(h)

    return [h.get_min_and_remove() for _ in range(len(arr))]   # O(NlogN)


# without additional memory and init for O(n)
def heap_sort2(arr: list[int]):
    # we can use our input array as store for heap
    # and lets reuse our heap store to store sorted value after removing min
    # (when we are removing min we free 1 slot in the end of store)

    h = Heap(arr)
    # btw its O(n) but I cant proof it :(
    for i in range(len(arr) - 1, -1, -1):    # sifting from deep layers
        h.sift_down(i)

    # in this step we have valid heap with input array used as store
    print(h)

    s = h.get_store()

    # O(NlogN)
    for i in range(len(arr) - 1, -1, -1):
        s[i] = h.get_min_and_remove()   # by removing we are free i`s slot and can store our min value in it
    s.reverse()

    return s


if __name__ == '__main__':
    for f in [heap_sort1, heap_sort2]:
        print('Function name:', f.__name__)
        a = [random.randint(0, 100) for _ in range(30)]
        print('Before:', a)
        print('After:', f(a), '\n')
