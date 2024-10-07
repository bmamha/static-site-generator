from split_nodes_image_and_link import split_nodes_link, split_nodes_image
from textnode import TextNode
import unittest


class TestLink(unittest.TestCase):
    def test_split_links(self):
        node = TextNode("This is a text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)","text")
        new_nodes = split_nodes_link([node])
        self.assertEqual(len(new_nodes), 4)
        self.assertEqual(new_nodes[0].text, "This is a text with a link ")
        self.assertEqual(new_nodes[0].text_type, "text")
        self.assertEqual(new_nodes[1].text, "to boot dev")
        self.assertEqual(new_nodes[1].text_type, "link")
        self.assertEqual(new_nodes[1].url, "https://www.boot.dev")
        self.assertEqual(new_nodes[2].text, " and ")
        self.assertEqual(new_nodes[2].text_type, "text")
        self.assertEqual(new_nodes[3].text, "to youtube")
        self.assertEqual(new_nodes[3].text_type, "link")
        self.assertEqual(new_nodes[3].url, "https://www.youtube.com/@bootdotdev")

class TestImage(unittest.TestCase):
    def test_split_images(self):
        node = TextNode("![a boat](https://boat.com) and a ![cat](cats.com/img1)", "text")
        new_nodes = split_nodes_image([node])
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text, "a boat")
        self.assertEqual(new_nodes[0].text_type, "image")
        self.assertEqual(new_nodes[0].url, "https://boat.com")
        self.assertEqual(new_nodes[1].text, " and a ")
        self.assertEqual(new_nodes[1].text_type, "text")
        self.assertEqual(new_nodes[2].text, "cat")
        self.assertEqual(new_nodes[2].text_type, "image")
        self.assertEqual(new_nodes[2].url, "cats.com/img1")

class TestLinks(unittest.TestCase):
    def test_image_case(self):
        text = "This is a text with a [link url](boot.dev) in the middle. We are testing if the last parts get picked up in our split link function"
        node = TextNode(text, "text")
        new_nodes = split_nodes_link([node])
        self.assertEqual(new_nodes[0].text, "This is a text with a ")
        self.assertEqual(new_nodes[1].text, "link url")
        self.assertEqual(new_nodes[1].text_type, "link")
        self.assertEqual(new_nodes[2].text, " in the middle. We are testing if the last parts get picked up in our split link function")

        




class TestImageAndLink(unittest.TestCase):
    def test_image_and_link(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        node = TextNode(text, "text")
        new_image_nodes = split_nodes_image([node])
        new_link_nodes = split_nodes_link(new_image_nodes)
        self.assertEqual(new_link_nodes[0].text, "This is **text** with an *italic* word and a `code block` and an " )
        self.assertEqual(new_link_nodes[1].text, "obi wan image")
        self.assertEqual(new_link_nodes[1].text_type, "image")
        self.assertEqual(new_link_nodes[2].text, " and a ")
        self.assertEqual(new_link_nodes[3].text, "link")
        self.assertEqual(new_link_nodes[3].text_type, "link")


if __name__ == "__main__":
    unittest.main(verbosity=2)


