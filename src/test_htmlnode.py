import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode
from text_node_to_html import text_node_to_html_node

class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )
    
    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, None, {'class': 'primary'})",
        )
    


class TestLeafNode(unittest.TestCase):
    def test_eq1(self):
        leafnode = LeafNode("p", "This is a paragraph of text.")
        leafnode_html = leafnode.to_html()
        self.assertEqual(leafnode_html,"<p>This is a paragraph of text.</p>" )
    
    def test_eq2(self):
        leafnode = LeafNode("a", "Click me!", {"href":"https://www.google.com"})
        leafnode_html = leafnode.to_html()
        self.assertEqual(leafnode_html,'<a href="https://www.google.com">Click me!</a>')

    def test_no_values(self):
        leafnode = LeafNode("p",)
        with self.assertRaises(ValueError):
            leafnode.to_html()

    def test_raw_text(self):
        leafnode = LeafNode("", "This is a raw text")
        leafnode_html = leafnode.to_html()
        self.assertEqual(leafnode_html, "This is a raw text")
    
class TestParentNode(unittest.TestCase):
    def  test_node(self):
        node = ParentNode("p", [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
        ],)

        self.assertEqual(node.to_html(),"<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_node_with_props(self):
         node = ParentNode("p", [
        LeafNode("b", "Bold text", {"color":"red"}),
        LeafNode(None, "Normal text",),
        LeafNode("i", "italic text", {"color":"blue"}),
        LeafNode(None, "Normal text"),
        ], {"font": 15})

         self.assertEqual(node.to_html(),'<p font="15"><b color="red">Bold text</b>Normal text<i color="blue">italic text</i>Normal text</p>')
         self.assertEqual(node.props_to_html(), ' font="15"')

      
    def test_children(self):
        node = ParentNode("p",[])
        with self.assertRaises(ValueError):
            node.to_html()
    def test_nested_node(self):
        node=ParentNode("div", [ParentNode("p", [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text")],),LeafNode("i", "italic text") ])

        self.assertEqual(node.to_html(), '<div><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p><i>italic text</i></div>')

class TestTextToLeafNode(unittest.TestCase):
    def test_bold(self):
        textnode = TextNode("This is a text node", "bold")
        leafnode = text_node_to_html_node(textnode)
        self.assertEqual(LeafNode("b", "This is a text node").to_html(), leafnode.to_html())
    
    def test_italic(self):
        textnode = TextNode("This is a text node", "italic")
        leafnode = text_node_to_html_node(textnode)
        self.assertEqual(LeafNode("i", "This is a text node").to_html(), leafnode.to_html())

    def test_text(self):
        textnode = TextNode("This is a text", "text")
        leafnode = text_node_to_html_node(textnode)
        self.assertEqual(LeafNode("", "This is a text").to_html(), leafnode.to_html())

    def test_image(self):
        textnode = TextNode("This is an image", "image", "boot.dev")
        leafnode = text_node_to_html_node(textnode)
        self.assertEqual(leafnode.to_html(), LeafNode("img","", {"src": "boot.dev", "alt": "This is an image"}).to_html())

    def test_link(self):
        textnode = TextNode("This is a link", "link", "boot.dev")
        leafnode = text_node_to_html_node(textnode)
        self.assertEqual(leafnode.to_html(), LeafNode("a","This is a link",{"href": "boot.dev"}).to_html())

    def test_no_case(self):
        textnode = TextNode("This is a text node", "random")
        with self.assertRaises(Exception):
            text_node_to_html_node(textnode)


if __name__ == "__main__":
    unittest.main(verbosity=2)