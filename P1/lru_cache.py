"""
Explanation:

LRUCache uses a dict to store key and values, because dict has constant time get and set.

A queue is used to handle eviction of the least recently used keys. Whenever a key is set or get, it is pushed to the
very last of the queue, that makes the least recently keys move to the first spots and get evicted when capacity
is reached.

All operations are constant time:

Dict set, get and delete = O(1)
Stack push and pop = O(1)

Space complexity is O(k) where k is capacity of cache
"""
class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size() == 0:
            return None
        else:
            return self.items.pop()


class Queue:
    def __init__(self):
        self.stack = Stack()

    def size(self):
        return self.stack.size()

    def enqueue(self, item):
        self.stack.push(item)

    def dequeue(self):
        temp_stack = Stack()

        while self.size() > 1:
            item = self.stack.pop()
            temp_stack.push(item)

        value = self.stack.pop()

        while temp_stack.size() > 0:
            self.enqueue(temp_stack.pop())

        return value


class LRUCache:
    def __init__(self, capacity):
        if type(capacity) != int or capacity <= 0:
            raise ValueError('Invalid capacity given.')

        self.capacity = capacity
        self._cache = dict()
        self._eviction_queue = Queue()

    def size(self):
        return self._eviction_queue.size()

    def get(self, key):
        value = self._cache.get(key, -1)

        if value != -1:
            # record this key as the most recently accessed
            # i.e; put it at the end of the eviction queue
            temp_queue = Queue()

            while self._eviction_queue.size() > 0:
                key_ = self._eviction_queue.dequeue()

                if key_ != key:
                    temp_queue.enqueue(key_)

            temp_queue.enqueue(key)
            self._eviction_queue = temp_queue

        return value

    def set(self, key, value):
        if self.size() == self.capacity:
            key_to_evict = self._eviction_queue.dequeue()
            del self._cache[key_to_evict]

        self._eviction_queue.enqueue(key)
        self._cache[key] = value



if __name__ == "__main__":

    def test_case1():
        cache = LRUCache(5)
        cache.set(1, 1)
        cache.set(2, 2)
        cache.set(3, 3)
        cache.set(4, 4)

        assert cache.get(1) == 1
        assert cache.get(3) == 3
        assert cache.get(9) == -1

    def test_case2():
        cache = LRUCache(3)

        cache.set(1, 1)
        cache.set(2, 2)
        cache.set(3, 3)

        assert cache.get(1) == 1
        assert cache.get(3) == 3

        cache.set(4, 4)
        assert cache.get(2) == -1

    def test_case3():
        cache = LRUCache(2)

        cache.set(1, 1)
        cache.set(2, 2)
        cache.set(3, 3)

        assert cache.get(1) == -1
        assert cache.get(2) == 2

    def test_case4():
        try:
            cache = LRUCache(-5)
        except ValueError:
            assert True
        else:
            raise AssertionError

    def test_case5():
        try:
            cache = LRUCache('')
        except ValueError:
            assert True
        else:
            raise AssertionError


    for i, test in enumerate([
        test_case1, test_case2, test_case3, test_case4, test_case5
    ]):
        try:
            test()
            print(f'Test {i+1}: Passed')
        except AssertionError:
            print(f'Test {i+1}: Failed')
