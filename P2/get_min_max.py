

def n_chunks(arr, n):
    for i in range(0, len(arr), n):
        yield i, i + (n - 1)


def get_min_max(ints):
    if type(ints) != list or len(ints) == 0:
        raise ValueError('Provide a non-empty list')

    min_ = ints[0]
    max_ = ints[-1]

    # get max 3 items at a time and sort them
    for l, h in n_chunks(ints, 3):
        h = len(ints) - 1 if h >= len(ints) else h

        items_count = (h - l) + 1

        # place min at l and max at h
        if items_count >= 2:
            if ints[l] > ints[l+1]:
                ints[l], ints[l+1] = ints[l+1], ints[l]

        if items_count == 3:
            if ints[l+1] > ints[h]:
                ints[l+1], ints[h] = ints[h], ints[l+1]

        # consider only the min and max
        min_in_items = ints[l]
        max_in_items = ints[h]

        min_ = min_in_items if min_in_items < min_ else min_
        max_ = max_in_items if max_in_items > max_ else max_

    return min_, max_


if __name__ == "__main__":
    def test_case1():
        ints = [7,0,19,1,3,37,21,17]
        assert get_min_max(ints) == (min(ints), max(ints))

    def test_case2():
        ints = [-1, 0, 1, 1000]
        assert get_min_max(ints) == (min(ints), max(ints))

    def test_case3():
        ints = [0, 0, 0, 0, 0]
        assert get_min_max(ints) == (min(ints), max(ints))

    def test_case4():
        try:
            get_min_max([])
        except ValueError:
            assert True
        else:
            raise AssertionError

    def test_case5():
        try:
            get_min_max(None)
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
