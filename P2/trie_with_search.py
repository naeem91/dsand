
class TrieNode:
    def __init__(self, value='', word=False):
        self.value = value
        self.child = dict()
        self.word = word

    def insert(self, char, is_word):
        if char not in self.child:
            new_node = TrieNode(value=char, word=is_word)
            self.child[char] = new_node
            return new_node
        else:
            return self.child[char]

    def suffixes(self, suffix=''):
        suffixes = []

        suffix = ''.join([suffix, self.value])

        if self.word:
            suffixes.append(suffix)

        for node in self.child.values():
            child_suffixes = node.suffixes(suffix)
            suffixes.extend(child_suffixes)

        return suffixes

    def child_suffixes(self):
        # all suffixes below this node
        suffixes = []
        for node in self.child.values():
            child_suffixes = node.suffixes()
            suffixes.extend(child_suffixes)

        return suffixes


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        if type(word) != str or len(word) == 0:
            raise ValueError('Provide a non-empty string for insertion')

        parent_node = self.root

        for i, ch in enumerate(word):
            is_word = i == len(word) - 1  # mark last node as representing a complete word
            parent_node = parent_node.insert(char=ch, is_word=is_word)

    def find(self, prefix):
        if type(prefix) != str or len(prefix) == 0:
            raise ValueError('Provide a non-empty string as prefix')

        head = self.root
        for ch in prefix:
            if ch not in head.child:
                return None

            head = head.child[ch]

        return head


if __name__ == "__main__":
    trie = Trie()
    words = [
        "ant", "anthology", "antagonist", "antonym",
        "fun", "function", "factory",
        "trie", "trigger", "trigonometry", "tripod"
    ]

    for word in words:
        trie.insert(word)

    def test_case1():
        node = trie.find('ant')
        assert node.child_suffixes() == ['hology', 'agonist', 'onym']

    def test_case2():
        node = trie.find('fu')
        assert node.child_suffixes() == ['n', 'nction']

    def test_case3():
        node = trie.find('tried')
        assert node is None

    def test_case4():
        try:
            trie.find(None)
        except ValueError:
            assert True
        else:
            raise AssertionError

    def test_case5():
        try:
            t = Trie()
            t.insert('')
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


