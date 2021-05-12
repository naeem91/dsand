
def _search_item(l, t, lower, upper):
    if lower > upper:
        return -1

    center = (lower + upper) // 2
    if l[center] < t:
        lower = center + 1
    elif l[center] > t:
        upper = center - 1
    else:
        return center

    return _search_item(l, t, lower, upper)


def _find_pivot(arr, lower, upper):
    """
    pivot is the index where array is rotated
    i.e; it is the greatest value in the array
    """
    if arr[lower] < arr[upper]:
        lower = upper
        upper = len(arr) - 1
        return _find_pivot(arr, lower, upper)
    elif arr[lower] > arr[upper]:
        upper = (lower + upper) // 2
        return _find_pivot(arr, lower, upper)
    else:
        return lower


def rotated_array_search(arr, number):
    if type(arr) != list or type(number) != int or len(arr) == 0:
        raise ValueError('Invalid values for list and number')

    pivot = _find_pivot(arr, lower=0, upper=len(arr) - 1)

    if number == arr[pivot]:
        return pivot
    elif number < arr[pivot]:
        # either search in left or right side of pivot
        if number < arr[0]:
            return _search_item(arr, number, lower=pivot + 1, upper=len(arr) - 1)
        else:
            return _search_item(arr, number, lower=0, upper=pivot - 1)
    else:
        return -1


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


if __name__ == "__main__":
    def test_case1():
        assert rotated_array_search([5,6,7,8,2,3,4], 6) == linear_search([5,6,7,8,2,3,4], 6)

    def test_case2():
        assert rotated_array_search([5,6,7,8,9,10,0], 0) == linear_search([5,6,7,8,9,10,0], 0)

    def test_case3():
        assert rotated_array_search([5,6,7,8,9,10,0,1,2], 1) == linear_search([5,6,7,8,9,10,0,1,2], 1)

    def test_case4():
        try:
            rotated_array_search(None, None)
        except ValueError:
            assert True
        else:
            raise AssertionError

    def test_case5():
        try:
            rotated_array_search([], 30)
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
