from markdown_to_blocks import markdown_to_blocks
import unittest


class TestMarkdownToBlock(unittest.TestCase):

    def test_markdown_text(self):
        text = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""

        
        
        self.assertEqual(markdown_to_blocks(text),['# This is a heading', 'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', '* This is the first list item in a list block\n* This is a list item\n* This is another list item'])
     
    def test_another_markdown_text(self):
        markdown = """### My items\n\n- cookies\n- chicken\n- candies"""
        self.assertEqual(markdown_to_blocks(markdown), ['### My items', "- cookies\n- chicken\n- candies"])

if __name__ == '__main__':
    unittest.main()