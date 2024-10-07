from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode
import unittest
from extract_markdown import extract_markdown_images, extract_markdown_links



class TestSplitNodesDelimiter(unittest.TestCase):

    def test_single_node_code(self):
        node = TextNode("This is a text with a `code block` word", "text")
        new_nodes = split_nodes_delimiter([node], "`", "code")
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text, "This is a text with a ")
        self.assertEqual(new_nodes[0].text_type, "text")
        self.assertEqual(new_nodes[1].text_type, "code")
        self.assertEqual(new_nodes[1].text, "code block")
        self.assertEqual(new_nodes[2].text_type, "text")
        self.assertEqual(new_nodes[2].text, " word")

    
    def test_single_node_bold(self):
        node = TextNode("This is a text with a **bold word** in it", "text")
        new_nodes = split_nodes_delimiter([node], "**", "bold")
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text, "This is a text with a ")
        self.assertEqual(new_nodes[0].text_type, "text")
        self.assertEqual(new_nodes[1].text_type, "bold")
        self.assertEqual(new_nodes[1].text, "bold word")
        self.assertEqual(new_nodes[2].text_type, "text")
        self.assertEqual(new_nodes[2].text, " in it")

    def test_single_node_italic(self):
        node = TextNode("This is a text with an *italic word* in it", "text")
        new_nodes = split_nodes_delimiter([node], "*", "italic")
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text, "This is a text with an ")
        self.assertEqual(new_nodes[0].text_type, "text")
        self.assertEqual(new_nodes[1].text_type, "italic")
        self.assertEqual(new_nodes[1].text, "italic word")
        self.assertEqual(new_nodes[2].text_type, "text")
        self.assertEqual(new_nodes[2].text, " in it")
    
    def test_wrong_delimeter(self):
        node = TextNode("This is a text with an *italic word* in it", "text")
        with self.assertRaises(Exception):
            new_node = split_nodes_delimiter([node], "/","text")

    def test_non_text_node(self):
        node = TextNode("This is *not* a text", "not a text")
        new_nodes = split_nodes_delimiter([node], "*", "bold")
        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(new_nodes[0].text, "This is *not* a text")
        self.assertEqual(new_nodes[0].text_type, "not a text")

    def test_single_node_multiple_delimeter(self):
        node = TextNode("This has **two** bold **texts** within text", "text")
        new_node = split_nodes_delimiter([node], "**", "bold")
        self.assertEqual(len(new_node), 5)
        self.assertEqual(new_node[0].text, "This has ")
        self.assertEqual(new_node[0].text_type, "text")
        self.assertEqual(new_node[1].text, "two")
        self.assertEqual(new_node[1].text_type, "bold")
        self.assertEqual(new_node[2].text, " bold ")
        self.assertEqual(new_node[2].text_type, "text")
        self.assertEqual(new_node[3].text, "texts")
        self.assertEqual(new_node[3].text_type, "bold")
        self.assertEqual(new_node[4].text, " within text")
        self.assertEqual(new_node[4].text_type, "text")
    
    def test_multiple_nodes(self):
        node1 = TextNode("This has **two** bold **texts** within text", "text")
        node2 = TextNode("This is a text with a **bold word** in it", "text")
        new_node = split_nodes_delimiter([node1, node2], "**", "bold")
        self.assertEqual(len(new_node), 8)
        self.assertEqual(new_node[0].text, "This has ")
        self.assertEqual(new_node[1].text, "two")
        self.assertEqual(new_node[1].text_type, "bold")
        self.assertEqual(new_node[7].text, " in it")
    




    
if __name__ == '__main__':
    unittest.main(verbosity=2)
        









    





