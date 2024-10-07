import unittest
from block_to_block_type import block_to_block_type

class TestBlocks(unittest.TestCase):
    def test_heading_block(self):
        heading1 = "# This is a heading 1"
        self.assertEqual(block_to_block_type(heading1), 'heading')
        heading2 = "## This is a heading 2"
        self.assertEqual(block_to_block_type(heading2), 'heading')
        heading6 = "###### This is a heading 6"
        self.assertEqual(block_to_block_type(heading6), 'heading')
        heading7 = "######## This is not a a heading"
        self.assertEqual(block_to_block_type(heading7), 'paragraph')
    
    def test_code_block(self):
        code_block = "```this is a code block```"
        self.assertEqual(block_to_block_type(code_block), "code")
        not_code_block = "``this is not a code block``"
        self.assertEqual(block_to_block_type(not_code_block), "paragraph")
    
    def test_quote_block(self):
        single_quote_block = ">This is a quote"
        self.assertEqual(block_to_block_type(single_quote_block), "quote")
        multiple_quote_block = ">This is first quote/\n>This is second quote\n>This is third quote"
        self.assertEqual(block_to_block_type(multiple_quote_block), "quote")

    
    def test_unordered_list(self):
        single_list = "- This is a single list"
        self.assertEqual(block_to_block_type(single_list), "unordered_list")
        multiple_line_list = "- This is first list\n- This is the second list\n- This is third"
        self.assertEqual(block_to_block_type(multiple_line_list), "unordered_list")
    
    def test_ordered_list(self):
        single_ordered_list = "1. This is a single ordered list"
        self.assertEqual(block_to_block_type(single_ordered_list), "ordered_list")
        multiple_ordered_list = "1. This is a single ordered list\n2. This is second line.\n3. And this is third"
        self.assertEqual(block_to_block_type(multiple_ordered_list), "ordered_list")




if __name__ == "__main__":
    unittest.main(verbosity=2)




