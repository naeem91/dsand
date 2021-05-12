

def sort_012(input_list):
    if type(input_list) != list or len(input_list) == 0:
        raise ValueError('Provide a non-empty list')

    # divide the list into three buckets
    bucket_size = (len(input_list) - 1) // 3
    bucket_size = 1 if bucket_size <= 0 else bucket_size

    # buckets starting indexes
    bucket_0 = 0
    bucket_1 = bucket_0 + bucket_size
    bucket_2 = bucket_1 + bucket_size

    # process bucket_0
    head = bucket_0
    while head < bucket_1:
        item = input_list[head]

        if item == 1:
            # swap with the item just before bucket_1 and extend bucket_1
            input_list[head], input_list[bucket_1 - 1] = input_list[bucket_1 -1], input_list[head]
            bucket_1 -= 1
        elif item == 2:
            # swap with the item just before bucket_2 and extend bucket_2
            input_list[head], input_list[bucket_2 - 1] = input_list[bucket_2 - 1], input_list[head]
            bucket_2 -= 1
        else:
            head += 1

    # process bucket_1
    head = bucket_1
    while head < bucket_2:
        item = input_list[head]

        if item == 0:
            # swap with the item at the start of bucket_1 and extend bucket_0
            input_list[head], input_list[bucket_1] = input_list[bucket_1], input_list[head]
            if head == bucket_1:
                head += 1
            bucket_1 += 1
        elif item == 2:
            # swap with the item just before bucket_2 and extend bucket_2
            input_list[head], input_list[bucket_2 - 1] = input_list[bucket_2 - 1], input_list[head]
            bucket_2 -= 1
        else:
            head += 1

    # process bucket_2
    head = bucket_2
    while head < len(input_list):
        item = input_list[head]

        if item == 0:
            # swap with the item at the start of bucket_1 and extend bucket_0
            input_list[head], input_list[bucket_1] = input_list[bucket_1], input_list[head]
            if head == bucket_1:
                head += 1

            if bucket_1 == bucket_2:
                bucket_2 += 1
            bucket_1 += 1
        elif item == 1:
            # swap with the item at the start of bucket_2 and extend bucket_1
            input_list[head], input_list[bucket_2] = input_list[bucket_2], input_list[head]
            if head == bucket_2:
                head += 1
            bucket_2 += 1
        else:
            head += 1

    return input_list


if __name__ == "__main__":
    def test_case1():
        assert sort_012([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]) == \
               sorted([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])

    def test_case2():
        assert sort_012([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]) == \
               sorted([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

    def test_case3():
            assert sort_012([2, 0, 1, 2]) == \
                   sorted([2, 0, 1, 2])

    def test_case4():
        try:
            sort_012([])
        except ValueError:
            assert True
        else:
            raise AssertionError

    def test_case5():
        try:
            sort_012(None)
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

