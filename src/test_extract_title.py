import unittest
from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_single_line_title(self):
        title = "# Hello"
        self.assertEqual(extract_title(title), "Hello")
    def test_multi_line_markdown(self):
        title = """# Title 
This is the first line of the paragraph
This is the second line. And so on."""
        self.assertEqual(extract_title(title), "Title" )
    
    def test_no_header(self):
        title = """There are no headers
There are no lovers.
There are no winners"""
        with self.assertRaises(Exception):
            extract_title(title)
        
    def test_in_the_middle_header(self):
        title = """
Love
# A true story"""
        self.assertEqual(extract_title(title), "A true story")



if __name__ == '__main__':
    unittest.main(verbosity=2)