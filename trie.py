import unittest


class Node(object):
    def __init__(self, val, is_word = False):
        self.char = val
        self.is_word = is_word
        self.nodes = {}

    def add_char(self, char):
        if char not in self.nodes:
            self.nodes[char] = Node(char)
    def add_word(self, chars):
        if len(chars) == 0:
            return
        self.add_char(chars[0])
        if len(chars) == 1:
            self.nodes[chars[0]].is_word = True
        elif len(chars) > 1:
            self.nodes[chars[0]].add_word(chars[1:])
    def word_exists(self, word):
        if not word:
            return self.is_word
        if word[0] in self.nodes:
            return self.nodes[word[0]].word_exists(word[1:])
        return False

class Trie(Node):
    def __init__(self):
        super(Trie,self).__init__(None,False)


class TrieTests(unittest.TestCase):
    def test_empty(self):
        empty_root = Trie()
        self.assertFalse(empty_root.is_word)
        self.assertFalse(empty_root.nodes)
        self.assertFalse(empty_root.char)
    def test_add_char(self):
        root = Trie()
        root.add_char('a')
        self.assertTrue('a' in root.nodes)
        self.assertEqual(root.nodes['a'].char, 'a')
        root.add_char('b')
        self.assertTrue('b' in root.nodes)
        self.assertEqual(root.nodes['b'].char, 'b')
    def test_add_char(self):
        root = Trie()
        root.add_word('abc')

        self.assertTrue('a' in root.nodes)
        a_node = root.nodes['a']
        self.assertEqual(a_node.char, 'a')
        self.assertFalse(a_node.is_word)

        self.assertTrue('b' in a_node.nodes)
        b_node = a_node.nodes['b']
        self.assertEqual(b_node.char, 'b')
        self.assertFalse(b_node.is_word)

        self.assertTrue('c' in b_node.nodes)
        c_node = b_node.nodes['c']
        self.assertEqual(c_node.char, 'c')
        self.assertTrue(c_node.is_word)

if __name__=="__main__":
    unittest.main()
    import pdb
    pdb.set_trace()
    trie = Trie()



