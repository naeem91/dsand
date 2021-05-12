import math

def _sqrt(number, first, last):

    mid = (first + last) // 2

    if mid <= 0:
        return number

    dividend = number // mid

    if dividend < mid:
        return _sqrt(number, first, last=mid)
    elif dividend > mid:
        return _sqrt(number, mid, last)
    else:
        return mid


def sqrt(number):
    if type(number) != int or number < 0:
        raise ValueError('Provide a positive integer value.')

    first = 0
    last = number

    return _sqrt(number, first, last)


if __name__ == "__main__":
    def test_case1():
        assert sqrt(25) == math.sqrt(25)

    def test_case2():
        assert sqrt(144) == math.sqrt(144)

    def test_case3():
        assert sqrt(0) == math.sqrt(0)

    def test_case4():
        try:
            sqrt(-1)
        except ValueError:
            assert True
        else:
            raise AssertionError

    def test_case5():
        try:
            sqrt('abc')
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
