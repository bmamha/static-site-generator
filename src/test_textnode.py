import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_eq_2(self):
        node = TextNode("This is a test node", "italic", "boot.dev")
        node2 = TextNode("This is a test node", "italic", "boot.dev")
        self.assertEqual(node, node2)
    
    def test_eq_3(self):
        node = TextNode("Third test node", "normal")
        node2 = TextNode("different test node", "normal")
        self.assertNotEqual(node,node2)
    
    def test_eq_4(self):
         node = TextNode("Fourth test node", "italic",)
         node2 = TextNode("Fourth test node", "italic", "boot.dev")
         self.assertNotEqual(node,node2)

if __name__ == "__main__":
    unittest.main(verbosity=2)