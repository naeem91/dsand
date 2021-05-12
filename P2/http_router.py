

class RouteTrieNode:
    def __init__(self, name=None, handler=None):
        self.name = name
        self.child = dict()
        self.handler = handler

    def insert(self, name, handler):
        if name not in self.child:
            new_node = RouteTrieNode(name=name, handler=handler)
            self.child[name] = new_node
            return new_node
        else:
            return self.child[name]


class RouteTrie:
    def __init__(self, root_handler, not_found_handler):
        self.root = RouteTrieNode(name='root', handler=root_handler)
        self.not_found_handler = not_found_handler

    def insert(self, paths, handler):
        parent_node = self.root

        for i, path in enumerate(paths):
            deepest = i == len(paths) - 1  # deepest node will be assigned the handler
            path_handler = handler if deepest else None
            parent_node = parent_node.insert(name=path, handler=path_handler)

    def find(self, paths):
        head = self.root

        for i, path in enumerate(paths):
            if path not in head.child:
                return self.not_found_handler

            head = head.child[path]

        # if no handler is assigned to the node, return not found
        return head.handler or self.not_found_handler


class Router:
    def __init__(self, root_handler, not_found_handler):
        if not any([callable(root_handler), callable(not_found_handler)]):
            raise ValueError('Handlers should be functions')

        self._route_trie = RouteTrie(
            root_handler=root_handler,
            not_found_handler=not_found_handler
        )

    def add_handler(self, path, handler):
        if type(path) != str or len(path) == 0:
            raise ValueError('Provide a non-empty string value for path')
        if not callable(handler):
            raise ValueError('Handlers should be a function')

        path_list = self.split_path(path)
        self._route_trie.insert(path_list, handler)

    def lookup(self, path):
        if type(path) != str or len(path) == 0:
            raise ValueError('Provide a non-empty string value for path')

        path_list = self.split_path(path)
        return self._route_trie.find(path_list)

    def split_path(self, path):
        # add a trailing slash if missing
        path = f'{path}/' if not path.endswith('/') else path
        path_parts = path.split('/')

        # remove unnecessary parts
        return path_parts[1: -1]


if __name__ == "__main__":
    r = Router(root_handler=lambda: 'Home Page', not_found_handler=lambda: '404 - Not Found')
    r.add_handler('/faq', handler=lambda: 'Faq Page')
    r.add_handler('/course/dsand/', handler=lambda: 'DSaND Page')
    r.add_handler('/course/dsand/beta', handler=lambda: 'Beta Page')

    def test_case1():
        page = r.lookup('/')()
        assert page == 'Home Page'

    def test_case2():
        page = r.lookup('/faq/1')()
        assert page == '404 - Not Found'

    def test_case3():
        page = r.lookup('/course/dsand/beta/')()
        assert page == 'Beta Page'

    def test_case4():
        try:
            r.lookup(None)
        except ValueError:
            assert True
        else:
            raise AssertionError

    def test_case5():
        try:
            r.add_handler(path='/contact-us', handler='')
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
