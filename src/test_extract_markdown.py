import unittest
from extract_markdown import extract_markdown_images, extract_markdown_links


class TestExtractImage(unittest.TestCase):
    def test_extract_image(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        extracted_images = extract_markdown_images(text)
        self.assertEqual(extracted_images, [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])


class TestExtractLink(unittest.TestCase):
    def test_extract_link(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        extracted_links = extract_markdown_links(text)
        self.assertEqual(extracted_links, [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")])

class TestIfItWorks(unittest.TestCase):
    def test_random_test(self):
        self.assertEqual(1, 1)



if __name__ == '__main__':
    unittest.main(verbosity=2)