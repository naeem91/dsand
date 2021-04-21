"""
Explanation:

We're visiting nodes of linked lists and creating sets of their values, then doing
union and intersection operations on those sets.


For performing either union or intersection, both linked lists have to be traversed:

list traversal => O(len(L1)+len(L2))
union => O(len(L1)+len(L2))
intersection => O(min(len(L1), len(L2))
creating output => O(len(k))  where k = len of union set

time complexity is of the linear order of input = O(n)

space complexity is also linear = O(n)
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def __iter__(self):
        head = self.head
        while head:
            yield head
            head = head.next

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1, llist_2):
    list_1_items = set()
    list_2_items = set()

    for node in llist_1:
        list_1_items.add(node.value)

    for node in llist_2:
        list_2_items.add(node.value)

    union_items = list_1_items | list_2_items

    union_list = LinkedList()

    for item in union_items:
        union_list.append(item)

    return union_list


def intersection(llist_1, llist_2):
    list_1_items = set()
    list_2_items = set()

    for node in llist_1:
        list_1_items.add(node.value)

    for node in llist_2:
        list_2_items.add(node.value)

    common_items = list_1_items & list_2_items

    intersect_list = LinkedList()

    for item in common_items:
        intersect_list.append(item)

    return intersect_list


if __name__ == "__main__":
    def _create_linked_list(list_):
        linked_list = LinkedList()

        for i in list_:
            linked_list.append(i)

        return linked_list

    def test_case1():
        element_1 = [3, 4]
        element_2 = [1, 2]

        linked_list_1 = _create_linked_list(element_1)
        linked_list_2 = _create_linked_list(element_2)

        # assert we're getting LinkedLists
        assert type(union(linked_list_1, linked_list_2)) == LinkedList
        assert type(intersection(linked_list_1, linked_list_2)) == LinkedList

    def test_case2():
        element_1 = [1, 2, 5]
        element_2 = [3, 5, 7, 9]

        linked_list_1 = _create_linked_list(element_1)
        linked_list_2 = _create_linked_list(element_2)

        expected_union = set(element_1) | set(element_2)
        expected_intersection = set(element_1) & set(element_2)

        u_output = {item.value for item in union(linked_list_1, linked_list_2)}
        i_output = {item.value for item in intersection(linked_list_1, linked_list_2)}

        assert u_output == expected_union
        assert i_output == expected_intersection

    def test_case3():
        element_1 = []
        element_2 = [1, 2]

        linked_list_1 = _create_linked_list(element_1)
        linked_list_2 = _create_linked_list(element_2)

        expected_union_set = set(element_1) | set(element_2)
        expected_intersection_set = set(element_1) & set(element_2)

        u_output = {item.value for item in union(linked_list_1, linked_list_2)}
        i_output = {item.value for item in intersection(linked_list_1, linked_list_2)}

        assert u_output == expected_union_set
        assert i_output == expected_intersection_set

    def test_case4():
        element_1 = []
        element_2 = []

        linked_list_1 = _create_linked_list(element_1)
        linked_list_2 = _create_linked_list(element_2)

        expected_union_set = set(element_1) | set(element_2)
        expected_intersection_set = set(element_1) & set(element_2)

        u_output = {item.value for item in union(linked_list_1, linked_list_2)}
        i_output = {item.value for item in intersection(linked_list_1, linked_list_2)}

        assert u_output == expected_union_set
        assert i_output == expected_intersection_set

    for i, test in enumerate([test_case1, test_case2, test_case3, test_case4]):
        try:
            test()
            print(f'Test {i+1}: Passed')
        except AssertionError:
            print(f'Test {i+1}: Failed')
