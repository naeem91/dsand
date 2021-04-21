"""
The search goes by DFS, all the files with suffix are added into a list.

visiting paths = O(n)
checking if a file path ends with suffix = O(1)

overall it is proportional to no. of paths = O(n)
"""

import os


def find_files(suffix, path):
    if os.path.isfile(path):
        if path.endswith(suffix):
            return [path]
        else:
            return []

    files_with_suffix = list()

    for p in os.listdir(path):
        file_with_suffix = find_files(suffix, os.path.join(path, p))
        files_with_suffix.extend(file_with_suffix)

    return files_with_suffix


if __name__ == "__main__":

    def test_case1():
        expected = ['./testdir/subdir3/subsubdir1/b.h', './testdir/subdir5/a.h', './testdir/t1.h', './testdir/subdir1/a.h']
        assert find_files('.h', '.') == expected

    def test_case2():
        expected = ['./testdir/subdir4/.gitkeep', './testdir/subdir2/.gitkeep']
        assert find_files('.gitkeep', '.') == expected

    def test_case3():
        expected = ['./testdir/subdir3/subsubdir1/b.c', './testdir/t1.c', './testdir/subdir5/a.c', './testdir/subdir1/a.c']
        assert find_files('.c', '.') == expected

    for i, test in enumerate([test_case1, test_case2, test_case3]):
        try:
            test()
            print(f'Test {i+1}: Passed')
        except AssertionError:
            print(f'Test {i+1}: Failed')