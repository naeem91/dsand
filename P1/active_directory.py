"""
Explanation:

Two strategies are used to speed up user group membership look up:

1. A group's users are kept in a set rather than in a list to make lookup time constant
2. A persistent caching can be used to store list of a user's groups. This cache can be built
when doing lookups:

for example in following hierarchy:

Parent
  |
Child
  |
sub-child

if a user is found in sub-child, all of the parents will be added to user member groups, if not every group will
be added to user not-member list. So on next lookup, membership will be determined even at the top level parent group
by consulting the cache.

The downside of this solution is cache invalidation will become an issue, groups cache of a user can be invalidated
when a user's membership is changed.

Complexity:

lookup in users set is constant = O(1)
visiting each sub group is = O(n)

overall the time complexity is proportional to total number of sub-groups to search = O(n)
"""

try:
    # a persistent cache
    # pip install diskcache
    from diskcache import Cache
    cache = Cache(directory='.')
except ImportError:
    cache = dict()


class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = set()

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.add(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


class UserGroupsCache:
    """
    maintains a cache of user groups
    """
    def __init__(self, user_id):
        self.user_id = user_id

    def add_to_user_groups(self, group, is_member):
        groups = cache[self.user_id]
        if is_member:
            groups['member'].add(group.name)
        else:
            groups['not_member'].add(group.name)

        cache[self.user_id] = groups

    def is_member(self, group):
        if self.user_id not in cache:
            cache[self.user_id] = {'member': set(), 'not_member': set()}

        groups = cache[self.user_id]

        if group.name in groups['member']:
            return True
        elif group.name in groups['not_member']:
            return False
        else:
            return None


def is_user_in_group(user, group):
    if not all([user, group]) or not str in [type(user), type(group)]:
        raise ValueError('Invalid user or group input.')

    is_member = False

    # lookup in cache first
    if UserGroupsCache(user).is_member(group) is not None:
        return UserGroupsCache(user).is_member(group)

    # lookup in group users
    if user in group.get_users():
        is_member = True
    else:
        # lookup in sub-groups
        for _group in group.get_groups():
            result = is_user_in_group(user, _group)

            if result:
                UserGroupsCache(user).add_to_user_groups(_group, True)
                is_member = True
                break

    # store membership in cache
    UserGroupsCache(user).add_to_user_groups(group, is_member)

    return is_member


if __name__ == "__main__":

    def test_case1():
        parent = Group("parent")
        child = Group("child")
        sub_child = Group("subchild")

        sub_child_user = "sub_child_user"
        sub_child.add_user(sub_child_user)

        child.add_group(sub_child)
        parent.add_group(child)

        assert is_user_in_group(sub_child_user, parent) == True
        assert is_user_in_group(sub_child_user, child) == True
        assert is_user_in_group('non_existent', parent) == False

    def test_case2():
        parent = Group("parent")

        try:
            is_user_in_group('', parent)
        except ValueError:
            assert True
        else:
            raise AssertionError

    def test_case3():
        parent = Group("parent")

        try:
            is_user_in_group('', '')
        except ValueError:
            assert True
        else:
            raise AssertionError

    for i, test in enumerate([test_case1, test_case2, test_case3]):
        try:
            test()
            print(f'Test {i+1}: Passed')
        except AssertionError:
            print(f'Test {i+1}: Failed')
