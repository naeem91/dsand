def _heapify(arr, n, i):
    largest_index = i
    left_node = 2 * i + 1
    right_node = 2 * i + 2

    # compare with left child
    if left_node < n and arr[i] < arr[left_node]:
        largest_index = left_node

    # compare with right child
    if right_node < n and arr[largest_index] < arr[right_node]:
        largest_index = right_node

    # if either of left / right child is the largest node
    if largest_index != i:
        arr[i], arr[largest_index] = arr[largest_index], arr[i]

        _heapify(arr, n, largest_index)


def _convert_items_to_decimal(arr):
    """
    e.g; [9, 6, 4] -> 964
    """
    decimal = 0

    power_of_10 = 0
    for i in range(len(arr) - 1, -1, -1):
        decimal += pow(10, power_of_10) * arr[i]
        power_of_10 += 1

    return decimal

def rearrange_array_elements(arr):
    if type(arr) != list or len(arr) == 0:
        raise ValueError('Provide a non-empty list')

    n = len(arr)

    # Build a maxheap.
    for i in range(n, -1, -1):
        _heapify(arr, n, i)

    # extract max elements and place in two arrays alternatively
    num1 = []
    num2 = []

    num1.append(arr[0])
    place = 2

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        _heapify(arr, i, 0)

        if place == 1:
            num1.append(arr[0])
            place = 2
        else:
            num2.append(arr[0])
            place = 1

    # convert list of ints to a single decimal
    return [_convert_items_to_decimal(num1), _convert_items_to_decimal(num2)]

if __name__ == "__main__":
    def test_case1():
        assert sum(rearrange_array_elements([1, 2, 3, 4, 5])) == sum([542, 31])

    def test_case2():
        assert sum(rearrange_array_elements([4, 6, 2, 5, 9, 8])) == sum([964, 852])

    def test_case3():
        try:
            rearrange_array_elements([])
        except ValueError:
            assert True
        else:
            raise AssertionError

    def test_case4():
        try:
            rearrange_array_elements(None)
        except ValueError:
            assert True
        else:
            raise AssertionError

    for i, test in enumerate([
        test_case1, test_case2, test_case3, test_case4
    ]):
        try:
            test()
            print(f'Test {i+1}: Passed')
        except AssertionError:
            print(f'Test {i+1}: Failed')
