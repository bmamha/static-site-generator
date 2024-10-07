import unittest
from markdown_to_html_node import markdown_to_html_node, count_heading, children_for_list
from htmlnode import HTMLNode, LeafNode



class TestHeadingType(unittest.TestCase):
    def test_header_count(self):
        heading1 = "# Header 1"
        self.assertEqual(count_heading(heading1), (1, "Header 1"))
        heading2 = "## Header 2"
        self.assertEqual(count_heading(heading2), (2, "Header 2"))
        heading6 = "###### Header 6"
        self.assertEqual(count_heading(heading6), (6, "Header 6"))


class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_single_header_leaf(self):
        markdown = "### I am just an ordinary header"
        node = markdown_to_html_node(markdown)
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.to_html(),"<div><h3>I am just an ordinary header</h3></div>")
    
    def test_header_and_list_nodes(self):
        markdown = """### My items\n\n- cookies\n- chicken\n- candies"""
        node = markdown_to_html_node(markdown)
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.to_html(), "<div><h3>My items</h3><ul><li>cookies</li><li>chicken</li><li>candies</li></ul></div>")
    
    def test_another_list_node(self):
        text = """# This is a *heading*

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""
        
        node = markdown_to_html_node(text)
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.to_html(),"<div><h1>This is a <i>heading</i></h1><p>This is a paragraph of text. It has some <b>bold</b> and <i>italic</i> words inside of it.</p><ul><li>This is the first list item in a list block</li><li>This is a list item</li><li>This is another list item</li></ul></div>")

    def test_node_with_a_code(self):
        text = "There are many ways to write code. For example:\n\n```python x = 3 + 4```"
        node = markdown_to_html_node(text)
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.to_html(), "<div><p>There are many ways to write code. For example:</p><pre><code>python x = 3 + 4</code></pre></div>")


class TestChildrenOfList(unittest.TestCase):

    def test_children_unordered_list(self):
        unorderedList = "- Oranges are the new black\n- Apple\n- Carrots"
        children = children_for_list(unorderedList)
        self.assertEqual(children[0].children[0].value, "Oranges are the new black")
        self.assertEqual(children[0].tag, "li")
        self.assertEqual(children[1].children[0].value, "Apple")
        self.assertEqual(children[2].children[0].value, "Carrots")

    def test_children_ordered_list(self):
        ordered_list = "1. Apple\n2. Orange\n3. Pear"
        children = children_for_list(ordered_list)
        self.assertEqual(children[0].children[0].value, "Apple")
        self.assertEqual(children[0].tag, "li")
        self.assertEqual(children[1].children[0].value, "Orange")
        self.assertEqual(children[2].children[0].value, "Pear")

class TestQuoteMarkdown(unittest.TestCase):
    def test_quote(self):
        quote = """> This is first quote.
> This is second quote.
> This is third quote."""
        node = markdown_to_html_node(quote)
        self.assertEqual(node.to_html(),"<div><blockquote><p>This is first quote. This is second quote. This is third quote.</p></blockquote></div>")

if __name__ == '__main__':
    unittest.main()